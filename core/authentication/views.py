from rest_framework import mixins, viewsets
from rest_framework_simplejwt.tokens import RefreshToken

from core.authentication.models import AppUser
from core.general.utils.helpers import format_multipart_form_data_field
from core.general.utils.responses import *

from .serializers import LoginSerializer, RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = RegisterSerializer

    def create(self, request):
        data = format_multipart_form_data_field(request.data, "address")

        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return success_response(
                key="user", data=serializer.data, status=status.HTTP_201_CREATED
            )
        return fail_response(serializer.errors)


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")
            user = AppUser.objects.get(email=email)

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
