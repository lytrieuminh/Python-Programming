#Viope-Chap6-Exercise4-4:

#Define subfunction:
def write_something(input_sentence: str, result: str = "Too short"):
    if len(input_sentence) >= 10:
        if "X" in input_sentence:
            result = input_sentence + "\nX spotted!"
        else:
            result = input_sentence
    return result

#Define main function:
def main():
    while True:
        sentence = input("Write something (quit ends): ")
        if sentence == "quit":
            break
        print(write_something(sentence))

if __name__ == '__main__':
    main()

