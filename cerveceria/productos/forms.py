from django import forms





class Productos_formulario(forms.Form):
    nombre_producto = forms.CharField(max_length=40)
    tipo_producto = forms.CharField(max_length=40)
    fecha_registro = forms.DateField()

class Cerv_art_formulario(forms.Form):
	estilo = forms.CharField(max_length=40)
	ibu = forms.IntegerField() 
	alcohol = forms.IntegerField() 
	cuerpo = forms.CharField(max_length=40)
	amargor = forms.CharField(max_length=40)
	aroma = forms.CharField(max_length=40)
	temp_consumo = forms.IntegerField() 

class Vino_formulario(forms.Form):	
	color = forms.CharField(max_length=40)
	estado = forms.CharField(max_length=40)
	envejecimiento = forms.IntegerField() 
	calidad = forms.CharField(max_length=40)
	azucar = forms.IntegerField() 


class Whisky_formulario(forms.Form):
	tipo = forms.CharField(max_length=40)
	materia_prima = forms.CharField(max_length=40)
	destilacion = forms.CharField(max_length=40)
	tipo_agua = forms.CharField(max_length=40)
	tiempo = forms.IntegerField() 