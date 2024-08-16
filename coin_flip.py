# Get random module
import random

# Main function
def main():
  # Start count-controlled loop
  for flip in range(10):
    # Get random number (choice of 2)
    result = random.randint(1, 6)
    # Display string for each number (condition)
    print(result)

# Execute main
main()