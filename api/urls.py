from django.urls import path
from .views import getUsers, createUser, userDetail

urlpatterns = [
    path("users/", getUsers, name="getUsers"),
    path("users/create", createUser, name="createUser"),
    path("users/<int:id>", userDetail, name="userDetails")
]