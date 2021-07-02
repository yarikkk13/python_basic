""" Создать класс Rectangle:
    -конструктор принимает две стороны x,y
    -описать арифметические методы:
    + сума площадей двух экземпляров класса
    - разница площадей
    == или площади равны
    != не равны
    >, < меньше или больше
    при вызове метода len() подсчитывать сумму сторон"""


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __sub__(self, other):
        return self.x * self.y - other.x * other.y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

    def __ne__(self, other):
        return self.x * self.y != other.x * other.y

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __len__(self):
        return 2 * (self.x + self.y)


r1 = Rectangle(10, 15)
r2 = Rectangle(10, 12)
# print(r1 + r2)
# print(r1 - r2)
# print(r1 == r2)
# print(r1 != r2)
# print(r1 < r2)
# print(r1 > r2)
# print(len(r1))

""" 1) написати програму для запису відомостей про пасажирські перевезення
    2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
    3) дані які треба буде зберігати:
      - вартість квитка(літак, поїзд)
      - кількість пасажирів(машина)
      - час в дорозі(всі)
      - час реєстрації(літак)
      - клас:перший,другий(літак)
      - вартість пального(машина)
      - км(машина)
      - місце: купе,св(поїзд)
    4) методи:
     - розрахунок вартості доїзду(машина)
     - загальний час перельоту(літак)
     - порівняти час в дорозі між двома будь якими транспортними засобами(двома обєктами) - наприклад 
       "літак на 5 годин швидше за поїзд"
     - вивести всі дані про перевезення(поїзд) """


class Transport:
    def __init__(self, time, name):
        self.time = time
        self.name = name

    def comparison(self, other):
        if self.time < other.time:
            print(f'{self.name} is faster for {other.time - self.time} hours than {other.name}')
            return self.time - other.time
        elif self.time > other.time:
            print(f'{other.name} is faster for {self.time - other.time} hours than {self.name}')
            return other.time - self.time
        else:
            print('they are both as fast as possible')
            return 0


class Car(Transport):
    def __init__(self, passengers, time, fuels_price, km, name='car'):
        super().__init__(time, name)
        self.passengers = passengers
        self.time = time
        self.fuels_price = fuels_price
        self.km = km
        self.name = name

    def cost(self):
        return self.fuels_price * self.km

    def comparison(self, other):
        super().comparison(other)


class Plane(Transport):
    def __init__(self, fee, time, registration, travel_class, name='plane'):
        super().__init__(time, name)
        self.fee = fee
        self.time = time
        self.registration = registration
        self.travel_class = travel_class
        self.name = name

    def general_time(self):
        return self.registration + self.time

    def comparison(self, other):
        super().comparison(other)


class Train(Transport):
    def __init__(self, fee, time, place, name='train'):
        super().__init__(time, name)
        self.fee = fee
        self.time = time
        self.place = place
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def comparison(self, other):
        super().comparison(other)


car1 = Car(2, 5, 12, 123, 'chevrolet')
car2 = Car(2, 10, 12, 123, 'zaz')
train1 = Train(150, 24, 'upper', 'UZ')
train2 = Train(450, 3, 'lux', 'Hyundai')
plane1 = Plane(1200, 3, 2, 2, 'mau')
plane2 = Plane(2400, 1, 1, 1, 'boeing')
print(car1.cost())
print(plane1.general_time())
print(train1)
car1.comparison(car2)
car2.comparison(train2)
train1.comparison(plane1)
plane2.comparison(car1)

""" 1)Створити пустий list
    2)Створити клас Letter
    3) створити змінну класу __count.
    4) при створенні обєкта має створюватись змінна обєкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
    5) при створені обєкта __count має збільшуватися на 1
    6) має бути метод(метод класу) для виводу __count
    7) має бути метод який записує в наш ліст текст з нашої змінної __text """

list_of_letters = []


class Letter:
    __count = 0

    def __init__(self, text):
        self.__text = text
        Letter.__count += 1

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        self.__text = new_text

    @classmethod
    def get_count(cls):
        return cls.__count

    def push_method(self):
        list_of_letters.append(self.__text)

# let1 = Letter('1233455124')
# let1.push_method()
# print(Letter.get_count())
# let1.set_text('new_text')
# print(let1.get_text())
# print(list_of_letters)
