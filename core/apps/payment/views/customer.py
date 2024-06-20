from http import HTTPMethod

from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.general.utils.helpers import AsaasResourceUrl
from core.general.utils.network import make_asaas_api_call
from core.general.utils.responses import *

from ..models import Customer
from ..serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):

        admin_only = ["create", "update", "destroy", "list"]

        if self.action in admin_only:
            return [
                IsAdminUser(),
            ]
        return [
            IsAuthenticated(),
        ]

    def create(self, request):
        """
        Asaas Customer Creation Example Request:

        {
            "name": "John Doe",
            "cpfCnpj": "24971563792",
            "email": "john.doe@asaas.com.br",
            "mobilePhone": "4799376637",
            "address": "Avenida Paulista",
            "province": "São Paulo",
            "postalCode": "01310-930",
            "addressNumber": "150",
            "complement": "Sala 201",
            "observations": "Test Payment - ASAAS CUSTOMER",
            "notificationDisabled": false
        }
        """

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            person = validated_data.get("person")

            if Customer.objects.filter(person=person).exists():
                return fail_response(
                    errors={"customer": "Already created"},
                    status=status.HTTP_409_CONFLICT,
                )

            payment_gateway_request_data = {
                "name": person.get_full_name(),
                "cpfCnpj": person.cpf,
                "email": person.email,
                "mobilePhone": person.mobile_phone,
                "address": person.address.street,
                "province": person.address.province,
                "postalCode": person.address.postal_code,
                "addressNumber": person.address.number,
                "complement": person.address.complement,
                "observations": validated_data.get("observations"),
                "notificationDisabled": validated_data.get("notification_disabled"),
            }

            payment_gateway_response = make_asaas_api_call(
                method=HTTPMethod.POST,
                request_data=payment_gateway_request_data,
                api_resource=AsaasResourceUrl.CUSTOMER,
            )

            if payment_gateway_response.status_code == 200:

                response_data = payment_gateway_response.json()

                validated_data["id"] = response_data["id"]

                serializer.save()

                return success_response(key="customer", data=serializer.data)

            errors = {
                value["code"]: value["description"]
                for value in payment_gateway_response.json()["errors"]
            }

            return fail_response(
                errors,
                status=payment_gateway_response.status_code,
            )

        return fail_response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            customer = self.get_object()

            if customer.owner == request.user:
                serializer = CustomerSerializer(customer)
                return success_response(key="customer", data=serializer.data)

            return fail_response(
                errors={"user": "You are not Customer Person"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Http404:
            return error_response("Customer not found")
