from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Register viewsets here (example):
# router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]