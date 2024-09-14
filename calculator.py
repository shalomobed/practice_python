"""Name: Shalom Obed
Description of My Program: A python program that implements a terminal calculator,
accepting expressions as input and evaluates them using the specified operator. This program supports addition,
subtraction, multiplication, division, modulus, power, and floor division operation until a stop word is entered.
Example: 3 * 5 NOT 3*5
"""
import ast
import operator


# Imports the operator module to perform arithmetic operations.

def addition(left, right):
    return left + right


# Addition function that takes 2 arguments, left and right, and returns their sum

def subtract(left, right):
    return left - right


# Subtraction function that takes 2 arguments, left and right, and returns their difference

def multiplication(left, right):
    return left * right


# Multiplication function that takes 2 arguments, left and right, and returns their product

def division(left, right):
    if right == 0:
        raise ValueError("Division by zero is not allowed")
    return left / right


# Division function that takes 2 arguments, left and right, and returns their quotient
def modulus(left, right):
    return left % right


# Modulus function that takes 2 arguments, left and right, and returns their modulus

def power(left, right):
    return left ** right


# Power function that takes 2 arguments, left and right, and returns left raise to the power of right

def floor_division(left, right):
    return left // right


'''Floor division function that takes 2 arguments, left and right, and returns their quotient round **down** to the 
nearest integer
'''

print("Please enter an Expression")


def calculate_expression(expression):
    # Function that takes the inputted arithmetic expression and returns "left", "operator" and "right" values
    calculation = expression.split()
    left = ast.literal_eval(calculation[0])
    # ast.literal_eval allows both integer and input values
    operator = calculation[1]
    right = ast.literal_eval(calculation[2])
    # ast.literal_eval allows both integer and input values
    # "Left" is the first value, the "operator" is the 2nd value and the "right" is the 3rd value
    return left, operator, right


def calculate_operator(operator):
    # Function to calculate the operator function based on the inputted operator
    operator_dict = {"+": addition, "-": subtract, "*": multiplication,
                     "/": division, "%": modulus, "**": power,
                     "//": floor_division}
    return operator_dict[operator]


def main():
    # Main function
    stop_words = ["quit", "q", "Quit", "Q"]
    # Stop words to break the program
    while True:
        # Loop to keep executing expressions until stated otherwise
        expression = input(":> ")
        if expression.lower() in stop_words:
            # Check if expression is a stop word
            break
            # If it is, break the loop, then exit the program
        try:
            left, operator, right = calculate_expression(expression)
            # Calculate the left, operator, and right operands
            operator_function = calculate_operator(operator)
            # Calculate the operator function based on the operator
            answer = operator_function(left, right)
            # Calculate the result tof the expression
            print(f"Result: {left} {operator} {right} = {answer}")
            # Print the arithmetic result
        except IndexError:
            print(f"Error: Invalid Expression - ({expression})")
            # if the expression is invalid, print an error message then continue in the loop


# Run the main function if the script is run directly
if __name__ == "__main__":
    main()
