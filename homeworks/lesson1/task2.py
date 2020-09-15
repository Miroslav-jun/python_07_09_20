"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

time = input("Введите кол-во секунд:\n")

if time.isdigit():
    time = int(time)
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = (time % 3600) % 60
    print(f"hh: {hours}, mm: {minutes}, ss: {seconds}")
else:
    print("Неверно введено число")
