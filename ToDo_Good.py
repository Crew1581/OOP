class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, priority):
        return [t for t, p in self.things if p == priority]

    def get_low_priority(self):
        priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)


todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))