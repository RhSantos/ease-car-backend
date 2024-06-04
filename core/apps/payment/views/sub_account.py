import uuid

from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.general.utils.helpers import AsaasResourceUrl
from core.general.utils.network import make_asaas_api_call
from core.general.utils.responses import *

from ..models import SubAccount
from ..serializers import SubAccountRequestSerializer, SubAccountResponseSerializer


class SubAccountViewSet(viewsets.ModelViewSet):

    queryset = SubAccount.objects.all()
    serializer_class = SubAccountRequestSerializer

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
        Asaas Sub Account Creation Example Request:

        {
            "incomeValue": 25000,
            "name": "teste",
            "email": "teste@gmail.com",
            "cpfCnpj": "66625514000140",
            "birthDate": "1994-05-16",
            "mobilePhone": "11 988451155",
            "addressNumber": "277",
            "address": "Av. Rolf Wiest",
            "complement": "Sala 502",
            "province": "Bom Retiro",
            "postalCode": "89223005"
        }
        """

        serializer = SubAccountRequestSerializer(data=request.data)

        if SubAccount.objects.filter(owner=request.user).exists():
            return fail_response(
                errors={"sub_account": "Already created"},
                status=status.HTTP_409_CONFLICT,
            )

        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = validated_data.get("owner")

            if user != None and user == request.user:
                payment_gateway_request_data = {
                    "incomeValue": 25000,
                    "name": user.get_full_name(),
                    "email": user.email,
                    "cpfCnpj": user.cpf,
                    "birthDate": str(user.birth_date),
                    "mobilePhone": user.mobile_phone,
                    "addressNumber": user.address.number,
                    "address": user.address.street,
                    "complement": user.address.complement,
                    "province": user.address.province,
                    "postalCode": user.address.postal_code,
                }

                payment_gateway_response = make_asaas_api_call(
                    payment_gateway_request_data, AsaasResourceUrl.SUB_ACCOUNT
                )

                if payment_gateway_response.status_code == 200:

                    response_data = payment_gateway_response.json()

                    sub_account = {
                        "id": uuid.UUID(response_data["id"]),
                        "owner": user,
                        "income_value": validated_data.get("income_value"),
                        "income_range": response_data["incomeRange"],
                        "api_key": response_data["apiKey"],
                        "wallet_id": response_data["walletId"],
                        "account_agency": response_data["accountNumber"]["agency"],
                        "account_number": response_data["accountNumber"]["account"],
                        "account_digit": response_data["accountNumber"]["accountDigit"],
                    }

                    response_serializer = SubAccountResponseSerializer(data=sub_account)

                    if response_serializer.is_valid():
                        response_serializer.save()

                        return success_response(
                            key="sub_account", data=payment_gateway_request_data
                        )

                    return fail_response(response_serializer.errors)

                errors = {
                    value["code"]: value["description"]
                    for value in payment_gateway_response.json()["errors"]
                }

                return fail_response(
                    errors,
                    status=payment_gateway_response.status_code,
                )

            return fail_response(
                {"user": "You are not Sub Account Owner"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return fail_response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            sub_account = self.get_object()

            if sub_account.owner == request.user:
                serializer = SubAccountResponseSerializer(sub_account)
                return success_response(key="sub_account", data=serializer.data)

            return fail_response(
                errors={"user": "You are not Sub Account Owner"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Http404:
            return error_response("Sub Account not found")
