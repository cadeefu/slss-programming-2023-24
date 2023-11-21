from pathlib import Path


# File Exercises
# Author:
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    # Print the second line
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        print(line.split(","))

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
    
        chicken_score = 0

        if "Chicken Adobo" in line:
            chicken_score += 1

        # print the current chicekn score
        print (f"The number of people who like Chicken Adobo as their favourite food is {chicken_score}")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

a_people = 0 

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:

        if "A" == line [0]:
            a_people += 1

        # Print how many people with first name "A"

print(f"The number of people who have the first letter of their first name start with the letter A is {a_people}")

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

guangzhou_people = 0 

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:

        if "Guangzhou" == line [0]:
            guangzhou_people += 1

        # Print how many people come from Guangzhou

print(f"The number of people come from Guangzhou is {guangzhou_people}")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

creditcard_user = 0

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:

        if int(line.split(",")[3])%2==0:
            creditcard_user += 1

        # Print how many people have an even credit card number

print(f"The number with an even credit card number are {creditcard_user}")

# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
