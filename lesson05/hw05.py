# Переделываем практическую:
#
# -Должен быть класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в файл
#
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

import json

list_of_letters = []


class Notepad:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.__dict__)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.price = new_price

    def push_method(self):
        list_of_letters.append(self.__dict__)

    @staticmethod
    def show_the_list():
        return list_of_letters

    @staticmethod
    def find_purchase(search_word):
        for element in list_of_letters:
            for k, v in element.items():
                if k == 'name':
                    if v == search_word:
                        return element

    @staticmethod
    def find_max():
        max_price = 0
        for element in list_of_letters:
            for k, v in element.items():
                if k == 'price':
                    if v > max_price:
                        max_price = v
        return max_price

    @staticmethod
    def find_sum():
        sum_of_items = 0
        for element in list_of_letters:
            for k, v in element.items():
                if k == 'price':
                    sum_of_items = sum_of_items + v
        return sum_of_items


note = Notepad('phone', 13)
note1 = Notepad('iphone', 13)
note2 = Notepad('get d', 13)
note3 = Notepad('toy', 13)
note4 = Notepad('apple', 13)

print(note)
note.push_method()
note1.push_method()
note2.push_method()
note3.push_method()
print(Notepad.show_the_list())
note4.set_price(45)
note4.push_method()
print(list_of_letters)
print(Notepad.find_purchase('apple'))
print(Notepad.find_max())

option = str()
while option != '9':
    option = input('1 Create note\n'
                   '2 List of all notes\n'
                   '3 Sum of all 9purchases\n'
                   '4 The most expensive purchase\n'
                   '5 Search by name of purchase\n'
                   '9 exit\n')
    if option == '1':
        with open('notepad.json', 'r') as file:
            list_of_letters = json.load(file)
        exact_name = input('enter the name of purchase\n')
        exact_price = input('enter the price of purchase\n')
        Notepad(exact_name, int(exact_price)).push_method()
        with open('notepad.json', 'w') as file:
            json.dump(list_of_letters, file)
    elif option == '2':
        with open('notepad.json', 'r') as file:
            list_of_letters = json.load(file)
        print(Notepad.show_the_list())
    elif option == '3':
        with open('notepad.json', 'r') as file:
            list_of_letters = json.load(file)
        print(Notepad.find_sum())
    elif option == '4':
        with open('notepad.json', 'r') as file:
            list_of_letters = json.load(file)
        print(Notepad.find_max())
    elif option == '5':
        with open('notepad.json', 'r') as file:
            list_of_letters = json.load(file)
        exact_word = input('for correct searching enter the exact name of purchase: ')
        print(Notepad.find_purchase(exact_word))
    elif option == '9':
        print('thanks for attention')
    else:
        print('wrong option')
