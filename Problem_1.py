# Problem 1
# Author: Cadee
# November 3 2023

# Ask for the user's name
user_name = input ("What's your name?")


print(f"Hello,{user_name}! It's nice to meet you!")

# Ask if they have been to the countries
# Create a list of questions 
questions = [
    "Have you been to Asia?",
    "Have you been to Europe?",
    "Have you been to North America?",
    "Have you been to Australia?",
    "Have you been to Africa?",
    "Have you been to Antactica?",

]

final_count = 0

# Ask the questions to the user
for question in questions:

    # Capture their yes or no
 


    # If their answer is yes, increase final count
    if input(question).lower().strip(",.?!") == "yes":
        final_count += 1

# Present the response
print(f"I see, you've visited: {final_count}/ 7")

