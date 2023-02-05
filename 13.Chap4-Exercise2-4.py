#Viope-Chap4-Exercise2-4:

random_write = True

while random_write:
    random_write = input("Write something: ")
    if random_write != "quit":
        print(random_write)
    elif random_write == "quit":
        print("Bye bye!")
        random_write = False

