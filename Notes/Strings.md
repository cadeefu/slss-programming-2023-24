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

We can use string methods to help solve[[Syntax Errors#Semantic Errors[semantic errors]]] 
# .lower()

The `.lower()` method takes a string and converts all uppercase characters to lowercase.

## .upper() 

The .upper() method uppercases all the le

## .strip() 

The .strip() method removes characters from both the the beginning and the end of the string.

```python  
user_feeling = input ("How are you feeling today?")

if user_feeling.lower().strip(",.?! ") == "good":  
	print("That's great!")  
```

## .split(str)

The .split(str) method splits a string into a list, separating the string based on the character you give it.

```python  
grocery_list = "eggs milk cheese hotwheels"grocery_list = grocery_str.splt(" ")0  
```
