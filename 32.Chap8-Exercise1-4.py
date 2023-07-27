# Viope-Chap8-Exercise1-4:

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

userinput = input("Give a number: ")

try:
    if any(char in numbers for char in userinput):
        userinput.isdigit() == True
        print("The input was suitable!")
    else:
        print("The input was malformed.")

except:
    raise TypeError
