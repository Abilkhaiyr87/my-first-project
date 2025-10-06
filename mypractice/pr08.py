# num1=int(input("введите число элементов списка: "))
# sp=[]
# #s=0
# for i in range(1,num1+1):
#     sp.insert(i,int(input(f"введите {i} число: ")))
# print(sum(sp))

num1=int(input("введите число элементов списка: "))
sp=[]
s=0
for i in range(num1):
    el=int(input(f"Введите {i+1} число: "))
    sp.append(el)
    s+=el
print("список: ",sp)
print("сумма: ",s)
print("среднее арифметическое: ", s/num1)
print("максимальное значение",max(sp))
print("мимнимальное значение",min(sp))
plus = []
minus= []
for n in sp:
    if n>0:
        plus.append(n)
    else:
        minus.append(n)
print("вывод отрицательных знач",minus)
print("вывод положительных знач",plus)
