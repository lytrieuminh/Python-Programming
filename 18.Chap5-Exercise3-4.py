#Viope-Chap5-Exercise3-4:

filename="strings.txt"
handle = open("strings.txt","r") #read file
content = handle.readlines() # read lines by lines

for i in content:
    if i.rstrip().isalnum():
        print(i.rstrip()," was ok.")
    else:
        print(i.rstrip()," was invalid.")
handle.close()

