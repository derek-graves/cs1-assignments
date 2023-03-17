from random import shuffle

def printIntro():
    print("\n")
    print("\n~~ Welcome to MEMORY GAME v0.1 ~~\n")
    print("Pick two cards at a time and see if they match.")
    print("Keep picking pairs of cards until you match them all!\n")

def printEqualsLine(num):
    equalsString = ""
    equalsString += num * "="
    print(equalsString)

def printBoard(board):
    for item in board:
        print(item.center(10), end="")
    print()

def getGuess(turnNumber, currentBoard):
    while True:
        print(f"Turn #{turnNumber}:")
        guess = input("card to flip> ")
        if guess.isdigit():
            guess = int(guess)
            if guess >= 0 and guess < len(currentBoard):
                if currentBoard[guess][0] == "=":
                    return guess
                else:
                    print("You've already matched that card.")
            else:
                print(f"Please guess a card from 0-{len(currentBoard) - 1}")
        else:
            print("Please guess an integer...")

def playRound(turnNum, currentBoard, answerBoard):
    print("\n")
    printEqualsLine(80)
    printBoard(currentBoard)

    guess1 = getGuess(turnNum, currentBoard)
    print(answerBoard[guess1].center(40))
    guess2 = getGuess(turnNum, currentBoard)
    while guess2 == guess1:
        print("...you cannot match a card with itself.")
        guess2 = getGuess(turnNum, len(currentBoard))
    print(answerBoard[guess2].center(40))

    if answerBoard[guess1] == answerBoard[guess2]:
        currentBoard[guess1] = answerBoard[guess1]
        currentBoard[guess2] = answerBoard[guess2]
        print("Correct!\n")
    else:
        print("Nope.\n")

    return currentBoard

def createGameboard(numCards):
    outputBoard = []
    for i in range(numCards):
        newItem = "===%d===" % (i)
        outputBoard.append(newItem)

    return outputBoard

def createAnswerKey(words):
    output = []
    for item in words:
        output.extend([item, item])

    return output

def outputResults(numCards, numTurns):
    if numTurns <= 5:
        performanceMessage = "Well done!\n"
    elif numTurns >= 10:
        performanceMessage = "You can do better.\n"
    else:
        performanceMessage = "Not bad.\n"

    print(f"You matched {numCards} cards in {numTurns} turns.")
    print(performanceMessage)
    print("\n")

def main():
    printIntro()
    wordList = ["finch", "robin", "raven", "egret", "heron"]
    answerKey = createAnswerKey(wordList)
    shuffle(answerKey)
    gameboard = createGameboard(len(answerKey))

    gameOver = False
    turnCounter = 0
    while not gameOver:
        turnCounter += 1
        gameboard = playRound(turnCounter, gameboard, answerKey)
        if gameboard == answerKey:
            printEqualsLine(80)
            printBoard(answerKey)
            print()
            gameOver = True
    outputResults(len(answerKey), turnCounter)

main()
