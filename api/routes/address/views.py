from django.http.response import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from authentication.models import Address
from api.serializers import AddressSerializer
from api.utils.jsend_responses import error_response, fail_response, success_response


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return success_response({"addresses": serializer.data})

    def retrieve(self, request, pk=None):
        try:
            address = self.get_object()
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        except Exception as e:
            print(e.__class__)
            return error_response("Address not found")

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                {"address": serializer.data}, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)

    def update(self, request, pk=None):
        try:
            address = self.get_object()
        except Http404:
            return error_response("Address not found")

        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return fail_response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            address = self.get_object()
            address.delete()
        except Http404:
            return error_response("Address not found")
        return success_response()
