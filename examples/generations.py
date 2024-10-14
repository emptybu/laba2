def my_generate(start=0, stop=5):
    number = start
    while number <= stop:
        yield number
        number += 1

for value in my_generate(1, 4):
    print(value)  # 1, 2, 3, 4
