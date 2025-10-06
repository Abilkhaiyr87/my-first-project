"""print(6 + 2)  # 8
print(6 - 2)  # 4
print(6 * 2)  # 12
print(6 / 2)  # 3.0
print(7 / 2)  # 3.5
print(7 // 2)  # 3
print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36

print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1
number = 3 + 4 * 5 ** 2 + 7
print(number)  # 110
number = (3 + 4) * (5 ** 2 + 7)
print(number)  # 224
number = 10
number += 5
print(number)  # 15

number -= 3
print(number)  # 12

number *= 4
print(number)  # 48
first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number) # 0.40002000000000004
print(2.0001 + 0.1)  # 2.1001000000000003
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number))  # 2
first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4))  # 2.1001
 #округление до целого числа
print(round(2.49))  # 2 - округление до ближайшего целого 2
print(round(2.51))  # 3


P = float(input("Начальная сумма вклада: "))
R = float(input("Процент по вкладу: "))
T = float(input("Количество лет: "))


interest = (P * R * T) / 100


print("Начисленные проценты:", interest)"""


'''# Запрашиваем температуру в Цельсиях у пользователя
celsius = float(input("Введите температуру в градусах Цельсия: "))

# Переводим температуру в Фаренгейты по формуле
fahrenheit = (9/5) * celsius + 32

# Выводим результат
print(f"{celsius} градусов Цельсия равны {fahrenheit} градусам Фаренгейта")'''


y = int(input("Введите год: "))


if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    print("Год високосный")
else:
    print("Год не високосный")

