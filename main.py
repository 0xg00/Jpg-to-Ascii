from PIL import Image

image = Image.open('imagen.jpg')

new_width = 50  # Cambia esto al ancho deseado en píxeles
aspect_ratio = 0.4  # Cambia esto para ajustar la relación de aspecto
new_height = int(new_width * aspect_ratio)
image = image.resize((new_width, new_height))

ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(pixel):
    grayscale_value = pixel[0]
    ascii_index = (grayscale_value * 9) // 255
    return ASCII_CHARS[ascii_index]

def image_to_ascii(image):
    width, height = image.size
    ascii_image = ""
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            ascii_image += pixel_to_ascii(pixel)
        ascii_image += "\n"
    return ascii_image

ascii_art = image_to_ascii(image)

print(ascii_art)
