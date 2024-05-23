from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from core.api.models import Review
from core.api.serializers import ReviewSerializer
from core.general.utils.responses import *


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return success_response(key="reviews", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            review = self.get_object()
            serializer = ReviewSerializer(review)
            return success_response(key="review", data=serializer.data)
        except Exception:
            return error_response("Review not found")

    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="review", data=serializer.data, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            review = self.get_object()
        except Http404:
            return error_response("Review not found")

        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(key="review", data=serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            review = self.get_object()
            review.delete()
        except Http404:
            return error_response("Review not found")
        return success_response()
