# create get_input() function
def get_inputs():
  num1 = float(input("Enter first number: "))
  operator = input("Enter operator (+, -, *, /): ")
  num2 = float(input("Enter second number: "))
  return num1, operator, num2

# create calculate() function
def calculate(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    # catch divided by 0
    if num2 == 0:
      return None # or you can raise Exception
    else:
      return num1 / num2
  else:
    return None # When invalid operator

# create display_result() function
def display_result(result):
  if result is None:
    print("Error: Invalid operation!")
  else:
    print(f"Result: {result}")

# create main() function
if __name__ == "__main__":
  num1, operator, num2 = get_inputs()
  result = calculate(num1, num2, operator)
  display_result(result)