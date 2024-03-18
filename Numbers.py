class Numbers:
    def __init__(self):
        self.s = []
    def add_number(self, n):
        self.s.append(n)
    def get_even(self):
        self.count = []
        for self.i in self.s:
            if int(self.i) % 2 == 0:
                self.count.append(int(self.i))
        return self.count
    def get_odd(self):
        self.count = []
        for self.i in self.s:
            if (int(self.i) + 1) % 2 == 0:
                self.count.append(int(self.i))
        return self.count
numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)
numbers.add_number(1)
numbers.add_number(7)
numbers.add_number(9)
numbers.add_number(12)

print(numbers.get_even())
print(numbers.get_odd())