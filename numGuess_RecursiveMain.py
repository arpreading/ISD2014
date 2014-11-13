from random import randint

def playerGuess(num=1):
    playerGuess.count = num
    n = int(input("Please try to guess the number between 1-100: "))
    if n != main.guess:
        if n < main.guess:
            print("Too Low")
            playerGuess(num +1)
        elif n > main.guess:
            print("Too High")
            playerGuess(num +1)

def main(randValue = randint(1,100)):
    main.guess = randValue
    playerGuess()
    print("That's Correct!")
    print("The number was: ",main.guess)
    print("You made",playerGuess.count,"guesses")

main ()
