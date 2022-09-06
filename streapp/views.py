from django.http import HttpResponse
from django.template import Template, Context, loader
from streapp.models import Peliculas, Series, Documentales
from django.shortcuts import render
from streapp.forms import PrimerFormulario, SeriesFormulario, DocumentalesFormulario

# Create your views here.
def inicio(request):
    return render(request, "streapp/inicio.html")


def peliculas(request):
    if request.method == 'POST':
        forma = PrimerFormulario(request.POST)

        if forma.is_valid():
            data = forma.cleaned_data
            pelis = Peliculas(nombre=data['nombre'], genero=data['genero'], fecha=data['fecha'], aptoPara=data['aptoPara'])
            pelis.save()
            return render(request, "streapp/inicio.html")
    else:
        forma= PrimerFormulario()
    return render(request, "streapp/peliculas.html", {"peliculas": forma})



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



def documentales(request):
    if request.method == 'POST':
        forma = DocumentalesFormulario(request.POST)

        if forma.is_valid():
            data = forma.cleaned_data
            docu = Documentales(nombre=data['nombre'], genero=data['genero'], fecha=data['fecha'], aptoPara=data['aptoPara'])
            docu.save()
            return render(request, "streapp/inicio.html")
    else:
        forma= DocumentalesFormulario()
    return render(request, "streapp/documentales.html", {"documentales": forma})

def buscar(request):
    return render(request, "streapp/buscar.html")

def buscador(request):
    if request.GET["pelicula"]:
        pelicula = request.GET["pelicula"]
        peliculas = Peliculas.objects.filter(pelicula__icontains=pelicula)
        return render(request, "streapp/peliculas.html",{"peliculas":peliculas})
    else:
        return render(request, "streapp/peliculas.html",{"peliculas":[]})
