def main():
  # Get two numbers from the user to add
  num1 = int(input("First number: "))
  num2 = int(input("Second number: "))

  # Call sum function
  total = sum(num1, num2)

  # Display sum
  print(f"The sum of {num1} and {num2} is {total}.")


def sum(num1, num2):
  '''
  Define a function that takes two ints and adds them together
  Param num1: int to be added
  Param num2: int to be added
  Return: an int result of the sum
  '''
  total = num1 + num2
  return total


# Execute main
main()