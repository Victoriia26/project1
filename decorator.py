# from datetime import datetime
#
# def time(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         end = datetime.now() - start
#         print(end)
#     return wrapper
#
# @time
# def func1():
#     lists = []
#     for i in range(1, 1000000):
#         lists.append(i)
#     return lists
#
# @time
# def func2():
#     lists = [x for x in range(1, 1000000)]
#     return lists
#
# func1()
# func2()

# def gumburger(cotlet):
#     def wrapper(*args, **kwargs):
#         print("верхняя булочка")
#
#         cotlet(*args, **kwargs)
#
#         print("нижняя булочка")
#     return wrapper
#
# @gumburger
# def cotlet(ingridient):
#     print(f"котлета из {ingridient}")
#     #print("котлета из {}".format(ingridient))
#
# cotlet("chiken")

# lists = ["Kyial", "Saikal", "Meerim", "Vika"]
# print(f"m-{lists[1]}")
# print("{0} {2} {1} {3}".format(lists[1], lists[3], lists[0], lists[2]))

# d = {
#     "name": "Vika",
#      "age": 22
#      }
# name = d.pop("name")
# d.update({"name": "Eldar"})
#
# print(d)
# print(name)

# import math
# print(pow(3, 2))
# print(math.sqrt(4))

# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact
#
# number = int(input("Введите число: "))
# print(factorial(number))

from math import sqrt

a = int(input())
b = int(input())
c = sqrt((a**2) + (b**2))
print(c)


