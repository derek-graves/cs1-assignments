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