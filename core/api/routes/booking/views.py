from django.http.response import Http404
from rest_framework import status, viewsets

from core.api.models import Booking
from core.api.serializers import BookingRequestSerializer, BookingResponseSerializer
from core.utils.jsend_responses import *


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingRequestSerializer

    def list(self, request):
        bookings = Booking.objects.all()
        serializer = BookingResponseSerializer(bookings, many=True)
        return success_response(key="bookings", data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            booking = self.get_object()
            serializer = BookingResponseSerializer(booking)
            return success_response(key="bookings", data=serializer.data)
        except Http404:
            return error_response("Booking not found")

    def create(self, request):
        request_serializer = BookingRequestSerializer(data=request.data)
        if request_serializer.is_valid():
            request_serializer.save()
            return success_response(
                key="booking",
                data=request_serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return fail_response(request_serializer.errors)

    def update(self, request, pk=None):
        try:
            booking = self.get_object()
        except Http404:
            return error_response("Booking not found")

        serializer = BookingRequestSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(key="booking", data=serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            booking = self.get_object()
            booking.delete()
        except Http404:
            return error_response("Booking not found")
        return success_response()
