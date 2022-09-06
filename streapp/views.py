from django.http import HttpResponse
from django.template import Template, Context, loader
from streapp.models import Peliculas, Series, Documentales
from django.shortcuts import render
from streapp.forms import PrimerFormulario, SeriesFormulario, DocumentalesFormulario

# Views de Inicio -------------------------------------------------------------------

def inicio(request):
    return render(request, "streapp/inicio.html")

# Views de Peliculas ----------------------------------------------------------------

def peliculas(request):
        listas = Peliculas.objects.all()
        return render(request, "streapp/peliculas.html", {"listas":listas})
    

def form_peliculas(request):
    if request.method == 'POST':
        forma = PrimerFormulario(request.POST)

        if forma.is_valid():
            data = forma.cleaned_data
            pelis = Peliculas(nombre=data['nombre'], genero=data['genero'], fecha=data['fecha'], aptoPara=data['aptoPara'])
            pelis.save()
            return render(request, "streapp/inicio.html")
    else:
        forma= PrimerFormulario()
    return render(request, "streapp/form_peliculas.html", {"form_peliculas": forma})

# Views de Series -------------------------------------------------------------------

def series(request):
        listas = Series.objects.all()
        return render(request, "streapp/series.html", {"listas":listas})
        

def form_series(request):
    if request.method == 'POST':
        forma = SeriesFormulario(request.POST)
        
        if forma.is_valid():
            data = forma.cleaned_data
            seri = Series(nombre=data['nombre'], genero=data['genero'], fecha=data['fecha'], aptoPara=data['aptoPara'])
            seri.save()
            return render(request, "streapp/inicio.html")
    else:
        forma= SeriesFormulario()
    return render(request, "streapp/form_series.html", {"form_series": forma})

# Views de Documentales -------------------------------------------------------------

def documentales(request):
        listas = Documentales.objects.all()
        return render(request, "streapp/documentales.html", {"listas":listas})
    
    
def form_documentales(request):
    if request.method == 'POST':
        forma = DocumentalesFormulario(request.POST)

        if forma.is_valid():
            data = forma.cleaned_data
            docu = Documentales(nombre=data['nombre'], genero=data['genero'], fecha=data['fecha'], aptoPara=data['aptoPara'])
            docu.save()
            return render(request, "streapp/inicio.html")
    else:
        forma= DocumentalesFormulario()
    return render(request, "streapp/form_documentales.html", {"form_documentales": forma})

# Otras Views  -----------------------------------------------------------------------


def buscar(request):
    return render(request, "streapp/buscar.html")

def buscador(request):
    if request.GET["pelicula"]:
        pelicula = request.GET["pelicula"]
        peliculas = Peliculas.objects.filter(pelicula__icontains=pelicula)
        return render(request, "streapp/peliculas.html",{"peliculas":peliculas})
    else:
        return render(request, "streapp/peliculas.html",{"peliculas":[]})
