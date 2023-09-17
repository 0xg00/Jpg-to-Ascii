from PIL import Image

# Abre la imagen
image = Image.open('imagen.jpg')

# Escala la imagen a un nuevo tamaño (ancho, alto)
new_width = 50  # Cambia esto al ancho deseado en píxeles
aspect_ratio = 0.4  # Cambia esto para ajustar la relación de aspecto
new_height = int(new_width * aspect_ratio)
image = image.resize((new_width, new_height))

# Define los caracteres que se utilizarán para crear el arte ASCII, de más oscuro a más claro
ASCII_CHARS = "@%#*+=-:. "

# Función para convertir un píxel en un carácter ASCII
def pixel_to_ascii(pixel):
    grayscale_value = pixel[0]
    ascii_index = (grayscale_value * 9) // 255
    return ASCII_CHARS[ascii_index]

# Función para convertir la imagen completa en arte ASCII
def image_to_ascii(image):
    width, height = image.size
    ascii_image = ""
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            ascii_image += pixel_to_ascii(pixel)
        ascii_image += "\n"  # Nueva línea al final de cada fila
    return ascii_image

# Convierte la imagen a arte ASCII
ascii_art = image_to_ascii(image)

# Imprime el arte ASCII en la consola
print(ascii_art)
