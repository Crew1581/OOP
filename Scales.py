class Scales:
    def __init__(self):
        self.a = 0
        self.b = 0
    def add_right(self, n):
        self.b += n
    def add_left(self, n):
        self.a += n
    def get_result(self):
        if self.a == self.b:
            return 'Весы в равновесии'
        elif self.a > self.b:
            return 'Левая чаша тяжелее'
        elif self.a < self.b:
            return 'Правая чаша тяжелее'

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())