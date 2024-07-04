"""Кормилина Александра Алексеевна, 4 вариант
Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
код задачи 16"""

def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sum_range(1, 5))
print(sum_range(5, 1))
print(sum_range(-3, 3))