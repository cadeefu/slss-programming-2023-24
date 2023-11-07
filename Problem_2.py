# Problem 2
# Author: Cadee
# November 6 2023

# Create a list of questions 
questions = [
    "Have do you rate course 1 out of 5?",
    "Have do you rate course 2 out of 5?",
    "Have do you rate course 3 out of 5?",
    "Have do you rate course 4 out of 5?",
    "Have do you rate course 5 out of 5?",
    
]

final_count = 0

# Take the users answer and count it
for question in questions:
    print(question)

    # Store their response
    rating = float(input().strip(",.?!"))
    final_count += rating

    average_score = final_count / len(questions)


print(average_score)

# Seperate users answer accordingly
# if score is less than or equal to 1 <score>? Ouch
if average_score <= 1:
    print("Ouch.")
# or else if Score higher than 1 but less than 3: <score>? Not a bad semester
elif 1 < average_score < 3:
    print("Not a bad semester")

# or selse if Score of 3 or higher: <score>? Glad to hear that!
else:
    print(f"{average_score}? Glad to hear that!")



