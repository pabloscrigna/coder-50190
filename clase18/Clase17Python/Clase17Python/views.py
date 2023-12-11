from django.http import HttpResponse  # importamos la clase HttpResponse

from datetime import datetime

from django.template import Template, Context, loader


# creamos una respuesta http al usuario
def saludo(request):
    return HttpResponse("Hola Comisión 50190-Coder!!")


# usamos etiquetas HTML
def segunda_vista(request):
    return HttpResponse(
        '<progress value="75" max="100"></progress><br></br>Esta es mi segunda vista!!'
    )


# incluimos un parámetro que varía según la información asignada a la variable dia
def dia_de_hoy(request):
    dia = datetime.now()

    textoHtml = f"Hoy es: <br></br> {dia}"

    return HttpResponse(textoHtml)


# enviamos un parametro por url
def saludo_nombre(request, nombre):
    textoHtml = f"Hola, {nombre}!!"

    return HttpResponse(textoHtml)


# enviar mas de un parametro por url
def saludo_nombre_edad(request, nombre, edad):

    if edad < 18:
        texto_html = f"Sos menor de edad, tienes {edad} años"
    else:
        texto_html = f"Me llamo Pedro y tengo {edad} años"

    return HttpResponse(texto_html)


def vista_template(request):
    mi_html = open(
        "/home/pablo/Documents/Coderhouse/coder-50190/Clase17/Python-50190/Clase17Python/Clase17Python/templates/template1.html"
    )

    datos_contexto = {
        "nombre": "Pablo",
        "apellido": "Scrigna"
    }

    datos_contexto["curso"] = "Python 50190"
    datos_contexto["notas"] = [8, 8, 9, 7]
    datos_contexto["creado"] = datetime.now()

    print(f"datos_contexto: {datos_contexto}")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context(datos_contexto)

    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)


def vista_template_loader(request):

    mi_html = loader.get_template("template1.html")

    datos_contexto = {
        "nombre": "Pablo",
        "apellido": "Scrigna"
    }

    datos_contexto["curso"] = "Python 50190"
    datos_contexto["notas"] = [8, 8, 9, 7]
    datos_contexto["creado"] = datetime.now()

    documento = mi_html.render(datos_contexto)
    return HttpResponse(documento)