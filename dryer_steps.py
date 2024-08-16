# Create main function for step-by-step instructions for disassembling a dryer
def main():
  # Display start-up message
  startup_message()
  input("Press Enter to see step 1")

  # Display steps pausing between each one
  step1()
  input("Press Enter to see step 2")
  step2()
  input("Press Enter to see step 3")
  step3()
  input("Press Enter to see step 4")
  step4()


# Function that provides the startup message
def startup_message():
  print("This program tells you how to")
  print("dissassemble an ACME laundry dryer.")
  print("There are 4 steps in the process.\n")

# Function that provides instructions for step 1
def step1():
  print("Step 1: Unplug th edryer and")
  print("move it away from the wall.\n")

# Function that provides instructions for step 2
def step2():
  print("Step 2: Remove the sex screws")
  print("from the back of the dryer.\n")

# Function that provides instructions for step 3
def step3():
  print("Step 3: Remove the back panel")
  print("from the dryer.\n")

# Function that provides instructions for step 4
def step4():
  print("Step 4: Pull the top of the")
  print("dryer straight up.")

# Run main
main()