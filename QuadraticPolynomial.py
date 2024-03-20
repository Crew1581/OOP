class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def x1(self):
        if (self.b**2 - 4*self.a*self.c) >= 0:
            return ((-self.b - (self.b**2 - 4*self.a*self.c)**0.5)/(2 * self.a))
        else:
            return None
    @property
    def x2(self):
        if (self.b**2 - 4*self.a*self.c) >= 0:
            return ((-self.b + (self.b**2 - 4*self.a*self.c)**0.5)/(2 * self.a))
        else:
            return None
    @property
    def view(self):
        return (f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- '))
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    @coefficients.setter
    def coefficients(self, a):
        self.a, self.b, self.c = a

polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)