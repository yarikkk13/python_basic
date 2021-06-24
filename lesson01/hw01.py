# # 1)Дан лист:
# #   list = [22, 3,5,2,8,2,-23, 8,23,5]
# #   - найти min число в листе
# #   - удалить все одинаковые значения
# #   - заменить каждое четвертое значение на "Х"
# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# # 3) вывести табличку умножения с помощью цикла while
# # 4) переделать первое задание под меню с помощью цикла
# #
# # ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# # пример:
# # [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# # [-1, -2, 3, 4, 555] => 4
# # [5, 5, 5, 5] => 5
# # [-10, 5, 5] => 5


list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# 1) finding the smallest num
smallestNum = list[0]
for i in list:
    if smallestNum > i:
        smallestNum = i
print(smallestNum)

# 2) delete all similar values

# for i in list:
#     if list.count(i)>1:
#         list.remove(i)
# print(list)
# якщо повторювані числа знаходяться один за одним, то наступне не видаляється,
# тобто список потрібно прогнати з кінця до початку

length = len(list)
while length > 0:
    if list.count(list[length - 1]) > 1:
        list.remove(list[length - 1])
    length -= 1
print(list)

# 3) replace every fourth value with x

i = 0
length = len(list)
while i < length:
    if i % 4 == 0 and i > 0:
        list[i - 1] = 'x'
    i += 1
else:
    print(list)

# 4) show on the screen empty square with '*' on its sides, side is in variable:
#
side = int(input('enter number : '))
for i in range(side):
    if i == 0 or i == side - 1:
        print('*' * side)
    else:
        print('*' + ' ' * (side - 2) + '*')

# 5) create multiplication table with cycle 'while'
n = int(input('to what number do you want multiplication table : '))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i * j, end="\t")
        j += 1
    i += 1
    print()

# 6) show the element of list which is the nearest to the mean of elements of this list

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [-1, -2, 3, 4, 555]
# list1 = [5, 5, 5, 5]
# list1 = [-10, 5, 5]

# 1 step sum => arithmetic mean
sum = 0
for element in list1:
    sum += element
mean = int(sum / len(list1))
lengthToMean = abs(list1[0] - mean)  # довжина першого елементу до середнього арифметичного по модулю
nearest = 'something get wrong'
# 2 step find the nearest number to the arithmetic mean
for element in list1:
    length = abs(element - mean)
    if length <= lengthToMean:
        lengthToMean = length
        nearest = element
print(nearest)