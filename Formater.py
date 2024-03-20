from functools import singledispatchmethod
class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    @format.register(int)
    @staticmethod
    def boo(data):
        print(f'Целое число: {data}')
    @format.register(float)
    @staticmethod
    def boo(data):
        print(f'Вещественное число: {data}')
    @format.register(tuple)
    @staticmethod
    def boo(data):
        print(f'Элементы кортежа: {', '.join(map(str, data))}')
    @format.register(list)
    @staticmethod
    def _(data):
        print(f'Элементы списка: {', '.join(map(str, data))}')
    @format.register(dict)
    @staticmethod
    def _(data):
        print(f'Пары словаря: {str(data.items())[12:-2]}')

Formatter.format(1337)
Formatter.format(20.77)