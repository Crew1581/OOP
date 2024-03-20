from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(float)
    @process.register(int)
    @staticmethod
    def _numeric_process(data):
        return 2 * data

    @process.register(str)
    @staticmethod
    def _str_process(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _list_process(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _tuple_process(data):
        return tuple(sorted(data))
