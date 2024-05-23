from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from core.general.utils.responses import success_response

from .models import Brand
from .serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):

        admin_only = ["create", "update", "destroy"]

        if self.action in admin_only:
            return [
                IsAdminUser(),
            ]
        return []

    def list(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return success_response(key="brands", data=serializer.data)
