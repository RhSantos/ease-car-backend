from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Rental
from api.serializers import RentalSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def list(self, request):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return success_response({"rentals": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            rental = self.get_object()
            serializer = RentalSerializer(rental)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Rental not found")

    def create(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"rental": serializer.data}, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            rental = self.get_object()
        except Http404:
            return error_response("Rental not found")

        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            rental = self.get_object()
            rental.delete()
        except Http404:
            return error_response("Rental not found")
        return success_response()
