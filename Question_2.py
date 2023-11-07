# Question 2
# Author: Cadee Fu
# 1 November 2023

# Create a list of questions 
questions = [
    "Judge 1",
    "Judge 2",
    "Judge 3",
    "Judge 4",
    "Judge 5",

]

final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)

    # Store their response
    rating = float(input().strip(",.?!"))
    final_score += rating

# Do some math - average
average_score = final_score/ len(questions)

# Present the response
print(f"Your Olympic score is: {average_score:.2f}/ 5")
