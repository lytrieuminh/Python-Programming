#Viope-Chap3-Exercise4-5:

a = int(input("Give a number: "))
b = int(input("Give another number: "))
if (a%2 == 0) and (b%2 == 0):
	print("Both numbers are even.")
elif (a%2 != 0) and (b%2 != 0):
	print("Both numbers are odd.")
else:
	print("One of the numbers is even")

