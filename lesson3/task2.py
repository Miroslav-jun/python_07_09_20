"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def my_user(name, email, town, year_birth, surname, phone):
    return(f"Имя - {name}, Фамилия - {surname}, год рождения - {year_birth}, город проживания -"
           f" {town}, email - {email}, phone - {phone}")

print(my_user(name = input('Имя:\n'), surname = input('Фамилия:\n'), year_birth = input('Год '
                                                                                        'рождения:\n'),town = input(
    'Город проживания:\n'), email = input('email:\n'), phone = input('Телефон:\n')))