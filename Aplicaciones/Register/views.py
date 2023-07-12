from django.shortcuts import render, redirect
from . models import Curso
# Create your views here.

def home(request):
    productosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": productosListados})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    cantidad=request.POST['txtCantidad']

    producto=Curso.objects.create(
        codigo=codigo, nombre =nombre, cantidad=cantidad)
    return redirect('/')