# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
option = int()

while option != 5:
    list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    option = int(input('1 Find minimal number in list\n'
                       '2 delete all similar values\n'
                       '3 replace all 4th value in list\n'
                       '4 show the nearest element of list\n'
                       '5 exit\n'))
    if option == 1:
        smallestNum = list[0]
        for i in list:
            if smallestNum > i:
                smallestNum = i
        print(smallestNum)
    elif option == 2:
        length = len(list)
        while length > 0:
            if list.count(list[length - 1]) > 1:
                list.remove(list[length - 1])
            length -= 1
        print(list)
    elif option == 3:
        i = 0
        length = len(list)
        while i < length:
            if i % 4 == 0 and i > 0:
                list[i - 1] = 'x'
            i += 1
        else:
            print(list)
    elif option == 4:
        sum = 0
        for element in list:
            sum += element
        mean = int(sum / len(list))
        lengthToMean = abs(list[0] - mean)
        nearest = 'something get wrong'
        for element in list:
            length = abs(element - mean)
            if length <= lengthToMean:
                lengthToMean = length
                nearest = element
        print(str(nearest) + ' is the nearest element')
    elif option == 5:
        print('thanks for attention')
    else:
        print('wrong option')