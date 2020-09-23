"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
file_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("task4.txt", "r", encoding="UTF-8") as file:
        for itm in file:
            file_str = file_dict.get(itm.split()[0]) + " " + itm.split()[2]
    with open("task4_new.txt", "w", encoding="UTF-8") as file_1:
        file_1.write(file_str)
except FileNotFoundError:
    print("Файл не найден")