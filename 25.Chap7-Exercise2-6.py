#Viope-Chap7-Exercise2-6:

import random


def sub(computer):
  if computer == 1:
    computer = "Foot"
  elif computer == 2:
    computer = "Nuke"
  elif computer == 3:
    computer = "Cockroach"
  print("Computer chose: ", computer)


def main():
  wins = 0
  rounds = 0
  draws = 0

  while True:
    computer = random.randint(1, 3)
    player = input("Foot, Nuke or Cockroach? (Quit ends): ")

    if player == "Quit":
      print("You played", rounds, "rounds, and won", wins,
            "rounds, playing tie in", draws, "rounds.")
      break
    elif player == ("Spaceshuttle"):
      print("Incorrect selection.")
    else:
      print("You chose: ", player)
      sub(computer)
      rounds += 1

      if (player, computer) == ("Foot", 1):
        draws += 1
        print("It is a tie!")
      elif (player, computer) == ("Foot", 2):
        print("You LOSE!")
      elif (player, computer) == ("Foot", 3):
        wins += 1
        print("You WIN!")
      elif (player, computer) == ("Nuke", 2):
        print("Both LOSE!")
      elif (player, computer) == ("Nuke", 1):
        wins += 1
        print("You WIN!")
      elif (player, computer) == ("Nuke", 3):
        print("You LOSE!")
      elif (player, computer) == ("Cockroach", 1):
        print("You LOSE!")
      elif (player, computer) == ("Cockroach", 2):
        wins += 1
        print("You WIN!")
      elif (player, computer) == ("Cockroach", 3):
        draws += 1
        print("Both LOSE!")


if __name__ == "__main__":
  main()

