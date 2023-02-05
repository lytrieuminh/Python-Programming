#Viope-Chap3-Exercise5-5:

print("Calculator")
FirstNumber = int(input("Give the first number: "))
SecondNumber = int(input("Give the second number: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
SomeThing = float(input("Please select something (1-4): "))
if SomeThing == 1:
	print("The result is: ",FirstNumber+SecondNumber)
elif SomeThing == 2:
	print("The result is: ",FirstNumber-SecondNumber)
elif SomeThing == 3:
	print("The result is: ",FirstNumber*SecondNumber)
elif SomeThing == 4:
	print("The result is: ",FirstNumber/SecondNumber)
else:
	print("Selection was not correct.")

