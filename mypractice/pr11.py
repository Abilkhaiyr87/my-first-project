'''
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def hello(self):
        print(f"Привет, я {self.name}!")
        print(f"мне {self.age} лет")

a=Human("нпс Расульчик",17)
b=Human("нпс Рамазанчик",18)

a.hello()
b.hello()
'''
from functools import total_ordering
from random import random

'''import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()'''

"""import random
numbers=[random.randint(1,100) for _ in range(100) ]
with open("numbers.txt","w") as f:
     for num in numbers:
         f.write(str(num)+"\n")

with open("numbers.txt", "r") as f:
    numbers = f.readlines()
numbers=[int(x.strip()) for x in numbers]
total=sum(numbers)
print("Сумма чисел",total)"""