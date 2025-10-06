'''text="привет как у вас дела?" #можно заменить на input() что бы пользователь ввел свой текст
spaces = text.count(" ")
print("количество пробелов:",spaces)'''
from email.policy import default

#text=input("введите текст:")
#spaces = text.replace(" ","_")
#print("количество пробелов:",spaces)


#numbers = [1,2,3,4,5,6,7,8,9]
#people = ["Tom", "Sam", "Bob"]
#cars=["blue","red","yellow","grey","green"]
#print(cars[2]) выведет yellow
#print(cars[-2]) выведет grey
#cars[2]="purple" присваивание нового значения
#del cars[2]
#print(cars)
#print(type(cars[0]),type(cars[1]))

#numbers1 = []
#numbers2 = list()

'''numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
print(numbers2)  # [1, 2, 3, 4, 5]

letters = list("Hello")
print(letters)  # ['H', 'e', 'l', 'l', 'o']'''

'''numbers = [5] * 6  # 6 раз повторяем 5
print(numbers)  # [5, 5, 5, 5, 5, 5]

people = ["Tom"] * 3  # 3 раза повторяем "Tom"
print(people)  # ["Tom", "Tom", "Tom"]

students = ["Bob", "Sam"] * 2  # 2 раза повторяем "Bob", "Sam"
print(students)  # ["Bob", "Sam", "Bob", "Sam"]'''

'''people = ["Tom", "Bob"]

people.append("Alice")

people.insert(1, "Bill")
people.extend(["Mike", "Sam"])
index_of_tom = people.index("Tom")
removed_item = people.pop(index_of_tom)
last_item = people.pop()
people.remove("Alice")
print(people)
people.clear()
print(people)

num = int(input("Введите число: "))
num_str = str(abs(num))
print(f"Количесвто цифр: {len(num_str)}")
digits = [int(d) for d in num_str]
print("Цифры по разряда:", digits)
print("Сумма цифр:", sum(digits))
'''