"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""

number = input("Введите число:")
number_itog = -1

if number.isdigit():
    while number:
        number = int(number)
        tmp = number % 10
        number = int(number) // 10
        if tmp > number_itog:
            number_itog = tmp
    print(number_itog)