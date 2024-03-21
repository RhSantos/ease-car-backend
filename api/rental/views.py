from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Rental
from api.serializers import RentalSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def list(self, request):
        rental = Rental.objects.all()
        serializer = RentalSerializer(rental, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            rental = self.get_object()
            serializer = RentalSerializer(rental)
            return Response(serializer.data)
        except Rental.DoesNotExist:
            return Response({"error": "Rental not found"}, status=404)

    def create(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            rental = self.get_object()
        except Rental.DoesNotExist:
            return Response(
                {"error": "Rental not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        rental = self.get_object()
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
