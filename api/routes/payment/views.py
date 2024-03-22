from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Payment
from api.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            payment = self.get_object()
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            payment = self.get_object()
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment = self.get_object()
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
