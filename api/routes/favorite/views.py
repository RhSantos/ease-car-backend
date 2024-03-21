from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Favorite
from api.serializers import FavoriteSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def list(self, request):
        favorite = Favorite.objects.all()
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            favorite = self.get_object()
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data)
        except Favorite.DoesNotExist:
            return Response({"error": "Favorite not found"}, status=404)

    def create(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            favorite = self.get_object()
        except Favorite.DoesNotExist:
            return Response(
                {"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        favorite = self.get_object()
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
