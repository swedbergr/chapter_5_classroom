def get_name():
  '''
  Function gets a first and last name from user and returns them
  Return: string of first name
  Return: string of last name
  '''
  first = input("First name: ")
  last = input("Last name: ")
  return first, last

# Main function
def main():
  first, last = get_name()
  print(f"Hello, {first} {last}.")

# Execute main
main()