# Winter Holidays
# Author: Cadee
# 8 Janurary 2024

# Requirements:
# - create a function called winter_holiday()
#   - takes one parameter
#   - returns a summary of an event from your holiday

# Please do not use ChatGPT or any LLM

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays
        the event is selected part
    """
        
    # Get events/ things that happened over the winter holiday
    good_events = [
    "I got a new backpack",
    "I spent time with my family" ,
    ]

    bad_events = [
    "I gained weight from the tasty dinners",
    "I hurt my finger at the gym"
    ]

    # If good_or_bad is "good" choose a random good event and return that
    if good_or_bad == "good":
       return random.choice(good_events)
    
    # If good_or_bad is "bad" choose a random bad event and return that
    if good_or_bad == "bad":
       return random.choice(bad_events)


def main() -> None:
    # Runs all the things we want to test in our .py file
    print (winter_holiday("good"))
    # "I got a Lego set for the first time in a long time"
    # "I went to Richmond Centre to walk around aimlessly."
    print (winter_holiday("bad"))
    # "I hoped to snowboard during the holiday and there was only rain."
    # "I asked for bidet for Christmas, instead I got a rando smart watch."

# If we're running THIS FILE using python
if __name__ == "__main__":
    main()