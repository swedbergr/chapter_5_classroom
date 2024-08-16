# Main statements for our program
def main():
  num1 = int(input("First number: "))
  message1()
  num2 = int(input("Second number: "))
  message2()

  sum = num1 + num2
  print(f"The sum is {sum}.")

# Define message1
def message1():
  print("Congradulations on picking a number!")

# Define message2
def message2():
  print("Wow! You are good at picking numbers!")

main()