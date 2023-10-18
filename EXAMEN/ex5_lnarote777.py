"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio
    escribe "Introduzca los trabajados:"
    lee diastrabajados
    
    mientras dias < 0 entonces 
        escribe "*** Error - el valor no puede ser negativo ***"
        
    años= diastrabajados / 365
    diasrestantes= diastrabajados % 365
    meses= diasrestantes / 30
    dias = diasrestantes % 30
    
    si años == 1 :
        año="año"
    sino
        año="años"

    si dias == 1 :
        dia = "día"
    sino
        dia = "días"

    si meses = 1 entonces
        mes = "mes"
    sino
        mes= "meses"
    
    escribe "Ha cotizado " + años + año + ", " + meses + mes +" y " + dias + dia "." "
Fin
"""

diastrabajados=int(input("Introduzca los días trabajados: "))

while diastrabajados < 0 :
    print("*** Error - el valor no puede ser negativo***")
    
años= diastrabajados // 365
diasrestantes= diastrabajados % 365
meses= diasrestantes // 30
dias = diasrestantes % 30

if años == 1 :
    año="año"
else:
    año="años"

if dias == 1 :
    dia = "día"
else:
    dia = "días"

if meses == 1:
    mes = "mes"
else:
    mes= "meses"

print("Ha cotizado " , años , año , ", " , meses , mes ," y " , dias , dia , ".")