# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto(object):
    brand = "Toyota"
    age = 4
    color = "blue"
    mark = "Prius"
    weight = 100

    def __int__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark
    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        print(self.age + 1)


car_1 = Auto()
car_1.stop()
car_1.move()
car_1.birthday()
