"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def my_sum(var_1, var_2, var_3):
    result = [var_1, var_2, var_3]
    result.remove(min(result))
    return sum(result)

print(my_sum(43, 55, 22))