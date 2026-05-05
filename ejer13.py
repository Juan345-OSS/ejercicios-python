#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

import re

class Ejercicio:
    def __init__(self,text):
        self.text = text

    def salida(self):
        resultado = re.sub(r'[^\w\s]', '', self.text).replace(" ", "").replace("_", "")
        a=resultado.lower()
        if a==a[::-1]:
            print(True)
        else:
            print(False)

juan= Ejercicio('Ana lleva al oso la avellana')
juan.salida()