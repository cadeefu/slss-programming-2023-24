# Chip Rater
# Author: Cadee
# 1 November 2023

# Interview people about their perception of how delcious chips are based on a set of questions
# In the end, we'll give an aggregate score
 
# Greet the user
print("Please answer the following questions based on the chip you just ate")

# Create a list of questions 
questions = [
    "How crispy is the chip on a scale to 1 to 5? 5 is very crispy. 1 is very mushy",
    "How would you rate the taste from 1 to 5? 5 is the best taste ever. 1 is I would rather eat dirt.",
    "From 1 to 5, how would you rate the packaging? 5 is I would just pay for the packaging. 1 is someone got paid to do thi??"

]

final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)

    # Store their response
    rating = int(input().strip(",.?!"))
    final_score += rating

# Do some math - average
average_score = final_score/ len(questions)

# Present the response
print(f"The average score of this chip is: {average_score:.2f}/ 5")
