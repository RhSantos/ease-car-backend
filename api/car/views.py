from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Car
from api.serializers import CarSerializer


@api_view(["GET"])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=404)
