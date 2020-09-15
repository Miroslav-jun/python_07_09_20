"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

number = input("Введите число n:")

if number.isdigit():
    number_txt = str(number)
    number_sum = int(number_txt) + int(number_txt + number_txt) + int(number_txt + number_txt + number_txt)
    print("Полученное число: %s" % number_sum)
else:
    print("Неверно введено число")