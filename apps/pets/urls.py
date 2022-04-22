from django.urls import path
from apps.pets import views

urlpatterns = [
  path('new', views.add_pet)
]
