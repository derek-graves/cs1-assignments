"""
Though there are many different ways to accomplish te task
of this assignment, student work should generally look as
follows.
"""

from random import randrange

chosenNumber = randrange(1,101)

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
            upper = guess - 1 # (1)
        # already checked > and ==, so < is the only remaining case
        else:
            messageEnd = "greater than your guess."
            lower = guess + 1 # (1)
        message = "My number is %s"%(messageEnd)
        print(message)
    
    remainingGuesses -= 1
    print("\n")

if win:
    print("Correct! You guessed my number in %d guesses. Well done!" %(5 - remainingGuesses + 1))
else:
    print("Out of guesses! You lose. My number was %d." %(chosenNumber))


"""
(1) As written, this code changes the bounds regardless of
    whether the guess was inside them. It's
    possible, for example, for the player to go from [1,49]
    to [1,76]. To prevent this behavior, students could
    check whether the guess is within the bounds, and only
    update the bounds if so.

    More ambitious students could 'force' the user to enter
    a number within the bounds by using a while loop, only
    proceeding once a desired number is found.
"""