"""
A standard program for this assignment should accomplish
everything accomplished by the following code.
"""
userNum = int(input("Please enter a positive integer: "))

for i in range(1,userNum + 1):
  for j in range(1,userNum + 1):
    value = i * j
    numDigits = len(str(value)) # (1) more formally done by iteratively modding by 10
    numSpaces = 5 - numDigits # (2) see augmentation below for more adaptive version
    print(value, end=numSpaces*" ")
  print("\n")


"""
(1) A more formal version of this, which avoids converting
    the integer to a string, could look as follows from 
    within the nested for loop:

    value = i * j
    temp = value
    digits = 0
    while temp > 0:
      digits += 1
      temp = temp // 10
"""

"""
(2) A more adaptive version of this line of code would not
    assume a maximum of 4 digits, and would instead
    calculate that maximum before determining numSpaces:

    maxDigits = userNum * userNum # this should be placed prior to the for loops
    numSpaces = (maxDigits + 1) - numDigits
"""

"""
"""
