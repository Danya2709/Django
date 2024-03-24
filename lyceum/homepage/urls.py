from django.urls import path

from . import views

urlpatterns = [path("coffee/", views.cof), path("", views.home)]
