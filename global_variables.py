# Define a global constant for the contribution rate
CONTRIBUTION_RATE = 0.05

# Create main function
def main():
  # Get gross pay and bonus
  gross_pay = float(input("What is the employee's gross pay? "))
  bonus = float(input("What is the employee's bonus? "))

  # Pass to functions
  pay_contribution(gross_pay)
  bonus_contribution(bonus)

# Create a function to calculate and display pay contribution
def pay_contribution(pay):
  global CONTRIBUITION_RATE
  # Calculate the contribution amount
  contribution = pay * CONTRIBUTION_RATE
  # Display contribution
  print(f"The amount of gross pay contribution is ${contribution:,.2f}.")

# Create a function to calculate and display the bonus contribution
def bonus_contribution(bonus):
  global CONTRIBUTION_RATE
  # Calculate the contribution amount
  contribution = bonus * CONTRIBUTION_RATE
  # Display contribution
  print(f"The amount of bonus pay contribution is ${contribution:,.2f}.")

# Call main
main()