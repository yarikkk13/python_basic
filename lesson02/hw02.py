# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################
st = 'as 23 fdfdg544'
list = []
for element in st:
    if element.isdigit():
        list.append(element)
print(','.join(list))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
st2 = 'as 23 fdfdg544 34'
list2 = []
for element in st2:
    if element.isdigit():
        list2.append(element)
    else:
        element = 'i'
        list2.append(element)
st2 = ''.join(list2)
list2 = st2.split('i')
new_list = []
for element in list2:
    if element.isdigit():
        new_list.append(element)
print(','.join(new_list))

# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
greetingList = [element.upper() for element in greeting]
print(greetingList)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
listOfNum = [i ** 2 for i in range(50) if i % 2 != 0]
print(listOfNum)


# function
# - створити функцію яка виводить ліст
def show_list():
    print([i ** 2 for i in range(50) if i % 2 != 0])


show_list()


# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def min_num(a, b, c):
    print(min(a, b, c))
    return min(a, b, c)


min_num(23, 43, 54)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_num(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


max_num(323, 54665, 54)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max_num(*args):
    print(max(*args))
    return min(*args)


min_max_num(23, 43, 54, 32, 43, 54, 65, 54, 323, 54665, 54)


# - створити функцію яка повертає найбільше число з ліста
def max_of_list(list13):
    return max(list13)


max_of_list(listOfNum)


# - створити функцію яка повертає найменьше число з ліста
def min_of_list(list13):
    return min(list13)


min_of_list(listOfNum)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_of_list(list13):
    return sum(list13)


sum_of_list(listOfNum)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def mean_of_list(list13):
    return sum(list13) / len(list13)


mean_of_list(listOfNum)


# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення


def decor(func):
    def wrap():
        func()
        str = func()
        print(str.replace('_', ' '))

    return wrap


@decor
def pr():
    return 'Hello_boss_!!!'


pr()
