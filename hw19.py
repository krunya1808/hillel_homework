# Прочитать сохранённый json-файл из задания №18
# и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import json
import csv
import random

with open('dict.json') as ndict:
    new_data = json.load(ndict)


name_of_fields = ['', 'Id', 'Name', 'Age', 'Phone']

if len(name_of_fields) > 0:
    fields = []
    counter = 0
    for item in new_data:
        value = new_data[item]
        value.insert(-len(value), item)
        counter += 1
        value.insert(0, f'# {counter}')
        num = str(random.randint(8095, 999999999)).zfill(9)
        value.insert(len(value) + 1, num)
        fields.append(value)

    with open('data_csv.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow(name_of_fields)
        for item in fields:
            file_writer.writerow(item)