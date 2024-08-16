# Evolution of number validation
improved_input = input()

# Step 1: Ignore ".", ",", and "-"
if not improved_input.replace(".", "").replace(",", "").replace("-", "").isdigit():
  print("Please only input a number.")

# Step 2: Ignore all "," but only the first "." and "-"
if not improved_input.replace(".", "", 1).replace(",", "").replace("-", "", 1).isdigit():
  print("Please only input a number.")

# Step 3: Ignore all ",", only the first "." after the first character and check if only the first character is "-" ir digit
if not improved_input[1:].replace(".", "", 1).replace(",", "").isdigit() and \
  not (improved_input[0] == "-" or improved_input[0].isdigit()):
  print("Please only input a number.")

# Step 4: Produce separate conditions for when the input is a single number and multiple characters
if len(improved_input) == 1:
  if not improved_input.isdigit():
    print("Please only input a number.")
elif not improved_input[1:].replace(".", "", 1).replace(",", "").isdigit() and \
   not (improved_input[0] == "-" or improved_input[0].isdigit()):
  print("Please only input a number.")

# Step 5: Produce separate conditions for when the input is a single number, starts with a decimal and has multiple
# characters, and starts with anything else and has multiple characters.
if len(improved_input) == 1:
  if not improved_input.isdigit():
    print("Please only input a number.")
elif improved_input[0] == ".":
  if not improved_input[1:].isdigit():
    print("Please only input a number.")
elif not improved_input[1:].replace(".", "", 1).isdigit() or \
  not (improved_input[0] == "-" or improved_input[0].isdigit()):
  print("Please only input a number.")