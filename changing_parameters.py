def main():
  num = int(input("Enter a number: "))
  increase(num)
  print(f"The value of num in main is {num}.")

def increase(num):
  num += 1
  print(f"The value of num in increase is {num}.")

main()