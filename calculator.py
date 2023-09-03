#!/bin/python3

#USER INPUT CALCULATOR

x = float(input("First number "))
o = input("Mathmatical Operator: ")
y = float(input("Second number: "))

if o == "+" or "plus":
	print(x + y)
elif o == "-" or "minus":
	print(x - y)
elif o == "/" or "divided by":
	print(x / y)
elif o == "*" or "times":
	print(x * y)
elif o == "**" or "^" or "to the power of":
	print(x ** y)
else:
	print("Unknown operator.")
