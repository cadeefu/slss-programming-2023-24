# Question 3
# Author: Cadee
# November 3 2023

import time

# Ask if the user wants a burger for $5
burger_choice= input("Would you like a burger for $5 (Yes/No)")
burger_sum = input().strip(",.?1").lower()
time.sleep(1)

# Ask if the user wants fries for $3
fries_choice = input("Would you like fries for $3 (Yes/No)")
fries_sum =  input().strip(",.?1").lower()
time.sleep(1)

sum = 0
if burger_sum == "yes":
    sum += 5
if fries_sum == "yes":
    sum += 3

print("Your total would be " + str(sum * 1.14))
