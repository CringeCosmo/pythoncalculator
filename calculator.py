#imports
import math
import cmath

#intro
print("Python Calculator.")

#changelogs
def changelog():
    print("Changelogs: Version 1.5.1")
    print(" - Added factorial.")
    print(" - Major bug fixes")
    print("   - Fixed exponential errors (used incorrect operator)")
    print("   - Removed unnecessary code.")
    print("   - Removed the integer limit on exponents, floats now allowed.")
    print(" - 1.5.1 fix: instructions did not show factorial option."


def factorial(x):
    fac = x
    factotal = 1
    while fac != 0:
        factotal = factotal * fac
        fac -= 1
    return factotal

def code():
    action = input("What do you want to do?\nOptions: Changelog, Calculate, Quit\n").lower()
    if action == "calculate":
        print("Available operations: add (+), subtract (-), multiply (*), divide (/), exponent (^), absolute value (|), greater than (>), less than (<), factorial (!)")
        op = input("Enter an operator: ")
        if op != "|" and op != "!":
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a number: "))
        else:
            num1 = float(input("Enter a number: "))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "^":
            print(num1 ** num2)
        elif op == "|":
            print(abs(num1))
        elif op == ">":
            if num1 > num2:
                print(num1)
            elif num2 > num1:
                print(num2)
            elif num1 == num2:
                print(num1_string + " = " + num2_string)
        elif op == "<":
            if num1 < num2:
                print(num1)
            elif num2 < num1:
                print(num2)
            elif num1 == num2:
                print(num1_string + " = " + num2_string)
        elif op == "!":
            print(factorial(num1))
        else:
            print("No proper operator found, please try again")
    elif action == "changelog":
        changelog()
    elif action == "quit":
        print("Goodbye")
        quit()
    else:
        print("No proper input found, please try again.")
    code()

#run
code()