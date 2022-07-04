from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuarios.forms import UserEditForm
from usuarios.models import *


# Create your views here.

## Vsita para iniciar sesion
# path login

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)

                return render(request, "padre.html", {"url":avatares[0].imagen.url})
            else:
                return render(request, "pfl_inicio_fail.html")
        else:
            return render(request, "pfl_inicio_fail.html")

    

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})



def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, "pfl_creado_ok.html")


    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            
            info = mi_formulario.cleaned_data

            usuario.email = info['email']
            password = info['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request, "pfl_edit_ok.html")

    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editar_perfil.html", {"mi_formulario":mi_formulario, "usuario":usuario})
    


@login_required
def infoPerfil(request):    
    return render(request, "info_usuario.html")



