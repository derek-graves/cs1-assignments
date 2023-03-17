"""
Student solutions should look almost identical to the one
below. The key realization is a ruler of size n is actually
just two rulers of size n - 1 surrounding a line of n marks.
Once students see that, the implementation should be fairly
straightforward.
"""

def recursiveRuler(n):
    # base case
    if n == 1:
        print("-")
    # recursive step
    else:
        recursiveRuler(n - 1)
        print(n * "-")
        recursiveRuler(n - 1)


def main():
    print("\n")
    size = int(input("What size ruler whould you like? "))
    print("\n")
    recursiveRuler(size)
    print("\n")

main()