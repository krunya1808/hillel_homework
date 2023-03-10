#Написать программу которая состоит из вечного цикла ожидающего ввод числа или одно из значений:
# "выход", "exit", "quit", "e" или "q" в любом регистре. При вводе одного из этих значений происходит
# выход из вечного цикла. При любом другом вводе вызывается отдельная функция которая умеет распознавать
# введённые числа. Сама функция ничего не распечатывает, она возвращает строку, типа:
# "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное число: Erdf"
# Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.
# Функция на вход принимает строку из ввода из вечного цикла. Анализирует её исключительно
# методом .isdigit() и другими методами строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же распознаёт
# десятичные дроби как с точкой, так и с запятой.
# Функция возвращает строку в которой описывается какое число введено - отрицательное или
# положительно, целое или дробное и выводит его или же сообщает, что введено не корректное число.
#*Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля

def detect_numbers(a):
    if a.isdigit():
        if int(a) == 0:
            return 'You enter 0!'
        elif int(a) > 0:
            return 'You enter whole positive number ' + a

    if a.isalnum() or a.isalpha():
        return 'Incorrect input:' + a

    if a.count('.') > 1 or a.count(',') > 1 or a.count('-') > 1:
        return 'You enter invalid number!'

    if a.find('-') != -1:
        if a.find(',') != -1 or a.find('.') != -1:
            if float(a) == -0.00:
                return 'You enter 0!'
            return 'You enter negative drob number ' + a
        return 'You enter negative whole number ' + a

    # if a.find(',') != -1 or a.find('.') != -1:
    #     float_val = float(a.replace(',', '.'))
    #     if float_val > 0:
    #         return 'You enter positive drob number ' + a
    #     float_val_s = str(float_val)
    #     if float_val_s.isalpha():
    #         return 'Incorrect input:'
    #     return 'You enter 0!'
    if a.find(',') != -1 or a.find('.') != -1:
        if float(a.isalpha()):
            print('Incorrect input:', a)
        return a











    # return 'Incorrect input:' + a
while True:
    a = input('Enter number or "выход", "exit", "quit", "e","q": ')
    a = a.lower()
    if a in ('выход', 'exit', 'quit', 'e', 'q'):
        print('Bye!')
        break
    else:
        print(detect_numbers(a))
