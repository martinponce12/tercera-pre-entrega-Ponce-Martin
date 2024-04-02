from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("alta_profesor/<nombre>", views.alta_profesor)

]