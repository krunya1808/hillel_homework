# Прочитать сохранённый csv-файл из задания №19
# и сохранить данные в excel-файл,кроме возраста – столбец с этими данными не нужен.

import csv
from openpyxl import Workbook

work_book = Workbook()
name_sheet = work_book['Sheet']
new_file = 'file.xlsx'
age_idx = False

with open('file.csv', encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file)
    for cs_idx, items in enumerate(file_reader):
        if 'Age' in items:
            age_idx = items.index('Age')
        if age_idx:
            del items[age_idx]
        for idx, item in enumerate(items):
            name_sheet.cell(row=idx + 1, column=cs_idx + 1, value=item)

work_book.save(filename=new_file)