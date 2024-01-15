# Colour Helper
# Author: Cadee Fu
# 13 December 2023

# Do you need help with colours?
# This is for you!

def pixel_to_string(pixel: tuple) -> str:
    """Take a rbg 3-tuple and "interpret it"
    as a colour and return that colour's names
    
    Params:
        pixel - 3-tuple of (red, green, blue)
        
    Return: 
        String representing the colour
    """
    r, g, b = pixel 

    if g > 170 and r < 78 and b < 70:
        return "green"
    # TODO: Implement detecting the colour red
    if g < 25 and b < 25 and r > 150:
        return "red"
    if g >= 80 and b < 55 and r < 55:
        return "jelly bean green"
    if g > 170 and b < 5 and r > 228:
        return "jelly bean yellow"
    if g < 70 and b < 69 and r > 230:
        return "red ball"
    
print(pixel_to_string((160,0,4)))
        
def is_light(pixel:tuple) -> bool:
    """ Take a pixel and if the average of the tuples values is greater than or equal to 
    128, it will return "True"

    Params:
        tuple named pixel - RGB values (red,green,blue)
    
    Return:
        a function that can output an answer true or false whether it is less than, equal to, 
        or greater than 128
    """
    r, g, b = pixel

    # add the values
    if ((r + g + b) / 3) >= 128:
        return True
    else:
        return False

black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128 ,128, 128)
white_pixel = (255, 255, 255)

print(is_light(black_pixel)) # False
print(is_light(dark_gray_pixel)) # False
print(is_light(light_gray_pixel)) # True
print(is_light(white_pixel)) # True
