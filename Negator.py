from functools import singledispatchmethod
class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def int_float_to_neg(data):
        return data *(-1)
    @neg.register(bool)
    @staticmethod
    def boot_to_neg(data):
        if data:
            return False
        else:
            return True

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
