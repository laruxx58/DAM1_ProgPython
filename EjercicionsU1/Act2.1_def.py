#Ejercico 2.1
#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def saludo(nom):
    return "Hola, " + nom


nom=str(input("Escribe tu nombre: "))
print (saludo(nom))
