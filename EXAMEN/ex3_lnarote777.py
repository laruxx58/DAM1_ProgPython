"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""

palabra=str(input("Intrduzca una palabra: "))


if len(palabra) == 8 :
    espacios=palabra.replace(" " , "")
    vocala=espacios.replace("a" , "@")
    vocale=vocala.replace("e" , "3")
    vocali=vocale.replace("i" , "1")
    encriptacion= "*"+ vocali + "#"
    print("Su palabra encriptada es: " , encriptacion )
elif len(palabra) < 8:
    user=str(input("Introduzca una palabra *mínimo 8 letras*: "))
    espacios=user.replace(" ", "")
    vocala=espacios.replace("a" , "@")
    vocale=vocala.replace("e" , "3")
    vocali=vocale.replace("i" , "1")
    encriptacion=vocali
    if len(user) == 8 :
        print( "*",encriptacion, "#")
    else:
        print(encriptacion)
else:
    espacios=palabra.replace(" ", "")
    vocala=espacios.replace("a" , "@")
    vocale=vocala.replace("e" , "3")
    vocali=vocale.replace("i" , "1")
    encriptacion=  vocali 
    print("Su palabra encriptada es: " , encriptacion )