# Author: Cadee Fu
# Dec 19 2023

import colour_helper

from PIL import Image
def is_light(pixel:tuple) -> bool:
    """ Take a pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    # calculate the average value of all three (red, green, blue)
    average = (red + green + blue) / 3
    # if the average >= 128 return True
    if average >= 128:
        return white_pixel
    # else return false
    else:
        return black_pixel
    
black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128 ,128, 128)
white_pixel = (255, 255, 255)

with Image.open("./Images/best_pizza.jpg") as im:
    # visit every pixel in the image
    image_height = im.height
    image_width = im.width
    # reads the image left-to-right, top-to-bottom
    # visits every pixel in the image
    for y in range(image_height):
        for x in range(image_width):
            # Get the current pixel information
            pixel = im.getpixel((x, y))
            # if the current pixel is light
                # put a white pixel in the same location
            if colour_helper.is_light(pixel):
                im.putpixel((x,y), white_pixel)
            # otherwise
            else: # put a black pixel in the same location
                im.putpixel((x,y), black_pixel)
    im.save("./Images/binarized.jpg")

