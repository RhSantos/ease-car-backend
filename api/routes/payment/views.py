from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Payment
from api.serializers import PaymentSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return success_response({"payments": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            payment = self.get_object()
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Payment not found")

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"payment": serializer.data}, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            payment = self.get_object()
        except Http404:
            return error_response("Payment not found")

        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            payment = self.get_object()
            payment.delete()
        except Http404:
            return error_response("Payment not found")
        return success_response()
