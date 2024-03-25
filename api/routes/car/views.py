from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Car
from api.serializers import CarSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return success_response({"cars": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            car = self.get_object()
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Car not found")

    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"car": serializer.data}, status=status.HTTP_201_CREATED
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
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            car = self.get_object()
            car.delete()
        except Http404:
            return error_response("Car not found")
        return success_response()
