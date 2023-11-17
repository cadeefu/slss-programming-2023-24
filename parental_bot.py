# Parental Bot
# Author: Cadee Fu
# November 17 2023

# Greet the user
print("Hello! I am your parental bot and I will be checking in on you to see if you need help. Please answer my questions truthfully.")

# Ask questions
score = 0

questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
]

# Get score
for question in questions:
    print (question)

    answer = input().lower().strip("?,.!")

    if answer == "yes":
        score +=1

if score == 0:
        print("I'm coming over.")
elif score <=2:
        print("Ok.")
elif score >=3:
        print("Good.")
