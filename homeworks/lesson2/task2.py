'''Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''


var_list = input('Введите значение:\n')
i = 0
if var_list.isdigit():
    var_list = list(var_list)
    max_list = int(var_list.index(max(var_list)))
    for items in var_list:
        if i == 0:
            items = var_list[1]
        elif i % 2 == 1 and i != max_list:
            items = var_list[i - 1]
        elif i % 2 != 1 and i != max_list:
            items = var_list[i + 1]
        else:
            items = var_list[max_list]
        i += 1
        print(items)
else:
    print('Не верно введены данные')





