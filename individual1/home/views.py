from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import *
import datetime
import locale

# Create your views here.
publicaciones=[
    {
        'autor':"Rodrigo",
        'titulo': "Publicacion 1",
        'contenido': "loremp ipsum",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Nicolas",
        'titulo': "Publicacion 2",
        'contenido': "loremp ipsum 2",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Adolfo",
        'titulo': "Publicacion 3",
        'contenido': "loremp ipsum 3",
        'fecha': "13 de julio del 2023"
    }
]

def bienvenida(request):
    contexto = {
        'publicaciones': publicaciones
    }
    return render(request,'home/index.html', contexto)

def logIn(request):
    locale.setlocale(locale.LC_TIME, 'es_ES')
    time= datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S').capitalize
    return render (request,'home/logIn.html',{'time':time})

def mostrarUsuario(request):
    lista_usuario = User.objects.all()
    return render(request, 'home/mostrar_usuario.html', {
        'lista_usuario' : lista_usuario
    })

def logOut(request):
    return render (request, 'home/logOut.html')

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            print(username)
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save()
            return redirect('blog-home')
        else:
            messages.error(request, "Hubo un error en el registro")
    formulario = RegistroUsuarioForm()
    return render(request, 'home/registro.html', {'formulario': formulario})