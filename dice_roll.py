# Import modules
import random

# Define global constants for dice
DICE_MIN = 1
DICE_MAX = 6

# Create main function
def main():
  # Create variable to control the loop
  again = "y"
  # Create loop to hold statements that simulate rolling two dice
  while again == "y":
    for r in range(2):
      roll = random.randint(DICE_MIN, DICE_MAX)
      print(roll)

    #Check if the user wants to roll the dice again
    again = input("Do you want to roll again? (y or n) ")

# Call main function
main()