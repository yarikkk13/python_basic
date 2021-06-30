# tuple1 = (1, 2)
#
# a, b = tuple1
# print(a, b)
#
# # l = [1, 2, 3, 4, 5, 6]
#
# # a,b,*_,z = l
# # print(_)
# # print(a,b,z)
#
# l = [1, 2, 4]
#
# a, _, c = l
# print(a,b)

# def func(arg1='a', arg2='b', arg3='c'):
#     return (arg1, arg2, arg3)
#
#
# d = {
#     "arg1": 1,
#     "arg2": 2,
#     "arg3": 3,
# }
# print(func(1,2,3))
# print(func(*d)) #func(arg1, arg2, arg3) ?
# print(func(**d)) #func(1, 2, 3) ?

#####################################################################################


# print(locals())
# print()
# print(globals())
# print(name)

# name = 'Max'
#
#
# def a():
#     # name = 'Vasia'
#
#     def b():
#         nonlocal name
#         name = 'Petia'
#         print(name)
#
#     b()
#     print(name)
#
#
# a()
# print(name)


#####################################################################################

# def counter():
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         return count
#     return wrap
#
#
# count1 = counter()
# count2 = counter()
#
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# print(count2())
# print(count1())
# print(count2())
# print(count1())
# print(count1())
# print(count1())

#####################################################################################

# func = lambda x,y: x+y

# const func = (x,y)=>x+y

# print(func(1,2))
# l = [1, 2, 3, 4, 5]
# map1 = map(lambda x: x ** 2, l)
# for item in map1:
#     print(item)
# print(list(map1))
#
# print(list(filter(lambda x: x < 4, l)))

#####################################################################################
# string = 'Hello'
# string.
from typing import List, Tuple, Optional, Union, Callable


# def splitter(st: str, ch: str) -> Union[tuple[str,...], list[int]]:
#     return [111,222]
#
#
# splitter("Hello world", ' ')

# def counter() -> Callable:
#     count = 0
#
#     def wrap() -> int:
#         nonlocal count
#         count += 1
#         return count
#
#     return wrap
#
#
# print(globals())


#####################################################################################

# print('4'*55)

# class User:
#     __count = 0
#
#
#
#
# user = User()
# user2 = User()
# User.count = 100
# print(User._User__count)  #how to get private variable in Class
# print(user2.__count)


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # def __str__(self):
    #     return f'User({self._name} - {self._age})'
    #
    # def __repr__(self):
    #     return self.__str__()

    def get_name(self):
        return self._name


user1 = User('Max', 15)
# print(user1.get_name())
l = [User('Max', 15), User('Max2', 15), User('Max3', 15)]
print(l)

d = {
    user1: 2
}

print(d)
