"""
In addition to the string and list challenges of this
assignment, sutdents must determine how best to decompose
their program into separate functions. How they go about
this is up to them, but they _must_ have at least three
separate functions, in addition to a main() function that
organizes/calls their other functions and takes user input.
Below is one example of how to do this.
"""

from random import randint

def printFormattedNumbers(numType, listOfNums):
  print(numType + ":   ", end = "")
  for i in range(len(listOfNums)):
    # maintain consistent spacing and stay on same line
    # until the last element in the list 
    if i == len(listOfNums) - 1:
      print(listOfNums[i])
    else:
      print(listOfNums[i], end = "  ")

def generateCipher(choices):
  outputCipher = []
  for i in range(0, 10):
    digit = randint(1,choices)
    outputCipher.append(digit)
  
  return outputCipher

def encryptPIN(pin, cipher):
  encrypted = ""
  for char in pin:
    char = int(char)
    encryptedChar = str(cipher[char])
    encrypted += encryptedChar

  return encrypted

def checkPIN(pin1, pin2):
  if pin1 == pin2:
    return True
  else:
    return False


def main():
  VALID_DIGITS = [0,1,2,3,4,5,6,7,8,9]
  TEST_PIN = "75309"

  cipher = generateCipher(3)
  printFormattedNumbers("PIN", VALID_DIGITS)
  printFormattedNumbers("NUM", cipher)
  encrypted = encryptPIN(TEST_PIN, cipher)

  enteredPIN = input("Please enter your PIN according to the cipher above.\n")
  correct = checkPIN(encrypted, enteredPIN)

  if correct:
    print("Correct! Access granted.")
  else:
    print("Incorrect. Access denied.")

main()