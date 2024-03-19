from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Car
from api.serializers import CarSerializer


@api_view(["GET"])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)