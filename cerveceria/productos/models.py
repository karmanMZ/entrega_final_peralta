from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre_producto = models.CharField(max_length=40)
    tipo_producto = models.CharField(max_length=40)
    fecha_registro = models.DateField()
    def __str__(self):
        return f"Nombre: {self.nombre_producto} -- Tipo: {self.tipo_producto} -- Registro: {self.fecha_registro}"
     
    

class Cerv_art(models.Model):
    estilo = models.CharField(max_length=40)
    ibu = models.IntegerField() 
    alcohol = models.IntegerField() 
    cuerpo = models.CharField(max_length=40)
    amargor = models.CharField(max_length=40)
    aroma = models.CharField(max_length=40)
    temp_consumo = models.IntegerField() 
    def __str__(self):
        return f"Estilo: {self.estilo} -- Ibu: {self.ibu}-- Alcohol: {self.alcohol}-- Cuerpo: {self.cuerpo}-- Amargor: {self.amargor} -- Aroma: {self.aroma} -- Temperatura de consumo: {self.temp_consumo}"

class Vino(models.Model):	
    color = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    envejecimiento = models.IntegerField() 
    calidad = models.CharField(max_length=40)
    azucar = models.IntegerField() 
    def __str__(self):
        return f"Color: {self.color} -- Estado: {self.estado} -- Envejecimiento: {self.envejecimiento} -- Calidad: {self.calidad} -- Azucar: {self.azucar}"


class Whisky(models.Model):
    tipo = models.CharField(max_length=40)
    materia_prima = models.CharField(max_length=40)
    destilacion = models.CharField(max_length=40)
    tipo_agua = models.CharField(max_length=40)
    tiempo = models.IntegerField() 
    def __str__(self):
        return f"Tipo: {self.tipo} -- Materia prima: {self.materia_prima} -- Destilacion: {self.destilacion} --Tipo de agua: {self.tipo_agua} --Tiempo: {self.tiempo}"