# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#
# user = User('Max')
# print(user.get_name())
# print(user.__name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __delete_name(self):
#         del self.__name
#
#     my_name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
# user.my_name = 'Vasia'
# del user.my_name
#
# print(user.my_name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Vasia'
# del user.name
#
# print(user.name)
#
# class Shape:
#     def area(self):
#         print('Area')
#
#     def perimeter(self):
#         print('Perimeter')
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         super().area()
#         return self.a * self.b * self.c
#
#     def perimeter(self):
#         super().perimeter()
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         super().area()
#         return self.a * self.b
#
#     def perimeter(self):
#         super().perimeter()
#         return self.a + self.b
#
#
# triangle = Triangle(1, 2, 3)
# rectangle = Rectangle(5, 6)
# print(triangle.area())
# print(triangle.perimeter())
# print()
# print(rectangle.area())
# print(rectangle.perimeter())


# shapes = [triangle, rectangle]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())

#
# from abc import ABC, abstractclassmethod
#
#
# class Shape(ABC):
#     @abstractclassmethod
#     def area(self):
#         pass
#
#     @abstractclassmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         super().area()
#         return self.a * self.b
#
#     def perimeter(self):
#         super().perimeter()
#         return self.a + self.b
#
#
# # shape = Shape()
# triangle = Triangle(1, 2, 3)
# rectangle = Rectangle(5, 6)
#
# shapes = [triangle, rectangle]
#
# for i in shapes:
#     print(i.perimeter())

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __len__(self):
#         return len(self.name)
#
#     def __add__(self, other):
#         return f'{self.name}-{other.name}'
#
#     def __sub__(self, other):
#         return self.age + other.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#
# user = User('Max', 20)
# user2 = User('Karina', 16)
# print(user)
# print(len(user))
#
# print(user+user2)
# print(user-user2)
# print(user<user2)
# print(user>user2)


class User:
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.__count += 1

    def get_name(self):
        return self.name

    @staticmethod
    def greeting():
        print('Hello')

    @classmethod
    def get_count(cls):
        return cls.__count


user = User('Max', 33)
user2 = User('Max', 33)
user3 = User('Max', 33)

# print(user.get_count())
print(User.get_count())