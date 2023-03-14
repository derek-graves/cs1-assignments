from random import randrange

chosenNumber = randrange(1,101)
print(chosenNumber)

# start game
print("I thought of a number between 1 and 100! Try to guess it.\n")
remainingGuesses = 5
lower = 1
upper = 100
win = False

# game loop
while remainingGuesses > 0:
    print("Range: [%d, %d]    Number of guesses left: %d" %(lower, upper, remainingGuesses))
    guess = int(input("Your guess: "))
    if guess == chosenNumber:
        win = True
        print("\n")
        break
    else:
        if guess > chosenNumber:
            messageEnd = "less than your guess."
            upper = guess - 1
        else:
            messageEnd = "greater than your guess."
            lower = guess + 1
        message = "My number is %s"%(messageEnd)
        print(message)
    
    remainingGuesses -= 1
    print("\n")

if win:
    print("Correct! You guessed my number in %d guesses. Well done!" %(5 - remainingGuesses + 1))
else:
    print("Out of guesses! You lose. My number was %d." %(chosenNumber))