from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
]
