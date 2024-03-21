from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Brand
from api.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
