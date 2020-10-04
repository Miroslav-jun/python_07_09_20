"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

from random import randint


class Car:
    speed = 10
    color = 0x00
    name = "base_car"
    is_police = False
    _curr_speed = 0

    def go(self):
        self._curr_speed = self.speed
        print("машина поехала")

    def stop(self):
        self._curr_speed = 0
        print("машина остановилась")

    def turn(self, direction_angle):
        print(f"машина повернула на {direction_angle} град.")

    def show_speed(self):
        print(f"скорость - {self.speed}")


class TownCar(Car):
    def __init__(self):
        self.name = self.__class__.__name__
        self.color = 0x020202
        self.speed = 70
        self.max_speed = 60

    def show_speed(self):
        super().show_speed()
        if self._curr_speed > self.max_speed:
            print("превышение скорости!!!"
                  f"max - {self.max_speed} current - {self._curr_speed}")


class SportCar(Car):
    def __init__(self):
        self.name = self.__class__.__name__
        self.color = 0x040404
        self.speed = 120


class WorkCar(Car):
    def __init__(self):
        self.name = self.__class__.__name__
        self.color = 0x060606
        self.speed = 60
        self.max_speed = 40

    def show_speed(self):
        super().show_speed()
        if self._curr_speed > self.max_speed:
            print("превышение скорости!!!"
                  f"max - {self.max_speed} current - {self._curr_speed}")


class PoliceCar(Car):
    def __init__(self):
        self.name = self.__class__.__name__
        self.color = 0x080808
        self.speed = 100
        self.is_police = True


cars = list()
cars.append(TownCar())
cars.append(SportCar())
cars.append(WorkCar())
cars.append(PoliceCar())


for car in cars:
    print("*" * 25)
    print(f"name - {car.name}")
    print(f"color - {car.color}")
    print(f"is police - {car.is_police}")
    car.go()
    car.show_speed()
    car.turn(randint(0, 360))
    car.stop()

