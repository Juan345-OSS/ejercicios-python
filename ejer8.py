# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */


palabra = input('Ingrese palabra: ').lower()
letras_vistas = ""

for letra in palabra:
    if letra not in letras_vistas:
        conteo = palabra.count(letra)
        print(f'La letra "{letra}" se repite {conteo} veces.')
        letras_vistas += letra