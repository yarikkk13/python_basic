"""перше завдання практичної"""
# st = 'as 23 fdfdg544'
# for ch in st:
#     count = st.count(ch)
#     print(f"'{ch}' -> {count}")
#     st = st.replace(ch, '')

"""
#################################################################################
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
#################################################################################
"""
st = 'as 23   fdf55dg544 34 34 !!!1!!'
result = ''
for ch in st:
    if ch.isdigit():
        result += ch
    else:
        result += ' '
print(result)
# result += ch if ch.isdecimal() else " "
result = ', '.join(result.split())
print(result)

# - створити функцію яка виводить ліст
l = [1, 2, 3, 4, 5]


def list_func(l):
    for i in range(len(l)):
        print(f'{i} -> {l[i]}')


list_func(l)

"""   
-функція: def pr(): return 'Hello_boss_!!!'
 написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення
"""


def decor(func):
    def wrap():
        return func().replace('_', ' ')

    return wrap


@decor
def pr():
    return 'Hello_boss_!!!'


print(pr())
