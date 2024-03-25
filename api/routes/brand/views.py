from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Brand
from api.serializers import BrandSerializer
from api.utils.jsend_responses import success_response


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return success_response({"brands": serializer.data})
