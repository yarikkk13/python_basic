"""1)создать два класса Prince и Cinderella:
у золушки должно быть имя возраст и размер ноги
у принца имя, возраст и размер найденой туфельки,
так же должен быть метод который принимает лист золушек и ищет ту самую

2) максимально в этих двух классах проанотировать типы

3) у класса золушки должна быть переменная count которая
будет считать сколько экземпляров класса золушка было создано"""


class Cinderella:
    count: int = 0

    def __init__(self, name: str, age: int, foot: int):
        self.name = name
        self.age = age
        self.foot = foot
        Cinderella.count += 1

    def __str__(self):
        return f'Cinderella({self.name} - {self.age} - {self.foot})'

    def __repr__(self):
        return self.__str__()


class Prince:
    def __init__(self, name: str, age: int, shoes: int):
        self.name = name
        self.age = age
        self.shoes = shoes

    def find_cinderella(self, list_cinds: list[Cinderella]) -> str:
        for c in list_cinds:
            if c.foot == self.shoes:
                return c.name


cindi1 = Cinderella('Anna', 18, 33)
cindi2 = Cinderella('Tonya', 25, 38)
cindi3 = Cinderella('Emma', 19, 36)
cindi4 = Cinderella('Luiza', 20, 39)
cindi5 = Cinderella('Victory', 29, 40)

cinderellas = list()
cinderellas.append(cindi1)
cinderellas.append(cindi2)
cinderellas.append(cindi3)
cinderellas.append(cindi4)
cinderellas.append(cindi5)
prince1 = Prince('petya', 12, 36)
print(prince1.find_cinderella(cinderellas))
