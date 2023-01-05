#Написать лямбда-функцию определяющую чётное/нечётное.
#Функция принимает параметр (число) и если чётное,
# то выдаёт слово “чётное”, если нет - то “не чётное”.
a = int(input('Enter your number: '))
lam = lambda a: print('Even number') if a%2 == 0 else print('Odd number')
lam(a)
