#Viope-Chap5-Exercise4-4:

promptForNumbers = True

while True:
  print("(1)Read the notebook\n(2)Add note\n(3)Empty the notebook\n(4)Quit\n")
  selection = int(input("Please select one: "))
  
  if selection == 1:
    with open("notebook.txt","r") as file:
      content = file.read()
      print(content)

  elif selection == 2:
    more_note= input("Write a new note: ")
    write_file = open("notebook.txt","a")
    write_file.write(more_note)
    write_file.close()
	
  elif selection == 3:
    read_file = open("notebook.txt","w")
    read_file.close()
    print("Notes deleted.")
	
  elif selection == 4:
    print("Notebook shutting down, thank you.")
    break
	
  else:
    print("Incorrect selection")

