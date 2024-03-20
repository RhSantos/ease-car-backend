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


@api_view(["POST"])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
