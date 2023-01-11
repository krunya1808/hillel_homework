#Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
from datetime import datetime
import time


def decor_time_execute(func):
    def wrapper():
        time_start = datetime.now()
        print("time_now: ", time_start)
        func()
        print("time_execution: ", datetime.now() - time_start)
    return wrapper


@decor_time_execute
def sum(a=4, b=3):
    time.sleep(2)
    print(a + b)


@decor_time_execute
def hello(name="Mark!"):
    time.sleep(3)
    print("Hello ", name)


sum()
print("-" * 40)
hello()
