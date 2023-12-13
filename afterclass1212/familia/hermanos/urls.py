from django.urls import path

from hermanos.views import leer_hermanos, alta_hermano

urlpatterns = [
    path("leer", leer_hermanos),
    path("alta", alta_hermano),
]