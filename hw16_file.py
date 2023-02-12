# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

s1 = input('Enter smt1: ')
s2 = input('Enter smt2: ')
s3 = input('Enter smt3: ')
s4 = input('Enter smt4: ')

my_file = open("File_string.txt", "w")
my_file.write(s1 + '\n' + s2 + '\n')
my_file.close()

my_file = open("File_string.txt", "a")
my_file.write(s3 + '\n' + s4)
my_file.close()