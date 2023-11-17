# Similar Hobbies 
# Author: Cadee Fu
# November 14 2023

# Greet the user 
print("Hello!! I am a bot that will calculate your similarity score of hobbies between you and your friend.")

# Get their info
first_person_hobbies = input("Please enter 3 hobbies (seperate your spaces please!)").lower().split()

second_person_hobbies = input("Please enter 3 hobbies (seperate your spaces please!)").lower().split()

# Calculate similarity score
similarity_score = 0

for hobbie in first_person_hobbies:
    if hobbie in second_person_hobbies:
        similarity_score +=1

# Print results
print(f"You and your friend have a similarity score of: {similarity_score}")




