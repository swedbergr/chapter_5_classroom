# Import math module
import math

def main():
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter a number: "))

  # Use a function from the math module
  calc = math.sin(math.radians(num1))

  # Display result
  print(calc)
main()