---
tags:
  - notes
  - natural-language-processing
  - 2023-24
  - programming-level-1-2
---

# Natural Language Processing

## Output
We can use a function to display text and symbols to the screen 
We use the `print()` function to display output

```python 
print("Your text goes in here.")
```

# Comments
Comments are pieces of text that are *not* interpreted by Python.
This means that the text is **ignored**. 
We use the # symbol to make our comments.

```python
# This is a comment
```

# Input
We grab information from the user using `input()`
When we run the function, it does two things:
1. it waits for the user to write something or nothing
2. The user presses **Enter/Return** to indicate that they're finished

```python
input()

input(<prompt>)    # prints out the prompt then waits
```

## Variables
Variables allow us to **store** information for the time that our app is running.

```python
favourite_food = input ("What is your favourite food? ")
```

`favourite_food` -> name of the variable
= -> assignment operator
`input...` -> value
## Naming
What you can do:
1. name them with letters, numbers, underscores
2. names **should** start with a lowercase letter
What you can't do:
1. you **can't** name them with spaces of symbols
2. you **cant **name them with certain names that are reserved
	1. e.g. if, while, for, and, or, ...

A good name is something like this:

```python
favourite_food
fave_food
date_of_birth
student_number
```

Bad names are like this:

```python
Favourite_food
a
num 
aa
aaa
aaaa
```
# [[Strings]]

# Format Strings
If we want to evaluate inside of a string, we use *f-strings*.

```python
fave_food = input ("What's your favourtie food?" )

print(f"Oooh, {fave_food}) sounds good!")
```

# String Methods

[[Methods]] are functions that we can use on [[objects]].

String methods allow us to modify strings. 

Say for example, we want to make all the characters of a string lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())
```


The `.lower()` method takes a string and converts all uppercase characters to lowercase.


# [[Modules]]

# [[Boolean]]

# [[Conditionals]]