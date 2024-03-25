from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Review
from api.serializers import ReviewSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return success_response({"reviews": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            review = self.get_object()
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Review not found")

    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"review": serializer.data}, status=status.HTTP_201_CREATED
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
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            review = self.get_object()
            review.delete()
        except Http404:
            return error_response("Review not found")
        return success_response()
