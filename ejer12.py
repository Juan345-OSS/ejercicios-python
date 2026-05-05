#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
class Texto:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def salida(self):
        out1 = ""
        for letra in self.text1:
            if letra not in self.text2:
                out1 += letra

        out2 = ""
        for letra in self.text2:
            if letra not in self.text1:
                out2 += letra

        print(f"out1: {out1}")
        print(f"out2: {out2}")

pepe = Texto('juan', 'jwwwan')
pepe.salida()
