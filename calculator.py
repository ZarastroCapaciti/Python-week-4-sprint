# program -> basic calculator

import math # for square root and power of
# standard addition with two numbers
def add(x, y):
    return x + y

# standard subtraction between two numbers
def subtract(x, y):
    return x - y

# standard multiplication between two numbers
def multiply(x, y):
    return x * y

# standard division between two numbers
def divide(x, y):
    return x / y

# to the power of x^y
def power(x, y):
    return pow(x, y)

# square root of x
def square(x):
    return math.sqrt(x)

print("Select a number to to add")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power of")
print("6.Square Root")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", power(num1, num2))
    elif choice == '6':
        num1 = float(input("Enter the number you want the square root of: "))
        if num1 < 0:
            print("Please choose a positive number, as negatives can't go through a square root.")
            break
        print("√", num1, "=", square(num1))
    else:
        print("Invalid Input")
