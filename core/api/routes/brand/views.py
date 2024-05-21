from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from core.api.models import Brand
from core.api.serializers import BrandSerializer
from core.utils.jsend_responses import success_response


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
