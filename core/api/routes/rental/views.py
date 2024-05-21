from django.http.response import Http404
from rest_framework import status, viewsets

from core.api.models import Rental
from core.api.serializers import RentalSerializer
from core.utils.jsend_responses import *


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def list(self, request):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return success_response(key="rentals", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            rental = self.get_object()
            serializer = RentalSerializer(rental)
            return success_response(key="rental", data=serializer.data)
        except Http404:
            return error_response("Rental not found")

    def create(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="rental", data=serializer.data, status=status.HTTP_201_CREATED
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
            return success_response(key="rental", data=serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            rental = self.get_object()
            rental.delete()
        except Http404:
            return error_response("Rental not found")
        return success_response()
