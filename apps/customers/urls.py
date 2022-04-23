from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from apps.customers.views import create_customer, manage_customer

urlpatterns = [
    path('signup', create_customer, name="create_customer"),
    path('login', obtain_jwt_token, name="login_customer"),
    path('me', manage_customer, name="manage_customer")
]