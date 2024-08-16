# Program that encrypts a message from the user and assigns a seed

# Import modules
import random

# Create main function
def main():
  # Get message from the user to be encrypted
  message = input("What message do you want to encrypt? ")
  # Get a set seed from the user
  seed = int(input("Seed for encryption: "))
  random.seed(seed)

  # Isolate message characters and encrypt each one
  for index in range(len(message)):
    char = message[index]
    encrypt(char)

# Create function that changes the character by a random amount
def encrypt(char):
  # Get ascii value of char
  ascii = ord(char)

  # Change char by random number
  r = random.randint(0, 126)
  ascii += r


  # Verify the number is between 32 and 126
  if ascii > 126: ascii -= 95

  # Convert back to char and display
  enc_char = chr(ascii)
  print(enc_char, end="")


# Execute main
main()