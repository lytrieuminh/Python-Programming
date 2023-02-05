#Viope-Chap3-Exercise2-5:

a = input("Give name: ")
if(a == "John"):
    a = input("Give password: ")
    if(a == "ABC123"):
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")

