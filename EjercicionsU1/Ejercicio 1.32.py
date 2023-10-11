#Ejercicio 1.32

#Inicio

#	Escribe "Introduce un número: "
#	Lee x
#	Escribe "Introduce otro: "
#	Lee y

#	Si (x >= y) entonces
#		numIni = x - 1
#		numFin = y
#	Sino
#		numIni = y - 1
#		numFin = x
		
#	Para i en (numIni...numFin) hacer
#		Escribe i + 
#		Si (numIni != numFin) entonces
#			Escribe "-"

#Fin


num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro: "))
if num1 >= num2 :
    numIni= num1 - 1 
    numFin = num2
else:
    numIni = num2 - 1 
    numFin = num1 
for i in range(numFin, numFin) :
    print(i)
    if numIni != numFin :
        print("-")