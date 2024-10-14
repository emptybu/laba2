from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    
    # Замена точек и пробелов на слеши
    birth_date = birth_date.replace('.', '/').replace(' ', '/')
    
    try:
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    except ValueError:
        return "Некорректный формат даты. Пожалуйста, используйте формат дд/мм/гггг."

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

date_of_birth = input("Введите дату рождения (дд/мм/гггг): ")
age = calculate_age(date_of_birth)

if isinstance(age, int):
    print(f"Ваш возраст: {age} лет")
else:
    print(age)  # Вывод ошибки
