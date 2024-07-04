class A:
    '''Класс A
    Устанавливает значение атрибута a
    Возвращает значение атрибута a'''
    def set_a(self, value):
        self.a = value
    def get_a(self):
        return self.a


class B:
    '''Класс B
    Инициализирует атрибут b
    Возвращает значение атрибута b'''
    def __init__(self, b):
        self.b = b
    def get_b(self):
        return self.b


class C(A, B):
    '''Класс C = A + B
    Инициализирует атрибуты a, b и c
    Параметры:
    a: Значение атрибута a
    b: Значение атрибута b
    c: Значение атрибута c'''
    def __init__(self, a, b, c):
        super().__init__(b)
        self.a = a
        self.c = c

    def set_b(self, value):
        self.b = value
    def set_c(self, value):
        self.c = value
    def get_c(self):
        return self.c


class D:
    '''Класс D
    Выводит на экран словарь атрибутов переданного объекта
    Выводит на экран словарь атрибутов класса'''
    @staticmethod
    def stat_print_dict(obj):
        print(obj.__dict__)

    @classmethod
    def cls_print_dict(cls):
        print(cls.__dict__)


# Примеры использования
c_instance = C(a=1, b=2, c=3)

print(c_instance.get_a())
print(c_instance.get_b())
print(c_instance.get_c())

D.stat_print_dict(c_instance)
D.cls_print_dict()