# Viope-Chap8-Exercise3-4:

import math
print("Calculator")
promptForNumbers = True


def given_number():
    while True:
        try:
            return int(input("Give a number: "))
        except ValueError:
            print("This input is invalid.")


def main():
    promptForNumbers = True
    while True:
        if promptForNumbers:
            given_number1 = int(given_number())
            given_number2 = int(given_number())
            promptForNumbers = False

        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2) \n(6)cos(number1/number2) \n(7)Change numbers \n(8)Quit")
        print(f"Current numbers: {given_number1}  {given_number2}")

        selection = float(input("Please select something (1-6): "))
        if selection == 1:
            print("The result is: ", given_number1 + given_number2)
        elif selection == 2:
            print("The result is: ", given_number1 - given_number2)
        elif selection == 3:
            print("The result is: ", given_number1 * given_number2)
        elif selection == 4:
            print("The result is: ", given_number1 / given_number2)
        elif selection == 5:
            print(f"The result is: {math.sin(given_number1/ given_number2)}")
        elif selection == 6:
            print(f"The result is: {math.cos(given_number1/ given_number2)}")
        elif selection == 8:
            print("Thank you!")
            break
        elif selection == 7:
            # Set prompt flag so that numbers will be requested upon next loop
            promptForNumbers = True


if __name__ == "__main__":
    main()
