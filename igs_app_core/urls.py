from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="igs_app_core_hello"),
]
