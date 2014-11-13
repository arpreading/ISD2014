from random import randint

guess = randint(1,100)
count = 1
playerGuess=int(input("Please try to guess the number between 1-100: "))

while playerGuess != guess:
    if playerGuess < guess:
        print("Too Low")
    elif playerGuess > guess:
        print("Too High")
    playerGuess=int(input("Please try to guess the number between 1-100: "))
    count += 1   

print("That's Correct!")
print("The number was:",guess, "You made",count,"guesses")
