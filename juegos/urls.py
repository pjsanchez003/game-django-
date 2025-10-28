# juegos/urls.py
from django.urls import path
from . import views

app_name = "juegos"  

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_juego, name='crear_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
]
