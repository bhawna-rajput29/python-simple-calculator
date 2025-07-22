def calculator(a, b, operation):
  if operation == "add":
      return a + b
  elif operation == "subtract":
      return a - b
  elif operation == "multiply":
      return a * b
  elif operation == "divide":
      return a / b
  else:
      return "Invalid operation"

# Example use
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Choose operation (add, subtract, multiply, divide): ")

result = calculator(num1, num2, op)
print("Result:", result)
