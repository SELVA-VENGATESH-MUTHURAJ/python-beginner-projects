def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
print("Choose an operation: +  -  *  / ")

op = input("Operation: ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(n1, n2))
elif op == '-':
    print("Result:", sub(n1, n2))
elif op == '*':
    print("Result:", mul(n1, n2))
elif op == '/':
    print("Result:", div(n1, n2))
else:
    print("Invalid operation.")
