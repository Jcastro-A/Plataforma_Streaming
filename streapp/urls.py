from django.urls import path
from streapp import views
from streapp.views import inicio, peliculas, series, documentales, buscar, form_series, form_peliculas, form_documentales

urlpatterns = [
    
    path ('', views.inicio, name="inicio"), 
    
    # urls de Peliculas
    path ('peliculas/', views.peliculas, name="peliculas"), 
    path ('form_peliculas/', views.form_peliculas,  name="form_peliculas"), 
    
    # urls de Series
    path ('series/', views.series,  name="series"), 
    path ('form_series/', views.form_series,  name="form_series"), 
    
    # urls de Documentales
    path ('documentales/', views.documentales,  name="documentales"), 
    path ('form_documentales/', views.form_documentales,  name="form_documentales"), 
    
    # Otras urls
    path ('buscar/', views.buscar, name="buscar"), 
    
]