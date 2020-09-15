'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_fall = [9, 10, 11]

dict_season = {'Лето':list_summer, 'Зима': list_winter, 'Весна': list_spring, 'Осень': list_fall}
number_season = input('Введите месяц года:\n')
err = 'Не найдено время года!'

print(dict_season)

if number_season.isdigit():
    for key, values in dict_season.items():
        is_season = int(number_season) in values
        name_season = key
        if is_season:
            break
    print(key)

else:
    print('Неверный формат ввода!!')

