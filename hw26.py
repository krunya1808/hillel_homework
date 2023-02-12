# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в
# степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
class Calculator():

    def sum(x, y):
        result = x + y
        return result

    def minus(x, y):
        result_2 = x - y
        return result_2

    def div(x, y):
        try:
            result_3 = x / y
            if y == 0:
                return result_3
            return result_3
        except ZeroDivisionError:
            return "Can`t div to zero!!!"

    def mnoz(x, y):
        return x * y

    def stepen(x, y):
        return x ** y

    def koren(x):
        try:
            if x < 0:
               return "Negative number"
            return x ** (0.5)
        except TypeError:
            return "Invalid type"


a_sum = Calculator.sum(2,5)
a_min = Calculator.minus(42,34)
a_div_zero = Calculator.div(2,0)
a_div = Calculator.div(20, 2)
a_mnoz = Calculator.mnoz(6, 7)
a_step = Calculator.stepen(4,3)
a_koren = Calculator.koren(25)
a_koren_neg = Calculator.koren(-25)

print(a_sum)
print(a_min)
print(a_div_zero)
print(a_div)
print(a_mnoz)
print(a_step)
print(a_koren)
print(a_koren_neg)




