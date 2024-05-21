from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.api.models import Payment
from core.api.serializers import PaymentResponseSerializer
from core.authentication.models import ProfileUser
from core.utils.jsend_responses import *


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentResponseSerializer

    def get_permissions(self):

        admin_only = ["create", "update", "destroy"]

        if self.action in admin_only:
            return [
                IsAdminUser(),
            ]
        return [
            IsAuthenticated(),
        ]

    def list(self, request):
        payments = Payment.objects.filter(owner=request.user)
        serializer = PaymentResponseSerializer(payments, many=True)
        return success_response(key="payments", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            payment = self.get_object()

            if payment.owner == request.user:
                serializer = PaymentResponseSerializer(payment)
                return success_response(key="payment", data=serializer.data)

            return fail_response(
                errors= {"user": "You are not Payment Owner"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Http404:
            return error_response("Payment not found")
