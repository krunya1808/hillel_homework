# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load» и снова пауза 1 сек.

# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
import time


class Auto(object):
    brand = None
    age = 0
    color = 'blue'
    mark = None
    weight = 1000

    def __int__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark
    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        print(self.age + 1)


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__int__(brand, age, mark)
        self.max_load = max_load
    def move(self):
        print('attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


truck_1 = Truck('BMW', 7, 'CX-3', 500)
truck_1.stop()
truck_1.move()
truck_1.load()
truck_1.birthday()
print('BRAND:', truck_1.brand)
print('AGE: ', truck_1.age)
print('COLOR: ', truck_1.color)
print('MARK: ', truck_1.mark)
print('WEIGHT: ', truck_1.weight)
print('MAX LOAD: ', truck_1.max_load)

print('-|-' * 30)

truck_2 = Truck('KIA', 5, 'rio', 450)
truck_2.stop()
truck_2.move()
truck_2.load()
truck_2.birthday()
print('BRAND:', truck_2.brand)
print('AGE: ', truck_2.age)
print('COLOR: ', truck_2.color)
print('MARK: ', truck_2.mark)
print('WEIGHT: ', truck_2.weight)
print('MAX LOAD: ', truck_2.max_load)

print('-|-' * 30)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        self.max_speed = max_speed
        self.age = age
        self.brand = brand
        self.mark = mark

    def move(self):
        print('move')
        print('max speed is', self.max_speed)


car_1 = Car('Nissan', 9, 'Micro', 170)
car_1.move()
car_1.stop()
car_1.birthday()
print('BRAND:', car_1.brand)
print('AGE: ', car_1.age)
print('COLOR: ', car_1.color)
print('MARK: ', car_1.mark)
print('WEIGHT: ', car_1.weight)
print('MAX SPEED: ', car_1.max_speed)

print('-|-' * 30)

car_2 = Car('Suzuki', 3, 'SX4', 220)
car_2.move()
car_2.stop()
car_2.birthday()
print('BRAND:', car_2.brand)
print('AGE: ', car_2.age)
print('COLOR: ', car_2.color)
print('MARK: ', car_2.mark)
print('WEIGHT: ', car_2.weight)
print('MAX SPEED: ', car_2.max_speed)
