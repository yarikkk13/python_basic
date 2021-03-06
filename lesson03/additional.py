""" Create функцию которая принимает число и возвращает текст как в примере:
   3275  — > "3000 + 200 + 70 +5" """


def func1(num: int) -> str:
    num = str(num)
    length = len(num)
    list_of_num = []
    i = 0
    while i < len(num):
        list_of_num.append(num[i] + '0' * (length - 1))
        length -= 1
        i += 1
    return '+'.join(list_of_num)


print(func1(121313))
""" Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
    Всегда будет только одно целое число, которое встречается нечетное количество раз
    [1, 2, 3, 4, 5, 2, 4, 1, 3] -> 5 """

list_of_n = [1, 2, 3, 4, 5, 2, 4, 1, 3]

odd_num: int = 0
for el in list_of_n:
    if list_of_n.count(el) % 2:
        odd_num = el
print(odd_num)

""" Знайти анаграму. Перевірити чи слово має в собі такі самі літери як і попереднє слово.
    ANAGRAM | MGANRAA -> true
    EXIT | AXET -> false
    GOOD | DOGO -> true """
word1 = 'EXIT'
word2 = 'AXET'
for el1 in word1:
    for el2 in word2:
        if el1 == el2:
            word1 = word1.replace(el1, '_')
            word2 = word2.replace(el2, '_')
if word1 == word2:
    print('true')
else:
    print('false')

""" Точная степень двойки. Дано натуральное число N. Выведите слово YES, если число N является
    точной степенью двойки, или слово NO в противном случае. Операцией возведения в степень 
    пользоваться нельзя! """

n = int(input('Введіть число, яке хочете превірити:'))
i = 1
while i < n:
    i = i * 2
if i == n:
    print("YES")
else:
    print("NO")
# print("NO" if (n := int(input('Введіть число, яке хочете превірити:'))) & (n - 1) else "YES")


""" Сумма цифр числа. Дано натуральное число N.Вычислите сумму его цифр. При решении этой задачи нельзя
    использовать строки, списки, массивы ну и циклы, разумеется.
    Рекурсія)."""


def sum_1(n):
    if n > 0:
        return n % 10 + sum_1(n // 10)
    else:
        return 0


def sum_(n):
    return n % 10 + sum_(n // 10) if n > 0 else 0


print(sum_1(985736279))

""" Палиндром
    Дано слово, состоящее только из строчных латинских букв.Проверьте, является ли это слово палиндромом.
    Выведите YES или NO. При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя
    использовать срезы с шагом, отличным от 1."""

pal1 = 'niain'
pal2 = 'tennet'
pal3 = 'tenpopopopopopoppppppppnet'


def palindromat(string: str):
    if len(string) < 2:
        print('yes')
    elif string[0] == string[len(string) - 1]:
        palindromat(string[1:len(string) - 1])
    else:
        print('no')


palindromat(pal1)
palindromat(pal2)
palindromat(pal3)

""" Количество единиц
    Дана последовательность натуральных чисел в строке, завершающаяся двумя числами 0 подряд. Определите,
    сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо
    игнорировать.
    2176491947586100 -> 3 """

str_of_num = '217641119910947586100322142'
length = len(str_of_num)
new_str = []
i = 0
while i < length - 1:
    if str_of_num[i] != '0':
        new_str.append(str_of_num[i])
    elif str_of_num[i] == str_of_num[i + 1]:
        break
    else:
        new_str.append('0')
    i += 1
print(new_str.count('1'))

""" Вирівняти багаторівневий масив в однорівневий
    [1, 3, ['Hello, 'World', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'World', 9, 6, 1, 'oops', 9]
    flat використовувати заборонено."""

list_of_lists = [1, 3, ['Hello', 'World', [9, 6, 1]], ['oops'], 9]


# l2: list = []
def flatter(l: list, l2: list = []):
    for el in l:
        if type(el) != list:
            l2.append(el)
        if type(el) == list:
            flatter(el)
    return l2


print(flatter(list_of_lists))
# не знаю як зробити щоб не створювати глобальну змінну або передавати її в самій функції дефолтним значенням

""" Знайти найбільший елемент в масиві за допомогою reduce
    [1, 6, 9, 0, 17, 88, 4, 7] -> 88 """

#  https://www.geeksforgeeks.org/reduce-in-python/

import functools

list_for_reduce = [1, 6, 9, 0, 17, 88, 4, 7]
max_num = functools.reduce(lambda a, b: a if a > b else b, list_for_reduce)
print(max_num)
