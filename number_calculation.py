# Main function
def main():
  val1 = int(input("Give me an int to add: "))
  val2 = int(input("Give me another int to add: "))
  sum(val1, val2)

# Create function that gets two values and calculates their sum
def sum(num1, num2=0):
  sum = num1 + num2
  print(f"{num1} + {num2} = {sum}")

# Run program
main()