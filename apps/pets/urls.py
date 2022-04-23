from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.pets import views

router = DefaultRouter()
router.register('', views.PetViewSet, basename='pets')

urlpatterns = [
    path('', include(router.urls)),
]