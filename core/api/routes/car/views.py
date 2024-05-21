from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser

from core.api.models import Car
from core.api.serializers import CarSerializer
from core.utils.jsend_responses import *


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):

        admin_only = ["create", "update", "destroy"]

        if self.action in admin_only:
            return [
                IsAdminUser(),
            ]
        return []

    def list(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return success_response(key="cars", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            car = self.get_object()
            serializer = CarSerializer(car)
            return success_response(key="car", data=serializer.data)
        except Http404:
            return error_response("Car not found")

    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="car", data=serializer.data, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            car = self.get_object()
        except Http404:
            return error_response("Car not found")

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(key="car", data=serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            car = self.get_object()
            car.delete()
        except Http404:
            return error_response("Car not found")
        return success_response()
