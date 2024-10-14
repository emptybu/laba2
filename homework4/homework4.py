import random
def my_generate(count=10, start=0, stop=200):
    for _ in range(count):
        yield random.randint(start, stop)

def find():
    X = input("Введите цифру X: ")
    try:
        X = int (X)
        if X >= 0 and X<10:
            numbers = list(my_generate(10, 0, 200))
            print(f"Случайные числа: {numbers}")
            multiples = list(filter(lambda num: num % X == 0, numbers))
            print(f"Числа, кратные {X}: {multiples}")
        else:
            print ('Введите цифру')
    except ValueError:
        print ('Введите цифру')

find()
