def letterFrequencyAnalyzer(string):
    LOWERCASE_ASCII_START = 97
    UPPERCASE_ASCII_START = 65
    # (1)
    frequencyList = []
    for i in range(26):
        frequencyList.append(0)

    for char in string:
        asciiCode = ord(char)
        # lower case
        if asciiCode >= 97 and asciiCode <= 122:
            frequencyList[asciiCode - LOWERCASE_ASCII_START] += 1
        # upper case
        elif asciiCode >= 65 and asciiCode <= 90:
            frequencyList[asciiCode - UPPERCASE_ASCII_START] += 1

    return frequencyList

def main():
    print(letterFrequencyAnalyzer(input("Please enter a string: ")))
    print(letterFrequencyAnalyzer(input("Please enter another string: ")))

main()

"""
(1) A list comprehension would be more succinct and more
    professional here, but they're not introduced until
    much later in the curriculum. Students could also hard 
    code the list with exactly 26 zeroes, but they should
    be encouraged to use the append method shown, as it
    makes the intended size of the list immediately clear.
"""
