from rest_framework import status
from rest_framework.generics import CreateAPIView

from utils.jsend_responses import *

from .models import Address
from .serializers import ProfileUserSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = ProfileUserSerializer

    def post(self, request):
        serializer = ProfileUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="user", data=serializer.data, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)
