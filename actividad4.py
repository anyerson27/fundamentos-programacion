# Operaciones Básicas
def suma(numero1, numero2):
    resultado = float((numero1+numero2))
    print("la suma de los numeros es: ", resultado)


def resta(numero1, numero2):
    resultado = float((numero1-numero2))
    print("la resta de los numeros es: ", resultado)


def multiplicacion(numero1, numero2):
    resultado = float((numero1*numero2))
    print("la multiplicacion  de los numeros es: ", resultado)


def division(numero1, numero2):
    if numero2 <= 0:
        print("no se puede dividir por 0")
    else:
        resultado = float((numero1/numero2))
        print("la division de los numeros es: ", resultado)


numero1 = float((input(" digite el primer numero: ")))
numero2 = float((input(" digite el segundo numero: ")))
operacion = str(
    (input(" digite el simbolo de acuerdo a la operacion que desee(+,-,*,/): ")))


if operacion[0] == "+":
    suma(numero1, numero2)
elif operacion[0] == "-":
    resta(numero1, numero2)
elif operacion[0] == "*":
    multiplicacion(numero1, numero2)
elif operacion[0] == "/":
    division(numero1, numero2)
else:
    print("simbolo de operacion no valido ")
