# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[::2])

# print('.1'.isnumeric())

# s = 'Hello World!'
# print(s[-1:0:-1])

# x = 10
# def func_1():
#     x = 20
#     def func_2():
#         nonlocal x
#     x = 30
#     x = 40
#     func_2()
# func_1()
# print(x)

#
# i = 0
# while True:
#     i += 2
#     print(i)
#     if i == 0: break


# print(list(dict(foo='bar', baz=2)))


# s = 'Hello World!'
# print(s[3:-3])
# print(s[:])


# class A:
#     def __init__(self):
#         self.greetings = f'Hello'
#
#     def greetings(self):
#         return f'Hello,world'
# obj = A()
# print(obj.greetings)


# x = [0]*10
# print(x)


# void function(int n){
#     int i,j,count=0;
#     for(i=n;i>0;i--)
#         for(j=1;j<=n;j++)
#             count++;
# }

# a, b = '',''
# c, d = (), ()
# e, f = [], []
# print(id(a) == id(b), id(c) == id(d), id(e) == id(f))


# a = (('john',40),('peter',45))
# b = dict(john=40,peter= 45)
# c = {}
# d = {40:'john',45:'peter'}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# y = [i + j for i in range(0, 5) for j in range(0, 2)]
# print(y)
# print(len(y))


# print('a b c'.split())


# s1 = {1, 2, 3, 4}
# s2 = {1, 3, 5, 7}
# y = s1|s2
# print(len(y))


# a = {'jack': 4098, 'sjierd': 4127}
# b = {4098: 'jack', 4127: 'sjierd'}


# print(a > b)

# s1 = {1, 2, 3, 4}
# s2 = {1, 3, 5, 7}
# y = s1 & s2
# print(y)


test = 77
if test >= 70:
    print("You have passed")
else:
    print("You have not passed")
