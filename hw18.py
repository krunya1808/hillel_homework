# Созадать словарь в качестве ключа которого будет 6-ти значное число,
# а в качестве значений кортеж состоящий из 2-х элементов – имя(str), возраст(int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.

import json
import random
v_name = ['Nina', 'Zina', 'Anna', 'Alex', 'Mark', 'David' ]
v_age = ['20', '13', '55', '34', '58', '23']
created_dict = {random.randint(123456, 654321): i for i in zip(v_name, v_age)}
with open('dict.json', 'w') as f:
    json.dump(created_dict, f)