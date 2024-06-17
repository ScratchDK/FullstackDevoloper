from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_client, name="create"),
    path('', views.show_clients),
    path('<int:pk>/update', views.UpdateClient.as_view(), name="update")
]
