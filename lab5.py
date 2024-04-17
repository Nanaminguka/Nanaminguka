def arithmetic_sequence(start, step):
    while True:
        yield start
        start += step

# Пример использования генератора
seq = arithmetic_sequence(1, 3)
for _ in range(5):
    print(next(seq))
