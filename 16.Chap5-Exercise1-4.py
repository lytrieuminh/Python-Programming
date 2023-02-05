#Viope-Chap5-Exercise1-4:

readfile = open("facts.txt","r")
content = readfile.readlines()

print("Following was read from the file:")
for i in content:
	print(i)

readfile.close()

