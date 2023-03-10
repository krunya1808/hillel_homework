#Используя input() ввести предложение состоящее из двух слов.
# Создать 2 переменные и в каждую записать по 1 введённому слову используя методы строк.
# Создать новую переменную 3-мя разными способами форматирования (фактически 3 переменные),
# которая бы состояла из введённых слов в обратном порядке, первое слово должно состоять только из больших букв,
# а второе с первой заглавной буквы и остальных маленьких. В начале предложения должен быть восклицательный знак,
# а в конце вопросительный.
#Используя только атрибуты функции print() вывести первоначальную строку и получившиеся разными способами форматирования
# через разделитель "<<<>>>", вывод сделать в файл.

a = input('Enter 2 words: ')
aa = a.split()
b = aa[0]
c = aa[1]
save_file = open('format_1_2_3.txt', 'w')

print('word1:', b, '\n''word2:', c, file=save_file)
print('<<<>>>' * 10, file=save_file)

b = b[::-1]
c = c[::-1]

format_1 = '!%s %s?' % (c.upper(), b.capitalize())
print(format_1, file=save_file)
print('<<<>>>' * 10, file=save_file)

format_2 = '!{} {}?'.format(c.upper(), b.capitalize())
print(format_2, file=save_file)
print('<<<>>>' * 10, file=save_file)

format_3 = f'!{c.upper()} {b.capitalize()}?'
print(format_3, file=save_file)
print('<<<>>>' * 10, file=save_file)

