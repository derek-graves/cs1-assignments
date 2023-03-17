"""
Student work should look similar to the functions defined
below. The most important aspects are correct base cases,
correct recursion steps, and the organization of their
branching statements.
"""

# Part A
def tribonacci(n):
    # first base case
    if (n == 0 or n == 1 or n == 2):
       return 0
    # second base case
    elif n == 3: 
       return 1
    # recursive step
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Part B
def numDigits(n):
    # base case
    if n == 0: return 0
    # recursive step
    else:
      return 1 + numDigits(n // 10)
    

def main():
   print("\n")
   trib = int(input("Which Tribonacci number would you like to know? "))
   print(tribonacci(trib))
   print("\n")
   
   num = int(input("What's your favorite positive integer? "))
   print("Your favorite positive integer has %d digits." %(numDigits(num)))
   print("\n")


main()