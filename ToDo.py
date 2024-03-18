class Todo:
    def __init__(self):
        self.things = []
    def add(self, deal, n):
        self.things.append((deal, n))
    def get_by_priority(self, n):
        return [x for x, a in self.things if a == n]
    def get_low_priority(self):
        self.m = min([prior for deal, prior in self.things], default=0)
        return [deal for deal, prior in self.things if self.m == prior]
    def get_high_priority(self):
        self.m = max([prior for deal, prior in self.things], default=0)
        return [deal for deal, prior in self.things if self.m == prior]


todo = Todo()



print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))