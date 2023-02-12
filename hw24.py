# Создать свой класс String на базе стандартного класса str.
# В нём необходимо:
# переопределить стандартный метод отвечающий за сложение
# написать отсутствующий в классе str метод отвечающий за вычитание
class String(str):
    def __add__(self, other):
        if isinstance(other, str):
            return String(str(self) + other)
        else:
            return String(str(self) + str(other))

    def __sub__(self, other):
        return String(str(self).replace(other, ''))


s1 = String("Hello ")
s2 = "world!"
s3 = s1 + s2
print(s3)

s4 = String("Hello world")
s5 = s4 - "o"
print(s5)


