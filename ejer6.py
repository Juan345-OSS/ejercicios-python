# Ejemplo: Si una imagen tiene 1920 píxeles de ancho y 1080 de alto (\(1920\ 1080\)), el resultado simplificado es 16:9

#libreria para hacer el calculo
from PIL import Image

def get_aspect(path):
    img=  Image.open(path)
    width, height= img.size
    return width/height

print(f"Relacion decimal:{get_aspect('foto.jpeg')}")