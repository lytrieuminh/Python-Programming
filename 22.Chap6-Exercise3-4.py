#Viope-Chap6-Exercise3-4:

given_string = True

while given_string:
  given_string = input("Write something (quit ends): ")

  if given_string != "quit" and len(given_string) < 10:
    print("Too short")
  elif given_string != "quit" and len(given_string) >= 10:
    print(given_string)
  elif given_string == "quit":
    given_string = False

