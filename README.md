# ASCII Art Generator

This simple Python script converts an image into ASCII art. It utilizes the `PIL` library to open and resize the image to a specified width while maintaining the aspect ratio.

## Usage

1. Make sure you have Python installed on your system.
   
2. Install the required library using:
   
pip install pillow

3. Replace `'imagen.jpg'` with the path to your desired image.

4. Adjust the `new_width` variable to your preferred width in pixels.

5. Fine-tune the `aspect_ratio` to control the output's aspect ratio.

6. Run the script to generate the ASCII art representation of the image.

## Customization

Feel free to modify the `ASCII_CHARS` variable with your own set of characters to achieve different visual effects.

```python
ASCII_CHARS = "@%#*+=-:. "
