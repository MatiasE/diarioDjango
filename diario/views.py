from django.shortcuts import render
from .models import Articulo
from django.utils import timezone

# Create your views here.
def pagina_inicio(request):
    articulos = Articulo.objects.all()
    return render(request, 'diario/pagina_inicio.html', {'articulos': articulos})