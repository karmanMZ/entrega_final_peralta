from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView
from . import views


urlpatterns = [
    
    path("login",views.login_request, name="login"),
    path("register",views.register, name="register"),
    path('logout', LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path("editarPerfil", views.editarPerfil , name="editarPerfil"),
    path("perfil", views.infoPerfil , name="perfil"),
    path("perfil/<int:id>", views.infoPerfil , name="perfil"),
    #path("", views. , name=""),
    



]
