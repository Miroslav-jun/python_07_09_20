'''Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.'''

var_str = input('Введите строку:\n')
var_str = list(var_str.split())
i = 0
for item in var_str:
    if len(item) > 10:
        item = item[0:10]
    else:
        item = item
    i = i + 1
    print(i, item)
