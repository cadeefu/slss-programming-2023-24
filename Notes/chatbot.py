# Chatbot
# Author: Cadee Fu
# Date: 20 September 2023

import random 
import time

# Greet the user
print("Hello there! 🤖")
time.sleep(1.5)
print ("I'm a crude Chatbot, here to talk to you.")
time.sleep(1.5) 

# Get the user's name and store it in a variable
user_name = input ("So... What's your name? ")

# Ask the user what their favourite food it 
print(f"It's good to meet you, {user_name}. ")
favourite_food = input ("Oh! I have a quick question... What's your favourite food? ")

# Make a comment about their favourite food but NOT BE OVERLY REPETITIVE
# Create a list of possible responses
list_of_food_responses = [
    f"Oh, I've never had {favourite_food} before.",
    "Mmmm. That sounds good!",
    "I heard that that is delicious.",
    "Cool."
 ]

# Choose one of those responses randomly
random_food_response = random.choice(list_of_food_responses)

# Print out that chosen response
print(random_food_response)



