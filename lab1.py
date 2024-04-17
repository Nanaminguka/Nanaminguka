def sum_even_squares(numbers):
    # Отфильтровать четные числа
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    # Возвести их в квадрат
    squared_numbers = map(lambda x: x ** 2, even_numbers)
    # Найти сумму
    return sum(squared_numbers)

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_squares(numbers)
print(result)  # Выведет: 220 (4^2 + 6^2 + 8^2 + 10^2 = 16 + 36 + 64 + 100 = 220)
