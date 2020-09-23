"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file_name = input('Название файла: ')
with open(file_name, "w", encoding="UTF-8") as file:
    while True:
        text = input()
        if text == '':
            break
        file.write(text + '\n')
