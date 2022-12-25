#1. Создать 3 переменные одного и тоже типа с одинаковыми данными и с одинаковым id.
#2. Создать 2 переменные одного и тоже типа с одинаковыми данными и с разными id.
#3*. Поменять их типы так, чтобы у 1-х трёх стали разные id, но при этом остались одинаковые данные (и одинаковый тип), а у 2-х последних стали одинаковые id и остались одинаковые данные (и одинаковый тип).

a = b = c = 333
print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(type(c))
print(id(c))

a = (a, )
b = (b, )
c = (c, )
print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(type(c))
print(id(c))

a1 = [1, 2, 3]
a2 = [1, 2, 3]
print('a1_type: ', type(a1))
print(id(a1))

print('a2_type: ', type(a2))
print(id(a2))


a1 = set(a1)
a2 = a1
print('new_a1_type: ', type(a1))
print('new_a1: ', id(a1))

print('new_a2_type: ', type(a2))
print('new_a2: ', id(a2))



