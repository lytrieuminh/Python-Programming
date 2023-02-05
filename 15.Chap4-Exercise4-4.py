#Viope-Chap4-Exercise4-4:

print("Calculator")

# Flag to indicate whether user should be prompted for input numbers
promptForNumbers = True

while True:
    if promptForNumbers:
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
        # Set prompt flag false to prevent re-prompting for numbers upon next loop
        promptForNumbers = False

    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers \n(6)Quit")
    print (f"Current numbers: {first_number} {second_number}")
    selection = float(input("Please select something (1-6): "))

    if selection == 1:
        print(f"The result is: {first_number + second_number}")    
    elif selection == 2:
        print(f"The result is: {first_number - second_number}")
    elif selection == 3:
        print(f"The result is: {first_number * second_number}")
    elif selection == 4:
        print(f"The result is: {first_number / second_number}")
    elif selection == 6:
        print("Thank you!") 
        break
    elif selection == 5:
        # Set prompt flag so that numbers will be requested upon next loop
        promptForNumbers = True  
else:
    print("Selection was not correct")

