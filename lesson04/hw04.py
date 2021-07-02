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
