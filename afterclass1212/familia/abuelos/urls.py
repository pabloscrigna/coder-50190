from django.urls import path

from abuelos.views import leer_abuelos, alta_abuelo

urlpatterns = [
    path("leer", leer_abuelos),
    path("alta", alta_abuelo),
]