from books.views import BookViewSet
from books_profiler.views import BookProfilerViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"book", BookViewSet, basename="book")
router.register(r"profile", BookProfilerViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
