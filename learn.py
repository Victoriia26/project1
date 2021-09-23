# # генераторы списков
# lists = []
# for i in range(0, 100):
#     lists.append(i)
#
# print(lists)

# list2 = [x for x in range(100)]
# print(list2)

# lists = []
# for i in range(1, 1000):
#     if i % 3 == 0:
#         lists.append(i)
#
# print(lists)

# lists = [x for x in range(1, 100) if x % 3 == 0]
# print(lists)

# lists = []
# for i in range(-100, 50):
#     if i % 3 == 0 and i % 5 == 0:
#        # pow(i, 3)
#         number = abs(i**3)
#         lists.append(number)
#
# print(lists)

# lists = [abs(pow(x, 3)) for x in range(-100, 50) if x % 3 == 0 and x % 5 == 0]
# print(lists)

# def filter_list(range1, range2):
#     lists = [abs(pow(x, 3)) for x in range(range1, range2) if x % 3 == 0 and x % 5 == 0]
#     return lists
#
# print(filter_list(-100, 50))

# kyal = {
#     'home': '2этаж',
#     'car': 'BMW x7'
# }
#
# saykal = {
#     'home': '3этаж',
#     'car': 'Toyota 470'
# }
#
# eldar = {
#     'home': '6этаж',
#     'car': 'Mers 222'
# }

# python_boot = [eldar, saykal, kyal]
# print(python_boot)
# home = list()
# for i in python_boot:
#     home.append(i.get('home'))
#
# print(home)

# python_boot = [eldar, saykal, kyal]
# car = [x.get('car') for x in python_boot]
# print(car)

from datetime import datetime

def func1():
    lists = []
    start = datetime.now()
    for i in range(1, 1000000):
        lists.append(i)
    end = datetime.now() - start
    print('Время для цикла for', end)
    return lists

def func2():
    start = datetime.now()
    lists = [x for x in range(1, 1000000)]
    end = datetime.now() - start
    print('Время list comprehentions', end)
    return lists

func1()
func2()