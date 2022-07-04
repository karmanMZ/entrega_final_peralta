from django.shortcuts import render
from productos.models import *
from productos.forms import *
import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from usuarios.models import *

# Create your views here.

# prs_ Productos
# crv_ Cerveza
# vno_ Vino
# wky_ Whisky


##
# Vista de inicio
#path "" ; inicio

def inicio(request):
    return render(request, "inicio.html")

##
@login_required
def cambios_ok(request):
    return render(request, "cambios_ok.html")



def aboutUs(request):
    return render(request, "about.html")



##
# Vista lista de productos (cerveza, vino, whisky)
# path prs_lista

def lista_productos(request):
    productos = Productos.objects.all()
    info_productos = {"info_productos": productos}

    return render(request , "lista_productos.html" , info_productos)
##



##
# Vista lista de cervezas
# path crv_lista
def lista_cervezas(request):
    cervezas = Cerv_art.objects.all()
    info_cervezas = {"info_cervezas": cervezas}

    return render(request , "lista_cervezas.html" , info_cervezas)
##

 
##
# Vista lista de vinos
# path vno_lista
def lista_vinos(request):
    vinos = Vino.objects.all()
    info_vinos = {"info_vinos": vinos}

    return render(request , "lista_vinos.html" , info_vinos)
##






##
# Vista lista de whiskys
# path wky_lista
def lista_whiskys(request):
    whisky = Whisky.objects.all()
    info_whisky = {"info_whisky": whisky}

    return render(request , "lista_whisky.html" , info_whisky)
##






##
# Vista para generar altas de cervezas
# path crv_alta_form
# template para generar alta es crv_altaFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def crv_altaFormulario(request):
    if request.method == 'POST':

        cerv_art = Cerv_art(estilo = request.POST["estilo"], ibu = request.POST["ibu"], alcohol = request.POST["alcohol"], cuerpo= request.POST["cuerpo"], amargor= request.POST["amargor"], aroma = request.POST["aroma"], temp_consumo = request.POST["temp_consumo"])
        cerv_art.save()

        return render(request, "cambios_ok.html")
   
    return render(request, "crv_altaFormulario.html")
##







##
# Vista para generar altas de vinos
# path vno_alta_form
# template para generar alta es vno_altaFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def vno_altaFormulario(request):
    if request.method == 'POST':

        vino = Vino(color = request.POST["color"], estado = request.POST["estado"], envejecimiento = request.POST["envejecimiento"], calidad= request.POST["calidad"], azucar = request.POST["azucar"])
        vino.save()

        return render(request, "cambios_ok.html")
   
    return render(request, "vno_altaFormulario.html")
##







##
# Vista para generar altas de whiskys
# path wky_alta_form
# template para generar alta es wky_altaFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def wky_altaFormulario(request):
    if request.method == 'POST':

        whisky = Whisky(tipo = request.POST["tipo"], materia_prima = request.POST["materia_prima"], destilacion = request.POST["destilacion"], tipo_agua= request.POST["tipo_agua"], tiempo = request.POST["tiempo"])
        whisky.save()

        return render(request, "cambios_ok.html")
   
    return render(request, "wky_altaFormulario.html")
##




##
# Vista para generar altas de productos
# path prs_alta_form
# template para generar alta es prs_altaFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def prs_altaFormulario(request):
    if request.method == 'POST':

        productos = Productos(nombre_producto = request.POST["nombre_producto"], tipo_producto = request.POST["tipo_producto"], fecha_registro = request.POST["fecha_registro"])
        productos.save()

        return render(request, "cambios_ok.html")
   
    return render(request, "prs_altaFormulario.html")
##




##
# Vista para editar cervezas
# path crv_edit_form
# template para editar es crv_editFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def crv_editarFormulario(request, id):

    cerv_art = Cerv_art.objects.get(id=id)

    if request.method == "POST":
        
        formulario = Cerv_art_formulario( request.POST )

        if formulario.is_valid():
            datos = formulario.cleaned_data

            cerv_art.estilo = datos["estilo"]
            cerv_art.ibu = datos["ibu"]
            cerv_art.alcohol = datos["alcohol"]
            cerv_art.cuerpo = datos["cuerpo"]
            cerv_art.amargor = datos["amargor"]
            cerv_art.aroma = datos["aroma"]
            cerv_art.temp_consumo = datos["temp_consumo"]
            cerv_art.save()

            return render(request, "cambios_ok.html")
    else:
        formulario = Cerv_art_formulario(initial={'estilo': cerv_art.estilo , 'ibu': cerv_art.ibu ,'alcohol': cerv_art.alcohol ,'cuerpo': cerv_art.cuerpo ,'amargor': cerv_art.amargor ,'aroma': cerv_art.aroma ,'temp_consumo': cerv_art.temp_consumo})
    
    return render(request, "crv_editFormulario.html", {"formulario":formulario, "cerv_art":cerv_art})
##




##
# vista para editar vinos
# path vno_edit_form
# template para editar es vno_editFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def vno_editarFormulario(request, id):

    vino = Vino.objects.get(id=id)

    if request.method == "POST":
        formulario = Vino_formulario( request.POST )
        if formulario.is_valid():
            datos = formulario.cleaned_data

            vino.color = datos["color"]
            vino.estado = datos["estado"]
            vino.envejecimiento = datos["envejecimiento"]
            vino.calidad = datos["calidad"]
            vino.azucar = datos["azucar"]            
            vino.save()

            return render(request, "cambios_ok.html")
    else:
        formulario = Vino_formulario(initial={'color': vino.color ,'estado': vino.estado ,'envejecimiento': vino.envejecimiento ,'calidad': vino.calidad ,'azucar': vino.azucar})
    
    return render(request, "vno_editFormulario.html", {"formulario":formulario, "vino":vino})
##







##
# vista para editar whiskys
# path wky_edit_form
# template para editar es wky_editFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html

@login_required
def wky_editarFormulario(request, id):

    whisky = Whisky.objects.get(id=id)

    if request.method == "POST":
        
        formulario = Whisky_formulario( request.POST )
        
        if formulario.is_valid():
            
            datos = formulario.cleaned_data

            whisky.tipo = datos['tipo']
            whisky.materia_prima = datos['materia_prima']  
            whisky.destilacion = datos['destilacion'] 
            whisky.tipo_agua = datos['tipo_agua'] 
            whisky.tiempo = datos['tiempo']           
            whisky.save()

            whisky = Whisky.objects.all()
            return render(request, "cambios_ok.html")

        

            
    else:
        formulario = Whisky_formulario(initial={'tipo': whisky.tipo ,'materia_prima': whisky.materia_prima ,'destilacion': whisky.destilacion ,'tipo_agua': whisky.tipo_agua ,'tiempo': whisky.tiempo})
        
    return render(request, "wky_editFormulario.html", {"formulario":formulario , "whisky": whisky})
    
##




##
# vista para editar productos
# path prs_edit_form
# template para editar es prs_editFormulario.html
# template informativo sobre cambios realizados es cambios_ok.html


@login_required
def prs_editarFormulario(request, id):

    productos = Productos.objects.get(id=id)

    if request.method == "POST":
        formulario = Productos_formulario( request.POST )
        if formulario.is_valid():
            datos = formulario.cleaned_data

            productos.nombre_producto = datos["nombre_producto"]
            productos.tipo_producto = datos["tipo_producto"]
            productos.fecha_registro = datos["fecha_registro"]      
            productos.save()

            return render(request, "cambios_ok.html")
    else:
        formulario = Productos_formulario(initial={'nombre_producto': productos.nombre_producto ,'tipo_producto': productos.tipo_producto ,'fecha_registro': productos.fecha_registro})
    
    return render(request, "prs_editFormulario.html", {"formulario":formulario , "productos": productos})
##


##
# Vista para eliminar Cervezas
# path crv_elim_form

@login_required
def crv_eliminarFormulario(request, id):

    cerv_art = Cerv_art.objects.get(id=id) 
    cerv_art.delete()

    cerv_art = Cerv_art.objects.all()

    return render(request, "cambios_ok.html")
##



##
# Vista para eliminar Vinos
# path vno_elim_form


@login_required
def vno_eliminarFormulario(request, id):

    vino = Vino.objects.get(id=id) 
    vino.delete()

    vino = Vino.objects.all()

    return render(request, "cambios_ok.html")
##




##
# Vista para eliminar Whiskys
# path wky_elim_form


@login_required
def wky_eliminarFormulario( request , id):

    whisky = Whisky.objects.get(id=id) 
    whisky.delete()

    whisky = Whisky.objects.all()

    return render(request, "lista_whisky.html", {"whiskys":whisky})
##




##
# Vista para eliminar Productos
# path prs_elim_form


@login_required
def prs_eliminarFormulario(request, id):

    productos = Productos.objects.get(id=id) 
    productos.delete()

    productos = Productos.objects.all()

    return render(request, "cambios_ok.html")
##




##
# Vista para renderizar lista completa de productos
# path vista_prs

def vista_Productos(request):
    
    cervezas = Cerv_art.objects.all()    
    vinos = Vino.objects.all()   
    whiskys = Whisky.objects.all()
    info = {"info_cervezas": cervezas ,"info_vinos": vinos ,"info_whiskys": whiskys}
    
    return render(request, "vistas_productos.html", info)
#


##
# Vista para renderizar la lista detallada de las cervezas
# path crv_info

def crv_infoDetallada(request, id):

    cerv_art = Cerv_art.objects.get(id=id)
      
    
    info = {"estilo":cerv_art.estilo, "ibu":cerv_art.ibu,"alcohol":cerv_art.alcohol,"cuerpo":cerv_art.cuerpo,"amargor":cerv_art.amargor,"aroma":cerv_art.aroma,"temp_consumo":cerv_art.temp_consumo}
    return render(request, "crv_mas_info.html", info)



##
# Vista para renderizar la lista detallada de los vinos
# path vno_info
def vno_infoDetallada(request, id):

    vino = Vino.objects.get(id=id)
    
    info = {"color":vino.color ,"estado":vino.estado ,"envejecimiento":vino.envejecimiento ,"calidad":vino.calidad ,"azucar":vino.azucar }
    return render(request, "vno_mas_info.html", info)




##
# Vista para renderizar la lista detallada de los whiskys
# path wky_info
def wky_infoDetallada(request, id):

    whisky = Whisky.objects.get(id=id)
      
    
    info = {"tipo":whisky.tipo ,"materia_prima":whisky.materia_prima ,"destilacion":whisky.destilacion ,"tipo_agua": whisky.tipo_agua ,"tiempo": whisky.tiempo} 
    
    return render(request, "wky_mas_info.html", info)


