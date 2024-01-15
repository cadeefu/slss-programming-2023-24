# Ball Warmup
# Author Cadee Fu
# Jan 12 2024

from PIL import Image

import colour_helper

RED_PIXEL = (150, 0, 0)

red_ball_img = Image.open("./Images/Red Ball.jpeg")

red_pixels = []

# Visit every pixel in the imade
for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        current_pixel = red_ball_img.getpixel((x,y))

        # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "red ball":
            red_pixels.append((x,y))

# Isolate red x pixels and find the minimum
smallest_x = 30000000

# For every pixel in "found" pixel list place a red pixel on that new image
for pixel_loc in red_pixels:
  pixel_loc[0] 
    # if the current x-loc is smaller than the smallest
  if pixel_loc[0] < smallest_x:
        # update the smallest x
      smallest_x = pixel_loc[0]

biggest_x = -1

# For every pixel in "found" pixel list place a red pixel on that new image
for pixel_loc in red_pixels:
  pixel_loc[0] 
    # if the current x-loc is smaller than the smallest
  if pixel_loc[0] > biggest_x:
        # update the biggest x
      biggest_x = pixel_loc[0]
    
# Calculate the middle of the red ball (x only)
print(f"X Ball Pixel: {(smallest_x)+(((biggest_x)-(smallest_x))/2)}")
                            
# Isolate red y pixels and find the maximum
smallest_y = 30000000

# For every pixel in "found" pixel list place a red pixel on that new image
for pixel_loc in red_pixels:
    # checking just the x locations
  pixel_loc[1] 
    # if the current x-loc is smaller than the smallest
  if pixel_loc[1] < smallest_y:
        # update the smallest y
      smallest_y = pixel_loc[1]
    
biggest_y = -1

# For every pixel in "found" pixel list place a red pixel on that new image
for pixel_loc in red_pixels:
    # checking just the x locations
  pixel_loc[1] 
    # if the current x-loc is smaller than the smallest
  if pixel_loc[1] > biggest_y:
        # update the biggest y
      biggest_y = pixel_loc[1]
    
# Calculate the middle of the red ball (y only)
print(f"Y Ball Pixel: {(smallest_y)+(((biggest_y)-(smallest_y))/2)}")

