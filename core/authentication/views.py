from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.authentication.models import ProfileUser
from core.general.utils.responses import *

from .models import Address
from .serializers import LoginSerializer, RegisterSerializer


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


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")
            user = ProfileUser.objects.get(email=email)

            if not user:
                return error_response("User not found")

            if user.check_password(password):

                refresh_token = RefreshToken.for_user(user)
                user_serializer = RegisterSerializer(user)

                data = {
                    "user": user_serializer.data,
                    "access-token": str(refresh_token.access_token),
                    "refresh-token": str(refresh_token),
                }

                return success_response(
                    key="auth", data=data, status=status.HTTP_201_CREATED
                )
        return fail_response(serializer.errors)
