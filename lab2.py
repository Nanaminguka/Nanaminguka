def convert_currency(amount, source_currency, target_currency, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

# Пример использования
amount = 100  # Исходная сумма
source_currency = 'USD'  # Исходная валюта
target_currency = 'EUR'  # Целевая валюта
exchange_rate = 0.85  # Курс обмена USD/EUR

converted_amount = convert_currency(amount, source_currency, target_currency, exchange_rate)
print(f"{amount} {source_currency} равно {converted_amount} {target_currency}")
