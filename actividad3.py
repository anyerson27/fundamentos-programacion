# Cálculos con Figuras

import math


def areaCirculo(radio):
    circulo = float((radio**2)*math.pi)
    print("el area del circulo es: ", round(circulo, 3))


def areaTriangulo(base, altura):
    triangulo = float((base*altura) / 2)
    print("el area del triangulo es: ", triangulo)


def areaCuadrado(lado):
    cuadrado = float((lado*lado))
    print("el area del cuadrado es: ", cuadrado)

radio = float((input(" digite el radio del circulo para calcular el area: ")))
areaCirculo(radio)

base = float((input("digite la base del triangulo para calcular el area: ")))
altura = float(
    (input("digite la altura del triangulo para calcular el area: ")))
areaTriangulo(base, altura)

lado = float((input("digite el lado del cuadrado para calcular el area: ")))
areaCuadrado(lado)
