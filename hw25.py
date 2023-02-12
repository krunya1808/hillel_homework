# Создайте свой произвольный класс и в нём помимо обычных методов
# и атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.
class RandomClass():
    time = 3
    clock = 1020

    def __init__(self,price,item):
        RandomClass.clock += 20
        self.price = price
        self.item = item
        print("The", item, price, "hrn")

    @staticmethod
    def static_one():
        print("Simple static method")

    @staticmethod
    def static_two():
        a = 10
        if a > 0:
            return a

    @classmethod
    def shop_time(cls):
        print("Shop times/week: ", cls.time)

    @classmethod
    def shop_clock(cls):
        print("Go to shop at: ", cls.clock)


a_1 = RandomClass(25,"apples")
a_2 = RandomClass.static_two()
print(a_2)
a_3 = RandomClass.shop_time()
a_4 = RandomClass.shop_clock()