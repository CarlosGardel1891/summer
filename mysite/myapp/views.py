from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable


# Create your views here.

def home(request):
    cursos = Curso.objects.all()

    return render(request, "gCursos.html", {"cursos": cursos})

def registrarCurso(request):
    nombre=request.POST['txtNombre']
    codigo=request.POST['txtCodigo']

    curso=Curso.objects.create(codigo= codigo, nombre= nombre)

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    nombre2=request.POST['txtNombre2']
    codigo2=request.POST['txtCodigo2']

    curso = Curso.objects.get(codigo=codigo2)
    curso.delete()
    curso=Curso.objects.create(codigo= codigo2, nombre= nombre2)

    return redirect('/')

def gEstudiante(request):

    estudiante = Estudiante.objects.all()
    return render(request, "gEstudiantes.html", {"estudiante": estudiante})

def registrarEstudiante(request):
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtCodigo']
    email=request.POST['txtEmail']

    estudiante2=Estudiante.objects.create(nombre= nombre, apellido=apellido, email=email)

    return redirect('/gEstudiante')

def eliminarEstudiante(request, email):
    estudiante2 = Estudiante.objects.get(email=email)
    estudiante2.delete()

    return redirect('/gEstudiante')

def edicionEstudiante(request, email):
    estudiante = Estudiante.objects.get(email=email)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

def editarEstudiante(request):
    
    nombre2=request.POST['txtNombre3']
    apellido2=request.POST['txtApellido3']
    email2=request.POST['txtEmail3']


    estudiante = Estudiante.objects.get(email=email2)
    estudiante.delete()

    estudiante=Estudiante.objects.create(nombre=nombre2, apellido=apellido2, email=email2)


    return redirect('/gEstudiante')





