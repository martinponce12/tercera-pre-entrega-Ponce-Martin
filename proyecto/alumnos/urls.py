from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("alta_alumno/<nombre>", views.alta_alumno)

]