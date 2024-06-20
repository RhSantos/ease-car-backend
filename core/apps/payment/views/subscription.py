import uuid
from http import HTTPMethod

from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.general.utils.helpers import AsaasResourceUrl
from core.general.utils.network import make_asaas_api_call
from core.general.utils.responses import *

from ..models import Subscription
from ..serializers import SubscriptionRequestSerializer, SubscriptionResponseSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionRequestSerializer

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
        Asaas Subscription Creation Example Request:

        {
            "customer": "cus_0T1mdomVMi39",
            "billingType": "CREDIT_CARD",
            "value": 19.9,
            "cycle": "MONTHLY",
            "nextDueDate": "2017-05-15",
            "discount": {
                "value": 19.9,
                "dueDateLimitDays": 0,
                "type": "PERCENTAGE"
            },
            "interest": {
                "value": 19.9
            },
            "fine": {
                "value": 19.9,
                "type": "FIXED"
            },
            "description": "Pro Plan Subscription"
        }
        """

        serializer = SubscriptionRequestSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            customer = validated_data.get("customer")

            if customer.person == request.user:

                if Subscription.objects.filter(customer=customer).exists():
                    return fail_response(
                        errors={"subscription": "Already subscribed"},
                        status=status.HTTP_409_CONFLICT,
                    )

                payment_gateway_request_data = {
                    "customer": customer,
                    "billingType": validated_data.get("billing_type"),
                    "value": validated_data.get("value"),
                    "cycle": validated_data.get("cycle"),
                    "nextDueDate": validated_data.get("next_due_date"),
                    "description": validated_data.get("description"),
                }

                if validated_data.get("discount_percentage"):
                    payment_gateway_request_data["discount"] = {
                        "value": validated_data.get("discount_percentage"),
                        "type": "PERCENTAGE",
                    }

                if validated_data.get("interest_value"):
                    payment_gateway_request_data["interest"] = (
                        {"value": validated_data.get("interest_value")},
                    )

                if validated_data.get("fine_value"):
                    payment_gateway_request_data["fine"] = (
                        {"value": validated_data.get("customer"), "type": "FIXED"},
                    )

                payment_gateway_response = make_asaas_api_call(
                    method=HTTPMethod.POST,
                    request_data=payment_gateway_request_data,
                    api_resource=AsaasResourceUrl.SUBSCRIPTION,
                )

                if payment_gateway_response.status_code == 200:

                    response_data = payment_gateway_response.json()

                    subscription = Subscription(
                        id=uuid.UUID(response_data["id"]),
                        owner=customer,
                        income_value=validated_data.get("income_value"),
                        income_range=response_data["incomeRange"],
                        api_key=response_data["apiKey"],
                        wallet_id=response_data["walletId"],
                        account_agency=response_data["accountNumber"]["agency"],
                        account_number=response_data["accountNumber"]["account"],
                        account_digit=response_data["accountNumber"]["accountDigit"],
                    )
                    response_serializer = SubscriptionResponseSerializer(subscription)

                    if response_serializer.is_valid():
                        response_serializer.save()

                        return success_response(
                            key="subscription", data=payment_gateway_request_data
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
            subscription = self.get_object()

            if subscription.owner == request.user:
                serializer = SubscriptionResponseSerializer(subscription)
                return success_response(key="subscription", data=serializer.data)

            return fail_response(
                errors={"user": "You are not Sub Account Owner"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Http404:
            return error_response("Sub Account not found")
