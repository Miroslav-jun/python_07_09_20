""" Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

proceeds = input("Введите значение выручки:")
cost = input("Введите значение издержки:")

if proceeds.isdigit() and cost.isdigit():
    proceeds = int(proceeds)
    cost = int(cost)

    if proceeds > cost:
        rentability = proceeds / cost
        numbers = input("Введите численность фирмы:")
        print(f"Прибыль =: {proceeds - cost}, Рентабельность =: {rentability}")

        if numbers.isdigit():
           proceeds_numbers = proceeds / int(numbers)
           print("Прибыль фирмы на одного сотрудника = %s" % proceeds_numbers)
        else:
            print("Неверно указана численность фирмы")
    elif cost > proceeds:
        print("Убыток = %s" % (cost - proceeds))


else:
    print("Введены неверные данные")