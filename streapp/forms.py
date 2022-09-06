from django import forms

class PrimerFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la película")
    genero = forms.CharField(label="Género")
    fecha = forms.DateField(label="Fecha(aaaa/mm/dd)")
    aptoPara = forms.IntegerField(label="Edad requerida")

class SeriesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la película")
    genero = forms.CharField(label="Género")
    fecha = forms.DateField(label="Fecha(aaaa/mm/dd)")
    aptoPara = forms.IntegerField(label="Edad requerida")

class DocumentalesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre de la película")
    genero = forms.CharField(label="Género")
    fecha = forms.DateField(label="Fecha(aaaa/mm/dd)")
    aptoPara = forms.IntegerField(label="Edad requerida")
