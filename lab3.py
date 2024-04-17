def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования функции
result = factorial(5)
print("Факториал числа 5 равен:", result)
