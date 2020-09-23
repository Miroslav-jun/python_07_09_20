"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("task2.txt", "r", encoding="UTF-8") as file:
        count = 0
        for itm in file:
            count += 1
            print("Количество слов в строке: %s"  % (len(itm.split())))
        print("Количество строк в файле: %s" % (count))
except IOError as f:
    print(f)
