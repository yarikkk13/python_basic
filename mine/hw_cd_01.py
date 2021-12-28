# Завдання 1:
# Написати програму, що підраховує кількість цифр у введеному, як аргумент скрипта цілому числі N.
# При цьому не використовуєте оператор для визначення довжини рядка, користуйтесь
# математичними операціями.

def sum_1(number):
    if number > 0:
        return number % 10 + sum_1(number // 10)
    else:
        return 0


print(sum_1(123))

# Завдання 2:
# Вивести ряд Фібоначчі до N-того члена (числа Фібоначчі fn обчислюються за формулами
# f0=f1=1; fn=fn-1+fn-2 при n=2,3,... Числова послідовність Фібоначчі 1, 1, 2, 3, 5, 8, 13, ...).
# Значення вводиться як аргумент скрипта

f1 = f2 = 1

n = int(input())

print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

print('end')

# Завдання 3:
# Дано список який містить набір результати деяких вимірювань температури (як додатні, так і від’ємні значення). Знайти
# значення температури та її індекс, яка була ближча за все до 0. У результаті вивести кортеж, який містить значення
# температури найближчої до 0 та її індекс у списку. Список температур можна визначити у самому скрипті.

list1 = [12, 15, -4, 2, 10, -15]
lengthToZero = abs(list1[0])

for element in list1:
    length = abs(element)
    if length <= lengthToZero:
        lengthToZero = length
        nearest = element

index = list1.index(nearest)
myTuple = (nearest, index)
print(myTuple)
print(type(myTuple))

# Завдання 4 :
# Частина 1: Отримати список всіх дільників числа

num = 40
myList = []

for element in range(1, num + 1):
    roundedNum = int(num / element)
    if roundedNum == num / element:
        myList.append(element)

print(myList)

# Частина 2: Отримати список всіх простих дільників числа

lst = []
for i in myList:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)

# Число для якого шукаються дільники передається, як аргумент скрипта
