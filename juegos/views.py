from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm

def index(request):
    juegos = Juego.objects.all()

    # Crear nuevo juego desde la misma página
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JuegoForm()

    return render(request, 'juegos/index.html', {'juegos': juegos, 'form': form})


def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/editar_juegos.html', {'form': form})


def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    return redirect('index')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm

def index(request):
    juegos = Juego.objects.all()

    # Crear nuevo juego desde la misma página
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('juegos:index')  # Asegúrate de usar el namespace correcto
    else:
        form = JuegoForm()

    return render(request, 'juegos/index.html', {'juegos': juegos, 'form': form})


def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('juegos:index')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/editar_juegos.html', {'form': form})


def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    return redirect('juegos:index')

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JuegoForm()

    return render(request, 'juegos/crear_juego.html', {'form': form})
