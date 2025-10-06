'''a= int(input("введите число а:"))
b=int(input("введите число b:"))
if a>b:
    F=a
else:
    F=b
    print("наибольшее число",F)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
g =  a if a>b else b
print("Наибольшее число: ",g)



amount = int(input("Введите сумму продажи: "))
if amount > 0:
    if amount>25000:
        discount=amount * 0.3
    elif amount>15000:
        discount=amount * 0.2
    elif amount>5000:
        discount = amount*0.12
    else:
        discount = amount*0.05
    print("Скидка: ", discount)
    print("Сумма с учетом скидки : ", amount-discount)
else:
    print("Некорректная сумма")'''
#циклы
# бесконечный цикл
while True:
    # вводим первое число
    num1 = int(input("Введите первое число: "))
    # вводим второе число
    num2 = int(input("Введите второе число: "))
    # вычисление суммы чисел
    print("Сумма чисел: ", num1+num2 )
    # запрос на выход из цикла
    str = input ("Нажмите Y или y для завершения программы: ")
    # выходим из цикла
    if (str =="Y" or str =="y"):  break