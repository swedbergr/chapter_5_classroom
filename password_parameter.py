# Define main function
def main():
  password = input("Enter the password: ")
  pass_check(password)
  print("This is the main function after the password is correct.")

def pass_check(password):
  while password != "period7":
    print("That is an incorrect password. Please try again.")
    password = input("Enter the password: ")

main()