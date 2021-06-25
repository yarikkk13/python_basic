# # l = [1, 2, 3, 4, 2, 1]
# # s = set()
# #
# # s.add(2)
# # s.add(2)
# # s.add(3)
# # s.add(4)
# # s.add(5)
# #
# # print(s)
#
# # s = {1, 2, 2, 3, 4, 5}
# # s = set(l)
# # s.
#
# set1 = {1, 2, 3, 4,10,11}
# set2 = {5, 6, 7, 8, 11}
# print(set1.issuperset(set2))
# print(set1.issubset(set2))
# print(set1.isdisjoint(set2))
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# set1.remove(100)
# set1.discard(10)
# pop = set1.pop()
# print(set1)
# print(pop)

# name = 'Max'
# age = 15
# weight = 60

# string = 'Hello, my name is Max, I`m 18 and my weight 70.5kg'
# string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight is ' + str(weight) + ' kg'
# string = 'Hello, my name is %s, I`m %d and my weight %d kg' % (name, age, weight)

# string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)

# string = 'Hello, my name is {}, I`m {} and my weight {} kg'
# string = string.format(name, age, weight)

# string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, name=name,  weight=weight)

# string = f'Hello, my name is {name}, I`m {age} and my weight {weight} kg'
# print(string)

# print(string[::-1])
# print(string.index('b'))
# print(string.find('l'))
# print(string.count('l'))
# print(string.capitalize())
# print(string.upper())
# print(string.islower())
# print(string.isupper())
# print(string.title())
# print(string.swapcase())
# print(string.isalpha())
# print(string.isdigit())
# print(string.startswith('hel'))
# print(string.endswith('hel'))
# string = 'hello is world'
# print([string.strip('a')])
# print([string.rstrip('a')])
# print([string.lstrip('a')])
# print(string.split(' '))
# print(string.partition('is'))

# print(' '.isspace())
# print(string.replace('ll', 'LL'))

# l =['hello', 'is', 'world']
#
# print(' '.join(l))

# print(min([3, 1, 4, 3, 5, 3]))
# print(max(3, 1, 4, 3, 5, 3))
# l = sorted([3, 1, 4, 3, 5, 3], reverse=True)
# print(pow(2, 2))
# # print(l)
########################################################
# list comprehension
########################################################

# l = [i for i in range(10)]
# l =[]
# for i in range(10):
#     l.append(i)

# l = [i**2 for i in range(10) if i % 2 == 0]
# print(l)

# l = [[1, 2, 3, 4, 5], [11, 22, 33, 44, 55]]

# new_l = [i for j in l for i in j]
# new_l = []
# for j in l:
#     for i in j:
#         new_l.append(i)
# print(new_l)

# dict_ = {
#     'NamE': 'Max',
#     'aGe': 15,
# }


# new_dict = {k.lower(): v for k, v in dict_.items()}
# new_dict = {}
# for k, v in dict_.items():
#     new_dict[k.lower()] = v
# print(new_dict)


"""
functions
"""


# def func(a, c, v=4, *args, **kwargs):
#     print(a, v, c)
#     print(args)
#     print(kwargs)
#
#
# func(10, 11, 12, 12, 45, 87, name='Max', age=15)

def decor(func):
    def wrap(*args, **kwargs):
        print('*****************************')
        func(*args, **kwargs)
        print('*****************************')

    return wrap


# @decor
@decor
def greeting(name):
    print('Hello ' + name)

greeting('Max')