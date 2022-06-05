# Operaciones Básicas

def factorial(numero):
    resultado=1
    for i in range(numero,0,-1):
        resultado=resultado*i
    print ("el factorial del numero ",numero, " es: ",resultado)


numero = int((input(" digite el numero para sacar el factorial: ")))
factorial(numero)