# Main function
def main():
  # Get two numbers from user
  num1 = int(input("First number: "))
  num2 = int(input("Second number: "))

  # Call the divide function
  quotient = divide(num1, num2)

  # Display result
  if quotient is None:
    print("Cannot divide by zero.")
  else:
    print(f"{num1} divided by {num2} is {quotient}.")


def divide(num1, num2):
  '''
  Function that divides two numbers
  Param num1: int for the dividend
  Param num2: int for the divisor
  Return quotient: quotient of parameters or None
  '''
  if num2 == 0:
    return None
  result = num1 / num2
  return result

# Execute main
main()