import json
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from .models import PrecioServicio, Servicio

def servicios(request):
    #Usando BD (ORM:Object-Relational Mapping)
    datos = Servicio.objects.all()

    return render(request, "serviciosApp/listar.html", {
        "servicios": datos
    })

def login_servicios(request):
    return render(request, "serviciosApp/login.html")
# PRECIOS

def servicio_crear(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        disponibilidad = request.POST.get("disponibilidad")

        # Crear un nuevo objeto Servicio y guardarlo en la base de datos
        servicio = Servicio(nombre=nombre, descripcion=descripcion, disponibilidad=disponibilidad)
        servicio.save()

        return HttpResponse(f"Servicio '{servicio.nombre}' creado exitosamente.")

    return render(request, "serviciosApp/crear.html")
def precios(request):
    datos = PrecioServicio.objects.all()

    return render(request, "serviciosApp/precios.html", {
        "precios": datos
    })

"""
#PRECIOS
def precios(request):
    precios = PrecioServicio.objects.all()

    pagina = '''
    <h1>Precios de nuestros servicios</h1>
    <ul>
    '''

    for precio in precios:
        pagina += f'''
            <li>
                <h2>{precio.servicio.nombre}</h2>

                <p>
                    <strong>Precio:</strong>
                    ${precio.precio} {precio.moneda}
                </p>

                <p>
                    <strong>Descuento:</strong>
                    {precio.descuento}%
                </p>

                <p>
                    <strong>Observación:</strong>
                    {precio.observacion}
                </p>
            </li>
            <hr>
        '''

    pagina += '''
    </ul>

    <img src="/static/images/gif/precios.gif"
         alt="Error en la carga de la imagen"
         width="100">

    <br>
    <a href="/">Volver al menú</a>
    '''
    return HttpResponse(pagina)
"""