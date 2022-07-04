from django.urls import path
from . import views


urlpatterns = [

    path("", views.inicio, name="inicio"),
    path("inicio", views.inicio, name="inicio"),
    path("about", views.aboutUs, name="about"),
    path("cambios_ok", views.cambios_ok),
    path("vista_prs", views.vista_Productos, name ="vista_prs"),
    path("crv_info", views.crv_infoDetallada, name ="crv_info"),
    path("crv_info/<int:id>", views.crv_infoDetallada, name ="crv_info"),
    path("vno_info", views.vno_infoDetallada, name ="vno_info"),
    path("vno_info/<int:id>", views.vno_infoDetallada, name ="vno_info"),
    path("wky_info", views.wky_infoDetallada, name ="wky_info"),
    path("wky_info/<int:id>", views.wky_infoDetallada, name ="wky_info"),
    path("prs_lista", views.lista_productos, name = "prs_lista"),
    path("crv_lista", views.lista_cervezas, name = "crv_lista"),
    path("vno_lista", views.lista_vinos, name = "vno_lista"),
    path("wky_lista", views.lista_whiskys, name = "wky_lista"),
    path("crv_alta_form", views.crv_altaFormulario, name = "crv_alta"),
    path("vno_alta_form", views.vno_altaFormulario, name = "vno_alta"),
    path("wky_alta_form", views.wky_altaFormulario, name = "wky_alta"),
    path("prs_alta_form", views.prs_altaFormulario, name = "prs_alta"),
    path("crv_edit_form/<int:id>", views.crv_editarFormulario, name = "crv_edit_form"),
    path("crv_edit_form", views.crv_editarFormulario, name = "crv_edit_form"),
    path("vno_edit_form/<int:id>", views.vno_editarFormulario, name = "vno_edit_form"),    
    path("vno_edit_form", views.vno_editarFormulario, name = "vno_edit_form"),
    path("wky_edit_form/<int:id>", views.wky_editarFormulario, name = "wky_edit_form"),
    path("wky_edit_form", views.wky_editarFormulario, name = "wky_edit_form"),
    path("prs_edit_form/<int:id>", views.prs_editarFormulario, name = "prs_edit_form"),
    path("prs_edit_form", views.prs_editarFormulario, name = "prs_edit_form"),
    path("crv_elim_form/<int:id>", views.crv_eliminarFormulario, name = "crv_elim_form"),
    path("crv_elim_form", views.crv_eliminarFormulario, name = "crv_elim_form"),
    path("vno_elim_form/<int:id>", views.vno_eliminarFormulario, name = "vno_elim_form"),
    path("vno_elim_form", views.vno_eliminarFormulario, name = "vno_elim_form"),
    path("wky_elim_form/<int:id>", views.wky_eliminarFormulario, name = "wky_elim_form"),
    path("wky_elim_form", views.wky_eliminarFormulario, name = "wky_elim_form"),
    path("prs_elim_form/<int:id>", views.prs_eliminarFormulario, name = "prs_elim_form"),
    path("prs_elim_form", views.prs_eliminarFormulario, name = "prs_elim_form")


    



]