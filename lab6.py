def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment, decrement

# Создание счетчика
increment_counter, decrement_counter = make_counter()

# Пример использования: увеличиваем счетчик на 5
for _ in range(5):
    print("Increment:", increment_counter())

# Пример использования: уменьшаем счетчик на 3
for _ in range(3):
    print("Decrement:", decrement_counter())
