from rest_framework import status
from rest_framework.generics import CreateAPIView

from utils.jsend_responses import *

from .models import Address
from .serializers import RegisterSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="user", data=serializer.data, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)
