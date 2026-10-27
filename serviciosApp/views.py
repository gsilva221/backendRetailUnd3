import json
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render
from .models import Servicio, PrecioServicio

def cargar_datos():
    archivo = Path(__file__).resolve().parent / "datos.json"
    with open(archivo, "r", encoding="utf-8") as archivo_json:
        return json.load(archivo_json)

def servicios(request):
    servicios = Servicio.objects.values('nombre', 'descripcion', 'disponibilidad')  # Cargar los servicios desde la base de datos

    return render(request, 'servicioApp/servicios.html', {'servicios': servicios})


def precios(request):
    precios = PrecioServicio.objects.select_related('servicio')  # Cargar los precios desde la base de datos
    pagina = '''
    <h1>Precios</h1>
    <ul>
'''
    for precio in precios:
        pagina += f'''
        <li>{precio.servicio.nombre}: ${precio.precio} {precio.moneda}</li>
'''
    pagina += '''
    </ul>
    <a href="/">Volver al menú</a>
    '''

    return HttpResponse(pagina)
