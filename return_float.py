def currency(value):
  '''
  Function that formats a float as currency
  Param value: float representing a curency amount
  Return: a string formatted for currency
  '''
  return f"${value:,.2f}"

# Sequence of main function
def main():
  value = float(input("What is the amount? "))

  print(currency(value))


# Execute main function
main()