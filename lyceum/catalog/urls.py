from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "number")

urlpatterns = [
    path("", views.item_list),
    path("<int:pk>/", views.item_detail),
    re_path(r"^re/(?P<a>[1-9][0-9]*)/", views.item),
    path("converter/<number:numbers>/", views.number),
]
