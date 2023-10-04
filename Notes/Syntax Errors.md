These types of errors are ones where you run your code and something breaks.

Syntax errors are relatively easy to fix.

Syntax errors happen when we don't follow the rules completely.

Some examples are when we forget a closing ". Or is we're missing a closing parenthesis

> Syntax <=> Rules
# Semantic Errors 

Semantic errors are much more challenging (in Ubials opinion) to squash.

Semantic errors are where your code doesn't "mean" what you actually mean.

```python
user_response = input("Do you like to eat food?")

if user_response.lower() == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What I (Mr. Ubial) mean is that if the user answers with ANYTHING affirmative the code should go into the "`yes`" block. 

One way to solve this problem is to use [[Strings#String Methods]]. We can use .lower() to catch all permutations of capital letters.
