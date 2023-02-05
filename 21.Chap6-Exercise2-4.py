#Viope-Chap6-Exercise2-4:

#Define subfunction:
def power_of_two(x):
    result = 2 ** x
    print(f"The result is {result}")

#Define main function:
def main():
    x = int(input("Give a number: "))
    power_of_two(x)
  

if __name__ == "__main__":
    main()

    