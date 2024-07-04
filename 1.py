"""Кормилина Александра Алексеевна, 4 вариант
Декоратор умножающий на 2 результат выполнения функции
код задачи 4"""

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@decorator
def add(a, b):
    return a + b


print(add(3, 4))