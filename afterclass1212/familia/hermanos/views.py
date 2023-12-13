from django.http import HttpResponse
from django.template import loader

from hermanos.models import Hermano


def leer_hermanos(request):

    cursor = Hermano.objects.all()

    hermanos = {
        "hermanos": cursor,
        "titulo": "Hermanos template",
        "nota": "Informacion de hermanos"
    }

    plantilla = loader.get_template("hermanos.html")

    documento = plantilla.render(hermanos)
    
    return HttpResponse(documento)


def alta_hermano(request):
    return HttpResponse("En construccion")