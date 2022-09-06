from django.urls import path
from streapp import views
from streapp.views import inicio, peliculas, series, documentales, buscar, form_series

urlpatterns = [
    
    path ('', views.inicio, name="inicio"), #esta era nuestra primer view
    path ('peliculas/', views.peliculas, name="peliculas"), #esta era nuestra primer view
    path ('documentales/', views.documentales,  name="documentales"), #esta era nuestra primer view
    path ('buscar/', views.buscar, name="buscar"), #esta era nuestra primer view
    path ('series/', views.series,  name="series"), #esta era nuestra primer view
    path ('form_series/', views.form_series,  name="form_series"), #esta era nuestra primer view
    
]