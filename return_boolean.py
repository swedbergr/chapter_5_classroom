def input_validation(user_input):
  '''
  Funtion validates input
  Param user_input: string input from user
  Return: boolean representing if input validates
  '''
  # Check if user_input is correct
  if user_input == "password":
    return True
  return False

# Main function
def main():
  # Iterate until correct password
  while True:
    password = input("Password: ")
    if input_validation(password):
      break

  # Main function
  print("You got through the password!")

# Execute main
main()