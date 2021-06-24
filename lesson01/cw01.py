option = str()
list = [{'name': 'turtle', 'price': 32}, {'name': 'rabbit', 'price': 89}, {'name': 'python', 'price': 999}]

while option != '9':
    option = input('1 Create note\n'
                   '2 List of all notes\n'
                   '3 Sum of all purchases\n'
                   '4 The most expensive purchase\n'
                   '5 Search by name of purchase\n'
                   '9 exit\n')
    if option == '1':
        name = input('enter the name of purchase\n')
        price = input('enter the price of purchase\n')
        purchase = dict([('name', name), ('price', int(price))])
        list.append(purchase)
    elif option == '2':
        print(list)
    elif option == '3':
        sum = 0
        for element in list:
            for k, v in element.items():
                if k == 'price':
                    sum = sum + v
        print(sum)
    elif option == '4':
        max = 0
        for element in list:
            for k, v in element.items():
                if k == 'price':
                    if v > max:
                        max = v
        print(max)
    elif option == '5':
        searchword = input('for correct searching enter the exact name of purchase: ')
        for element in list:
            for k, v in element.items():
                if k == 'name':
                    if v == searchword:
                        print(element)
    elif option == '9':
        print('thanks for attention')
    else:
        print('wrong option')