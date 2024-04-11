from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.models import Payment
from api.serializers import PaymentSerializer
from authentication.models import ProfileUser
from utils.jsend_responses import *


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

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
        serializer = PaymentSerializer(payments, many=True)
        return success_response(key="payments", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            payment = self.get_object()

            if payment.owner == request.user:
                serializer = PaymentSerializer(payment)
                return success_response(key="payment", data=serializer.data)

            return fail_response(
                errors= {"user": "You are not Payment Owner"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Http404:
            return error_response("Payment not found")
