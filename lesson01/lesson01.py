# print('hello world')

# print(1,2,3, sep='-', end=' finish')

# i=3
# f=1.2
# b=True #False
# s='some text'
# n= None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# print(i)
# print(f)
# print(b)
# print(n)

# a=b=c=10
# print(a,b,c)

a = 6
b = 4

# print(a+b)
# print(a-b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a*b)
# print(a**b)

# num = int(input('enter num: '))
# print(type(num))
# print(num)

# int(),float(),bool(),str()

# l1=list()
# l2=[]

l1 = [1, 2, 3, 4, 2, 5, -1]
#
# print(l1[3])
# del l1[3]
# print(l1)
#
# l1[0]=22
# print(l1)
# l1[23]=213
# print(l1)
#
# print(len(l1))
#
# l2 = l1.copy()
#
# l1.append(22)
# l1.insert(22,32)
#
# deleted = l1.pop()  # видаляє останній елемент і зразу записує в  змінну
# deleted = l1.pop(0) # видаляє елемент з індексом в масиві і зразу записує в  змінну
# print(deleted)
#
# l1.remove(2) # видаляє перше вказане число в списку (list), if doesnt exist will be exception
#
# l1.extend([22,33,44]) # add at the end of list
#
# print(l1.index(2))   # find in which first index is first '2'
# print(l1.index(2,3))   # start finding from 3 index
#
# l1.reverse()
#
# l1.sort()
# l1.sort(reverse=True)
#
# print(l1.count(2)) # count amount of '2' in list
#
# l1.clear() # clears the list
#
# print(l1)
#
# print(l1[-1])  # first starting from end
#
# print(l1[3:5])  # з третього по пятий не показуючи 5
# print(l1[:5])  # from 0 to 4
# print(l1[:5:2])  # every second element
# print(l1[::2])  # every second element FROM ZERO ELEMENT

# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a is b)
# print(a != b)
# print(a is not b)
# print(a is not b and 2>5)
# print(a is not b or 2>5)
# print(2 in [2, 3, 4, 56, 4])
# print(2 in [3, 4, 56, 4])  # boolean

# h=10
# if h>8:
#     print('h gt 8')
# else:
#     print('h lt 8')
#
# print('h gt 8') if h>8 else print('l lt 8')

# my_tuple = ('anna',25,25)   # tuple кортеж list that we cant change
# print(my_tuple.count(25))
# print(my_tuple.index(25))

# dictionary = {
#     'name':'vasya',
#     'age':32
# }
# print(dictionary['name'])
# print(dictionary.get('name1', 'Max'))
#
# popitem = dictionary.popitem()
# pop = dictionary.pop('name')
#
# print(dictionary)
# print(dictionary.items())
#
# d = dict([('name','petya'),('age', 33)])
# print(d)


# for i in range(10):
#     print(i)
#
# for i in l1:
#     print(i)
#
# for k,v in d.items():
#     print('key: ',k)
#     print('value: ',v)

# i=5
# while i>0:
#     print(i)
#     i-=1
# else:
#     print('end while')


myList = [{'name': 'trtrfd', 'price': 32}, {'name': 'turtle', 'price': 89}, {'name': 'regdgdsf', 'price': 324},
          {'name': 'jkdfjsdfsd', 'price': 545}]
# 3 Sum of all purchases
sum = 0
for element in myList:
    for k, v in element.items():
        if k == 'price':
            sum = sum + v
print(sum)
# 4 The most expensive purchase\n'
max = 0
for element in myList:
    for k, v in element.items():
        if k == 'price':
            if v > max:
                max = v
print(max)
# 5 Search by name of purchase\n'
searchword = input('for correct searching enter the exact name of purchase: ')
for element in myList:
    for k, v in element.items():
        if k == 'name':
            if v == searchword:
                print(element)