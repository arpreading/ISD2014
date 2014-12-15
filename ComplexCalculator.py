## areadi01 - ISD2014 CW4
#
# My PsuedoCode interpretation of the problem:
#
# Take a string from the user,
# Split it into parts such that 'int1,int2 j' is returned as complex(int1,int2)
# Separate out any other whole numbers calculate as complex(wholeNumber) so that it is returned in the form (n+0j)
# Perform calculation according to the operator(s) included in the string.  Return the value. Repeat if prompted or exit
#
# Difficulties with the problem:
#
# 1) splitting the string in the correct format so that it can be worked with properly.
#
# 2) using try/except to raise the exceptions to print a message
#
# 3) working with the complex class but not having the 'imaj' part as a string
#
# 4) I though importing the 're' module would've been good for splitting the string,
#   but way beyond my understanding at present.


#functions for performing calculations (maybe would be placed in another function at a later date)
def add(firstNumber,secondNumber):
    return firstNumber+secondNumber

def subtract(firstNumber,secondNumber):
    return firstNumber-secondNumber

def multiply(firstNumber,secondNumber):
    return firstNumber*secondNumber

def divide(firstNumber,secondNumber):
    return float(firstNumber)/float(secondNumber)

#function for splitting the string (would be better to use split or re.split, as numbers and operators doesn't really help)
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

# function for evaluating user input as prompted by the problem set
def evaluate(complexnumber, inputString):
    calc_val = 0
    stop = {'q','Q','quit'}
    clear = {'c','C','clear'}
    for char in inputString: #needs to be try/except (print message), rather than 'hard' exceptions
            if char in stop:
                raise EOFError ("Goodbye!")
            elif char in clear:
                calc_val = 0
            #elif:     this should either be a call to the calculator function or process the input here
            else:
                raise ValueError ("Error!")
                

# main function of program
def main():
    complexnumber = 3,4j # would be good for this to get its value from the first complex number found in the user input
    print("Welcome to the complex calculator")
    while True:
        user1 = input("Please enter your input: ")
        evaluate (complexnumber, user1)# This is where the magic should happen.
        new_calc = input("Would you like to know more? 'yes/no' ")
        if new_calc != "yes":
            print("Goodbye")
            break
        else:
            continue

if __name__ == '__main__':
    main()
    
