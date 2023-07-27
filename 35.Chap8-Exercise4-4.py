# Viope-Chap8-Exercise4-4:

import time

try:
    f = open("notebook.txt", "r")
    print("Now using file", f.name)

except Exception:
    print("No default notebook was found, created one.")
    mf = open("notebook.txt", "w")
    print("Now using file", mf.name)


mf = "notebook.txt"
promptForNumbers = True

while True:
    print("(1)Read the notebook\n(2)Add note\n(3)Empty the notebook\n(4)Change the notebook\n(5)Quit\n")
    selection = int(input("Please select one: "))

    if selection == 1:
        with open(mf, "r") as file:
            content = file.read()
            print(content)
            f = open(mf)
            print("Now using file", f.name)

    elif selection == 2:
        more_note = input("Write a new note: ")
        write_file = open(mf, "w")
        write_file.write(more_note)
        write_file.write(":::")
        write_file.write(time.strftime("%X %x"))
        write_file.close()
        print("Now using file ", write_file.name)

    elif selection == 3:
        empty_file = open("notebook.txt", "w")
        empty_file.close()
        print("Notes deleted.")

    elif selection == 4:
        mf = input("Give the name of the new file: ")
        try:
            f = open(mf)
            filetext = f.read()
            print("Now using file", f.name)

        except Exception:
            print("No notebook with that name detected, created one.")
            x = open(mf, "w")
            print("Now using file", x.name)
        else:
            f.close
            promptForNumbers = True

    elif selection == 5:
        print("Notebook shutting down, thank you.")
        break

    else:
        print("Incorrect selection")
