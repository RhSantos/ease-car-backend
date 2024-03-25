from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Booking
from api.serializers import BookingSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return success_response({"bookings": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            booking = self.get_object()
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Booking not found")

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"booking": serializer.data}, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            booking = self.get_object()
        except Http404:
            return error_response("Booking not found")

        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            booking = self.get_object()
            booking.delete()
        except Http404:
            return error_response("Booking not found")
        return success_response()
