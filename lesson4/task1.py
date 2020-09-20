"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

def salary_calc(working_hour: float, rate_hour: float, premium: float) -> float:
    '''
    salary return
    :param working: float
    :param rate_hour: float
    :param premium: float
    :return: float
    '''
    return (working * rate_hour) + premium
try:
    _, working, rate, premium = sys.argv
    print(f"f Запрлата сотрудника: {salary_calc(working_hour, rate_hour, premium)}")
except ValueError as a:
    print('Неверно укзаны данные')