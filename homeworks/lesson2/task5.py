'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.'''


my_list = [7, 5, 3, 3, 2]

list_value = input('Введите значение:\n')
if list_value.isdigit():
    list_value = int(list_value)

    if list_value in my_list:
        my_list.insert(my_list.index(list_value), list_value)
    else:
        my_list.append(list_value)
    print(my_list)
else:
    print('Неверное значение')
