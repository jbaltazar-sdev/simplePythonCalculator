"""
Jeremy Baltazar - 01-14-2025

This is a simple calculator program that was built for fun.

It executes simple operations such as addition, multiplication,
division, subtraction, and finding the remainder.
"""

# ---------FUNCTIONS---------- #

def multiply(x,y):
    return x * y
    
def division(x,y):
    return x / y
    
def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def remainder(x,y):
    return x // y

# -------------------------------------- #

# Asks the user for two numbers.
first_input = float(input("Input a number >>> "))
second_input = float(input("Input another number >>> "))

# Then it will display a message showing the operators they can use.
print('''
(Choose the following math operator you wish to use for the two numbers):
    x = multiplication
    / = division
    + = addition
    - = substraction
    // = remainder
''')

# It will then ask you to input an operator.
math_op = input(">>> ")

# This is where the code decides what function to run by 
# what operator the user input.
if math_op == "x":
    mul_res = multiply(first_input, second_input)
    print(f"The two numbers multiplied become {mul_res}.")
elif math_op == "/":
    div_res = division(first_input, second_input)
    print(f"The two numbers divided become {div_res}.")
elif math_op == "+":
    add_res = addition(first_input, second_input)
    print(f"The two numbers added become {add_res}.")
elif math_op == "-":
    sub_res = subtraction(first_input, second_input)
    print(f"The two numbers subtracted become {sub_res}.")
elif math_op == "//":
    rem_res = remainder(first_input, second_input)
    print(f"The remainder of the two numbers is {rem_res}.")
else:
    print("I don't know what type of operator that is?")