
def mensaje1():
    print("mensaje")

def mensaje2():
    return input("dame un mensaje") 




def sumapositivos(num1 , num2):
    if num1<0 :
        num1 = 0
    if num2 <0 :
        num2=0
    return num1+num2

n1=int(input("Introduzca un numero: "))
n2=int(input("introduzca otro número:"))
print(sumapositivos(n1, n2))