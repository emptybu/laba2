import random

def get_user_choice():
    user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while user_input not in ["камень", "ножницы", "бумага"]:
        print("Некорректный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
        user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

# Основная логика игры
user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(f"Ваш выбор: {user_choice}")
print(f"Выбор компьютера: {computer_choice}")

result = determine_winner(user_choice, computer_choice)
print(result)
