class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def from_iterable(cls, lst):
        if len(lst) == 3:
            return cls(lst[0], lst[1], lst[2])
    @classmethod
    def from_str(cls, s):
        cls.s = s.split()
        return cls(float(cls.s[0]), float(cls.s[1]), float(cls.s[2]))
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)