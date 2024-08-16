# Create a program that decripts a message knowing the seed

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
    decrypt(char)

# Create function that changes the character by a random amount
def decrypt(char):
  # Get ascii value of char
  ascii = ord(char)

  # Change char by random number
  ascii -= random.randint(0, 126)

  # Verify the number is between 32 and 126
  if ascii < 32: ascii += 95

  # Convert back to char and display
  enc_char = chr(ascii)
  print(enc_char, end="")


# Execute main
main()