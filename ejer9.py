# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */



num= float(input('Ingrese Numero: '))

a= num % 2

b= round(a)

if b == 0:
    print(True)
else:
    print(False)