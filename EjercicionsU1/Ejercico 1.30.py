# Ejercico 1.30

#Inicio
#   escribe ("Dame un numero:")
#   escribe ("Cuanto se incrementa: ")
#   escribe ("¿Total de la serie? ")
#   lee num, incremento, serie
#   mientras num<0 and incremento<0 :
#       escribe (" Vuelva a introducir el incremento ")
#       escribe(" vuelva a introducir el total de la serie ")
#   para i en (0...serie) hacer
#       num += incremento
#       escribe (" SERIE =>  " , num)
#Fin



num=int(input("Dame un número: "))
incremento=int(input("Dame un incremento: "))
serie=int(input("¿Hata qué numero dura la serie? "))
while incremento<0 and serie<0 :
    print("Vuelve a introducir el incremento (mayor que 0): ")
    print("Vuelve a introducir el numero de la serie (mayor que 0): ")
for i in range(num,serie,incremento) :
    print("SERIE =>", i)
