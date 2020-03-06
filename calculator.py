#imports
import math
import cmath

#intro
print("Python Calculator")

#changelogs
def changelog():
    print("Changelogs: Version 1.3")
    print(" - Added absolute value")

def code():
    action = input("What do you want to do?\nOptions: Changelog, Calculate, Quit\n").lower()
    if action == "calculate":
        print("Available operations: addition (+), subtraction (-), multiplication (*), division (/), exponential (^), absolute value (|)")
        op = input("Enter an operator: ")
        if op != "|":
            if op == "^":
                yn = input("Only integers can be calculated using ^, are you sure you want to continue? Y or N: ").lower()
                if yn == "y":
                    num1 = int(input("Enter a number: "))
                    num2 = int(input("Enter a number: "))
                else:
                    code()
            else:
                num1 = float(input("Enter a number: "))
                num2 = float(input("Enter a number: "))
            num1_string = str(num1)
            num2_string = str(num2)
        else:
            num1 = float(input("Enter a number: "))
            num1_string = str(num1)
            num2_string = str(num1)

        if num1_string == "" or num2_string == "":
            print("One or both numbers are empty, please try again")
        else:
            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "/":
                print(num1 / num2)
            elif op == "^":
                print(num1 ^ num2)
            elif op == "|":
                print(abs(num1))
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

code()