from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guitarlist", views.guitar_list, name="guitarlist"),
    path("guitarlist/<slug:slug>", views.guitar_details, name="details")
]