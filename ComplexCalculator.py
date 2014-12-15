## areadi01 - ISD2014 CW4
#
# Difficulties with the problem:
#
# 1) splitting the string in the correct format so that it can be worked with properly.
# Take a string, split it into parts such that 'int1,int2 j' is returned as complex(int1,int2)
# separate out any other whole numbers complex(wholeNumber) so that it is returned in the form (n+0j)
# Perform calculation according to the operator(s) included in the string.  Return the value.
#
# 2) using try/except to raise the exceptions to print a message
#
# 3) working with the complex class but not having the 'imaj' part as a string
#
# 4) I though importing the 're' module would've been good for splitting the string,
#   but way beyond my understanding at present.


#functions for performing calculations
def add(firstNumber,secondNumber):
    return firstNumber+secondNumber

def subtract(firstNumber,secondNumber):
    return firstNumber-secondNumber

def multiply(firstNumber,secondNumber):
    return firstNumber*secondNumber

def divide(firstNumber,secondNumber):
    return float(firstNumber)/float(secondNumber)

#function for splitting the string
def calcInput(s):
    numbers = "0123456789."
    operators = []
    integers = []
    last_number = ""
    for value in s:
        if value in numbers:
            last_number += value
        else:
            if last_number:
                integers.append(last_number)
                last_number = ""
            if value:
                operators.append(value)
    if last_number:
        integers.append(last_number)
    return operators + integers

# function for evaluating user input
def evaluate(complexnumber, inputString):
    calc_val = 0
    stop = {'q','Q','quit'}
    clear = {'c','C','clear'}
    for char in inputString:
            if char in stop:
                raise EOFError ("Goodbye!")
            elif char in clear:
                calc_val = 0
            else:
                raise ValueError ("Error!")
                

# main function of program
def main():
    complexnumber = 3,4j
    print("Welcome to the complex calculator")
    while True:
        user1 = input("Please enter your input: ")
        evaluate (complexnumber, user1)
        new_calc = input("Would you like to know more? 'yes/no' ")
        if new_calc != "yes":
            print("Goodbye")
            break
        else:
            continue

main()        
