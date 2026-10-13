import json
from pathlib import Path
from django.shortcuts import redirect, render
from django.http import HttpResponse

from serviciosApp.forms import PrecioServicioCrearForm, ServicioForm
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
    form_servicio = ServicioForm(request.POST or None)
    form_precio = PrecioServicioCrearForm(request.POST or None)
    if request.method == 'POST':
        if form_servicio.is_valid() and form_precio.is_valid():
            servicio = form_servicio.save()
            precio = form_precio.save(commit=False)
            precio.servicio = servicio
            precio.save()
            return redirect('/servicios/')
    return render(request, 'serviciosApp/crear.html', {
        'form_servicio': form_servicio,
        'form_precio': form_precio
    })
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