# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# """
st = 'as 23 fdfdg544'
list_of = [i for i in st]
list_of_st = {}
i = 0
while i < len(list_of):
    # print(list_of[i])
    # print(list_of.count(list_of[i]))
    list_of_st[list_of[i]] = list_of.count(list_of[i])
    i += 1
print(list_of_st)
for k, v in list_of_st.items():
    print(f"'{k}' -> {v}")

"""second way of solving is in list_comprehension.py"""

# list comprehension
#
# 1)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
# пример:
# ['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = ['GT' if element > 4 else 'LT' for element in numbers]
print(new_list)

# 2) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
# записать в лист тюплы (x,y) если x+y == 0
# пример:
# [(1, -1), (2, -2), (5, -5)]
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
new_list3 = [(x, y) for x in list1 for y in list2 if (x + y) == 0]
print(new_list3)
