from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Brand
from api.serializers import BrandSerializer


@api_view(["GET"])
def get_all_brands(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)
