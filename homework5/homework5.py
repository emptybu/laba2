def get_number():
    for number in range(30):
        if number % 2 != 0:
            yield number

# Получаем нечетные числа
odd_numbers = list(get_number())

# Выводим первое, пятое и последнее нечетное число
first = odd_numbers[0] if len(odd_numbers) > 0 else None
fifth = odd_numbers[4] if len(odd_numbers) > 4 else None
last = odd_numbers[-1] if len(odd_numbers) > 0 else None

print(f"Первое нечетное число: {first}")
print(f"Пятое нечетное число: {fifth}")
print(f"Последнее нечетное число: {last}")
