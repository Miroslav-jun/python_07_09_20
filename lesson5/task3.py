"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
count = 0
salary = 0
try:
    with open("task3.txt", "r", encoding="UTF-8") as file:
        for itm in file:
            salary += float(itm.split()[1])
            count += 1
            if float(itm.split()[1]) < 20000:
                print("Сотрудник %s имеет оклад менее 20 тыс. руб" % (itm.split()[0]))
        try:
            print("Средняя доход сотрудников: %s" % (salary / count))
        except ZeroDivisionError:
            print("Деление на ноль!")
except FileNotFoundError:
    print("Файла не найден")