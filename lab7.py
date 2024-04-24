# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

# Пример испольования
if __name__ == "__main__":
    print("Addition:", add(8, 9))
    print("Subtraction:", subtract(10, 4))
    print("Multiplication:", multiply(7, 2))
    print("Division:", divide(15, 3))
    print("Power:", power(2, 4))
