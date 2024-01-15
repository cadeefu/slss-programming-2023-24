# SFu's best
# Cadee Fu
# November 10 , 2023

# Load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open that file
with open("data.csv") as f:
    # Read the first line of the data
    f.readline()
    print(f.readline())

# Create a "profile" fpr someone that shows their favourite places at SFU
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize our top similarity score and their name
top_sim_score = 0
top_sim_name = "" # place holder for name

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()
    # For every line of data in that file
    for line in f:
        # Convert the line of data into a list
        current_likes = line.split(",")

        # Initialize the CURRENT similairty score
        # Store the current person's name
        current_sim_score = 0
        current_name = current_likes[1]

        # For every item in our PROFILE
        for item in profile:
            if item in current_likes:

            # If that item is in the data's list
                current_sim_score +=1 
                # Increase the similiarity score by 1

        # print the current sim_score
        print (f"{current_name}-Score:{current_sim_score}")

        # If the current score is > top similiarity score
        if current_sim_score > top_sim_score:
            # Update the top similiarty score and name
            top_sim_score = current_sim_score
            top_sim_name = current_name

print("TOP SIMILAR PERSON!")
print(f"{top_sim_name}- Score: {top_sim_score}")

# Print lower similar score
# Initialize our top similarity score and their name
low_sim_score = 0
low_sim_name = "" # place holder for name

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()
    # For every line of data in that file
    for line in f:
        # Convert the line of data into a list
        current_likes = line.split(",")

        # Initialize the CURRENT similairty score
        # Store the current person's name
        current_sim_score = 0
        current_name = current_likes[1]

        # For every item in our PROFILE
        for item in profile:
            if item in current_likes:

            # If that item is in the data's list
                current_sim_score +=1 
                # Increase the similiarity score by 1

        # print the current sim_score
        print (f"{current_name}-Score:{current_sim_score}")

        # If the current score is > top similiarity score
        if current_sim_score < top_sim_score:
            # Update the top similiarty score and name
            low_sim_score = current_sim_score
            low_sim_name = current_name

print("LOWEST SIMILAR PERSON!")
print(f"{low_sim_name}- Score: {low_sim_score}")

