from art import logo

print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation symbol from above: ")

answer = operations[operation_symbol](n1=int(num1), n2=int(num2))

print(f"{num1} {operation_symbol} {num2} = {answer}")
