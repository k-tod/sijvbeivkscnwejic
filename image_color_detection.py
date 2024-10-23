
from PIL import Image

def image_contains_color(image_path, tolerance_percentage=5):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()  # Get pixel data using load() to access pixels by coordinates

    # Calculate the pixel tolerance for both width (x) and height (y) based on the percentage
    x_tolerance = int(width * (tolerance_percentage / 100))
    y_tolerance = int(height * (tolerance_percentage / 100))

    # Iterate over every pixel in the image, ignoring the edges defined by the identical percentage tolerance
    for y in range(y_tolerance, height - y_tolerance):
        for x in range(x_tolerance, width - x_tolerance):
            pixel = pixels[x, y]

            # Check if the pixel is neither black nor white
            if pixel != (0, 0, 0) and pixel != (255, 255, 255):
                # Return True with the coordinates of the pixel
                return True, x, y

    # If no non-black/white pixel is found, return False with (0, 0)
    return False, 0, 0
