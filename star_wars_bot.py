# Star Wars Bot
# Author: Cadee Fu
# October 16 2023

import time

# Introduce what the bot is doing
print("Hello, today I will decide if you can join the dark side 😈")
time.sleep(1)

# Ask if they like capes
cape_response = input("Do you like capes?")
time.sleep(1)

# Ask if they like red
red_response = input("Do you like red?")
time.sleep(1)

# Conclude the answer
if cape_response.lower().strip(",.?!") == "yes" or red_response.lower().strip(",.?!") == "yes":
    print("You belong to the dark side of the force.")
else: 
	print("I believe you are part of the light side")