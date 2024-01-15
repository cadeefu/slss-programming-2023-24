# Functions Practice
# Author: Cadee Fu
# 24 November 2023

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


# print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# Question 1 

def stars(num_of_stars: int) -> str:
    """Return the are of stars.
    
    Parans:

    num_stars - The numbers of stars to return
    """

    return "*" * num_of_stars

# print this function
print(stars(12))


# Questions 2

def biggest_of_three(num_one: int, num_two: int, num_three: int) -> int:
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else: 
        return num_three

print(biggest_of_three(2,3,40))

# Question 3

def pyramid_stars(user_response: int) -> int:
    for i in range(1, user_response+1):
        print("*" * i)

print(pyramid_stars(5))

# Question 4

def pyramid_mirror(USER_response: int) -> int:
    count = 1
    for x in range(USER_response, 0, -1):
        print(" " * x + "*" * count)
        count+=1

print(pyramid_mirror(5))


