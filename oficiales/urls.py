from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeOf, name='homeOf'),
    path('marcaOf/', views.marcaOf, name="marcaOf"),
    path('reportesOf/', views.reportesOf, name="reportesOf"),
    path('perfilOf/', views.perfilOf, name="perfilOf"),
    
    path('crearReporte/', views.crearReporte, name='crearReporte'),


    
]
