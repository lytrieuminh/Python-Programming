# Viope-Chap8-Exercise2-4:

def getfilename():
    filename = input("Give the file name: ")
    return filename


def main():
    returned = getfilename()

    try:
        handle = open(returned, "r")
        filetext = handle.read()
        result = 1000 / float(filetext)

    except IOError:
        print("There seems to be no file with that name.")

    except (TypeError, ValueError):
        print("The file contents were unsuitable.")

    else:
        print(f"The result was {result}")


if __name__ == "__main__":
    main()
