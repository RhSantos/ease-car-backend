from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/refresh-token/", TokenRefreshView.as_view()),
    path("auth/register/", RegisterAPIView.as_view()),
    path("auth/login/", LoginAPIView.as_view()),
    path("api/", include("api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
