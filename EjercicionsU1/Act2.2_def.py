#Ejercico 2.2
#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

def importe(a, b):
    return "Importe total: " + str(a*b)


a=int(input("Horas de trabajo: "))
b=int(input("Coste por horas: "))
print(importe(a, b))