def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def devide(n1, n2):
  return n1 / n2

operations = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": devide
       }

num1 = int(input("What is the first number?:"))
num2 = int(input("What is the second number?:"))

for i in operations:
  print(i)

choice = input("Choose an operation: ")
answer = operations[choice](num1, num2)
print(f"{num1} {choice} {num2} = {answer}")
