# Tipos de Datos y funciones
# Anyerson Bolivar Zamora Varon
# 02 de junio del 2022

from os import system


def validaEdad(edad):
    if edad < 18:
        return "es menor de edad "
    else:
        return "es mayor de edad "

def pesoIdeal(peso, estatura):    
 # IMC= Peso (Kg) / Estatura  al cuadrado (Mt).
 # Si su IMC es inferior a 18.5, está dentro de los valores correspondientes a “delgadez o bajo peso".
 # Si su IMC es entre 18.5 y 24.9, está dentro de los valores "normales" o de peso saludable.
 # Si su IMC es entre 25.0 y 29.9, está dentro de los valores correspondientes a "sobrepeso".
 # Si su IMC es 30.0 o superior, está dentro de los valores de "obesidad".
    imc = peso/estatura**2
    if imc <= 18.5:
        return "bajo de peso"
    elif imc > 18.5 and imc <= 24.9:
        return "peso saludable"
    elif imc > 24.9 and imc <= 29.9:
        return "sobrepeso"
    else:
        return "obesidad "


print("DATOS PERSONALES")
#tienePesoIdeal=""
#esMayorEdad=""
nombre= str((input(" Ingresa tu nombre "))) 
documento= str((input(" Ingresa el tipo de documento ")))
numero= int((input(" Ingrese numero de documento ")))
sexo= str((input(" ¿cual es tu sexo ? ")))

while True:
    age = int(input("¿cual es su edad?: "))
    if age <= 0:
        print("digite edad valida ")
    else:
        esMayorEdad=validaEdad(age)
        break

while True:
  # el bebe mas pequeñ0 del mundo midio 0.23 metros= 23(cm)
    estatura = float((input(" ¿cual es tu estatura en metros? (ej:1.70): ")))
    peso = float(input("¿cual es tu peso en kg?: "))
    if estatura <= 0.23:
        print("coloque estatura valida")
    elif peso <= 6:
        print("coloque peso valido ")
    else:
        tienePesoIdeal=pesoIdeal(peso, estatura)
        break

system("cls")
print("RESUMEN DE DATOS \n ")
print("nombre: " , nombre)
print("tipo de documento: " , documento)
print("numero de documento: " , numero)
print("sexo: " , sexo[0].upper())
print("edad: " , age)
print("***" , esMayorEdad.upper(), "***" )
print("estatura: " , estatura)
print("peso: " , peso)
print("***" , tienePesoIdeal.upper(), "***" )
