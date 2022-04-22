from django.urls import path

from apps.customers import views

urlpatterns = [
    path('signup', views.create_customer, name="create_customer"),
    path('me', views.manage_customer, name="manage_customer")
]