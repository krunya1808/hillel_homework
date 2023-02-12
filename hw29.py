#1) Реалізувати функцію, яка порахує прибуток по таблиці invoice_items.
# Сума по замовленню = UnitPrice * Quantity. Прибуток = сумма замовлень.
# Якщо вирішуєте через sql, то необхідно для суми викрористати агрегатну функцію sum.
#2) Реалізувати функцію, которая виведе повторювані FirstName з таблиці customers і
# кількість їх входжень в таблицю. Результат має виглядати як:
#Марія 2 Микола 3.
#Тобто виводимо тільки ті імена, які повторюються більше одного разу.
#Якщо вирішуєте через sql, то використовуємо count та group by.
#Приймаються рішення як з допомогою python, так і з sql.

import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_employees() -> None:
    '''
    Функция получения всех записей из таблицы employees
    '''
    query_sql = '''
        SELECT *
          FROM employees;
    '''
    result = execute_query(query_sql)
    unwrapper(result)


#  get_employees()


def get_filter_customers(state=None, city=None) -> None:
    '''
    Функция для выбора клиентов по городу и штату
    '''
    query_sql = '''
    SELECT *
      FROM customers
    '''
    filter = ''
    if state and city:
        filter = f"WHERE State = '{state}' AND City = '{city}';"
    elif state:
        filter = f"WHERE State = '{state}';"
    elif city:
        filter = f"WHERE City = '{city}';"
    query_sql += filter
    result = execute_query(query_sql)
    unwrapper(result)


#  get_filter_customers(state='SP', city='São Paulo')
#  get_filter_customers(city='Prague')
#  get_filter_customers(state='SP')
#  get_filter_customers()


def get_unique_customers() -> Set:
    query_sql = '''
        SELECT FirstName
          FROM customers;
    '''
    names = execute_query(query_sql)
    unique_names = set()
    for name in names:
        unique_names.add(name[0])
    return len(unique_names)


#  result = get_unique_customers()
#  print(result)


def get_unique_customers_by_sql() -> Set:
    query_sql = '''
        SELECT count(distinct FirstName)
          FROM customers;
    '''
    unique_names_qty = execute_query(query_sql)[0][0]
    return unique_names_qty

#1) Реалізувати функцію, яка порахує прибуток по таблиці invoice_items.
# Сума по замовленню = UnitPrice * Quantity. Прибуток = сумма замовлень.
# Якщо вирішуєте через sql, то необхідно для суми викрористати агрегатну функцію sum.
def income_in_invoice_items() -> None:
    query_sql = '''
        SELECT *
          FROM invoice_items
          
        '''
    for item in query_sql:
        UnitPrice = 0, 99
        Quantity = 1
        sum_order = 0
        income = 0
        sum_order == UnitPrice * Quantity
        item += 1
        income = sum_order + sum_order
    print(income)

#2) Реалізувати функцію, которая виведе повторювані FirstName з таблиці customers і
# кількість їх входжень в таблицю. Результат має виглядати як:
#Марія 2 Микола 3.

def repeate_fname() -> Set:
    query_sql = '''
            SELECT FirstName
              FROM customers
            '''
    fname = execute_query(query_sql)
    print(fname)
    unique_name = set()
    n_name = 0
    for name in names:
        unique_name.add(name[0])
    return len(unique_name)

result = repeate_fname()
print(result)


result = get_unique_customers_by_sql()
print(result)