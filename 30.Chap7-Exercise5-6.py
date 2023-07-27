# Viope-Chap7-Exercise5-6:

import math
print("Calculator")

promptForNumbers = True

while True:
    if promptForNumbers:
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))

        promptForNumbers = False

    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2) \n(6)cos(number1/number2) \n(7)Change numbers \n(8)Quit")
    print(f"Current numbers: {first_number} {second_number}")
    selection = float(input("Please select something (1-6): "))

    if selection == 1:
        print(f"The result is: {first_number + second_number}")
    elif selection == 2:
        print(f"The result is: {first_number - second_number}")
    elif selection == 3:
        print(f"The result is: {first_number * second_number}")
    elif selection == 4:
        print(f"The result is: {first_number / second_number}")
    elif selection == 5:
        print(f"The result is: {math.sin(first_number / second_number)}")
    elif selection == 6:
        print(f"The result is: {math.cos(first_number / second_number)}")
    elif selection == 8:
        print("Thank you!")
        break
    elif selection == 7:
        # Set prompt flag so that numbers will be requested upon next loop
        promptForNumbers = True
    else:
        print("Selection was not correct")
