# accept complex number
def parse_number(str_num):
  """
  Try converting the string to float first; if it fails,
  attempt complex. Return None if conversion is not possible.
  """
  try:
    # try to parse in float
    return float(str_num)
  except ValueError:
    pass

  try:
    # if it cannot parse float, try parse complex
    return complex(str_num)
  except ValueError:
    return None 

# create get_input() function
def get_inputs():
  """
  Receive input from the user: 2 numbers and an operator.
  If parsing the numbers fails, return (None, None, None).
  """
  str_num1 = input("Enter first number: ")
  operator = input("Enter operator (+, -, *, /): ")
  str_num2 = input("Enter second number: ")

  num1 = parse_number(str_num1)
  num2 = parse_number(str_num2)

  if num1 is None or num2 is None:
    print("Error: Please enter valid numbers (float or complex).")
    return None, None, None
  
  return num1, operator, num2

# create calculate() function
def calculate(num1, num2, operator):
  """
  Calculate by supporting both float and complex numbers.
  Return None if the operator is incorrect or another error occurs.
  """
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    # catch divided by 0
    # for complex use abs(num2) for checking it is 0 or not
    if abs(num2) == 0:
      return None # or you can raise Exception
    else:
      return num1 / num2
  else:
    return None # When invalid operator

# create display_result() function
def display_result(result):
  """
  Show the result. If the result is None, please indicate that it is an invalid operation.
  """
  if result is None:
    print("Error: Invalid operation!")
  else:
    print(f"Result: {result}")

# create main() function
def main():
  print("====== BASIC CALCULATOR ======")

  while True:
    num1, operator, num2 = get_inputs()
    if num1 is None or num2 is None or operator is None:
      # if error from parse input
      choice = input("Try again? (y/n): ")
      if choice.lower() != 'y':
        break
      continue # or break or ask it again

    result = calculate(num1, num2, operator)
    display_result(result)

    choice = input("Calculate again? (y/n): ")
    if choice.lower() != 'y':
      break

  print("Thank you for using the Basic Calculator!")

if __name__ == "__main__":
  main()