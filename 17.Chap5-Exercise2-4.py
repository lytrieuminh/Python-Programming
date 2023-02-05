#Viope-Chap5-Exercise2-4:

a = input("Give a file name: ")
b = input("Write something: ")
myfile = open(a, "w")

myfile.write(b)
myfile.close()

print(f"Wrote {b}  to the file {a}")

