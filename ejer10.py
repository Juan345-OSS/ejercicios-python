# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

import morse_talk as mt 

texto=str(input('Ingrese su mensaje: '))

codigo = mt.encode(texto)
print(f'el codigo de su mensaje es {codigo}')

rever=mt.decode(codigo)
print(f'El codigo es:- {rever}')