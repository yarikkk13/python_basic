# def foo():
#     try:
#         return 1
#     finally:
#         return 2
#
#
# print(foo())
# class Person:
#     def __init__(self, id):
#         self.id=id
# obama = Person(100)
# obama.__dict__['age'] = 49
# print(obama.age + len(obama.__dict__))


#
# def dostuff(parm1, **parem3):
#     print(type(parem3))
#
# dostuff('capiats', Arizona = 'pjererd', California = 'fsdfsd')


#
# class Account:
#     def __init__(self,id):
#         self.id = id
#         id = 666
#
# acc = Account(123)
# print(acc.id)


#
# nam = ['fsdfsd','werwe']
# loc = nam.index('ddd')
# # print(loc)
#
# foo = {1:1, 2:2}
# foo = {}
# print(len(foo))


# print('\x48\x49!')

#
# import math
# print(math.floor(5.5))


#
# conter = 1
# def glo():
#     global conter
#     for i in (1,2,3):
#         conter+=1
#
# glo()
# print(conter)


# consfs = {}
# consfs[1] = 1
# consfs['1'] = 2
# consfs[1] +=1
#
# sum = 0
# for k in consfs:
#     sum += consfs[k]
#
# print(sum)


#
# num = [1,12,2,3]
# num.append([12,21,21])
# print(len(num))


#
# num = set([1,1,2,3,3,3,4])
# print(len(num))


# names = ['ddda','dadad','Chales','Dao']
#
# print(names[-1][-1])


#
# mu_tu = (1,2,3,4)
# mu_tu.append((5,5,6))
# print(len(mu_tu))


#
# print(0xA + 0xa)


# kvps = {'1':1,'2':2}
# thcoc = kvps.copy()
# kvps['1'] = 5
# sum = kvps['1']+ thcoc['1']
# print(sum
#
#

#
# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)


#
# variable = 5
# variable += 2
# print(variable)

# foo = {}
# print(type(foo))


# print(type(1J))


# x = True
# y = False
# z = False
#
# if x or y and z:
#     print('re')
# else:print('gg')


# print(type(lambda :None))


#
# name = "SoftServe IT  Academy"
# print(name.find("IT"))


#
# kvps = {'1':1, '2':2}
# thecop = dict(kvps)
# kvps['1'] = 5
# sicc = kvps['1']+thecop['1']
# print(sicc)
#
#
# one = chr(104)
# teo = chr(105)
# print(one+teo)

#
#
# name="SoftServe"
# print(name.title())

#
# def print_head(str):
#     print('+++' + str +'+++')
# category = 1
# text = 'some info'
# # print(print_head("{} and {}".format(category, text)))
# print_head("{} and {}".format(category, text))


list_first = [[11, 2, 3], [44, 5, 6], [10, 1, 2], [17, 8, 6]]


def findMaxSum(list_first):
    return sum(max(list_first, key =sum))


print(findMaxSum(list_first))
