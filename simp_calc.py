##
# Sample calculator program
# areadi01
#


##
# functions
#

def add(firstNumber,secondNumber):
    return firstNumber+secondNumber

def subtract(firstNumber,secondNumber):
    return firstNumber-secondNumber

def multiply(firstNumber,secondNumber):
    return firstNumber*secondNumber

def divide(firstNumber,secondNumber):
    return float(firstNumber)/float(secondNumber)

##
#program
#

def main():
    while True:
        firstNumber = int(input("Please enter the first number to be calculated: "))
        secondNumber = int(input("Please enter the second number to be calculated: "))
        operator = input("Please enter the action you wish to perform '+,-,/,*': ")
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print ("Sorry the calculation you have entered is not valid!")
            main()
        else:
            print("You wish to perform: ",firstNumber,operator,secondNumber)
            if operator == "+":
                print("The answer is: ",add(firstNumber,secondNumber))
            elif operator == "-":
                print("The answer is: ",subtract(firstNumber,secondNumber))
            elif operator == "*":
                print("The answer is: ",multiply(firstNumber,secondNumber))
            elif operator == "/":
                print("The answer is: ",divide(firstNumber,secondNumber))
        another_calc = input("Would you like to perform another calculation? yes/no? ")
        if another_calc != "yes":
            print("Goodbye!")
            break
        else:
            continue


main()

 
