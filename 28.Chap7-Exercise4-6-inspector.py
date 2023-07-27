# Viope-Chap7-Exercise3-6:
# This is the answer.
# Just put the code below 👇 into Viope's answering box.

def testme(userinput):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    val = True

    if len(userinput) < 6:
        val = False
    if not any(char in letters for char in userinput):
        val = False
    if not any(char in numbers for char in userinput):
        val = False
    if val:
        return val
