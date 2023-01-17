# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку.
# (результаты всех преобразований выводить на экран).

str1 = b'r\xc3\xa9sum\xc3\xa9'
str1_new = str1.decode()
print(str1_new)

str_byte = str1_new.encode("Latin1")
print(str_byte)

str2 = str_byte.decode("Latin1")
print(str2)

