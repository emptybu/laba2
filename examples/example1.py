def example(color):
    if color == "black":
        return "me too"
    elif color == "white":
        return "i hate this color"
    else:
        return "I don't know"

# ввод пользователем
what_is_it = input("What is your favorite color? ")

# вызов функции
result = example(what_is_it)
print(result)
