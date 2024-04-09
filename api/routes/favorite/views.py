from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Favorite
from api.serializers import FavoriteSerializer
from utils.jsend_responses import *


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many=True)
        return success_response(key="favorites", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            favorite = self.get_object()
            serializer = FavoriteSerializer(favorite)
            return success_response(key="favorite", data=serializer.data)
        except Exception:
            return error_response("Favorite not found")

    def create(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"favorite": serializer.data}, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            favorite = self.get_object()
        except Http404:
            return error_response("Favorite not found")

        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            favorite = self.get_object()
            favorite.delete()
        except Http404:
            return error_response("Favorite not found")
        return success_response()
