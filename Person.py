class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def get_name(self):
        return (self.name + ' ' + self.surname)
    def set_name(self, new_name):
        self.name, self.surname = new_name.split()
    fullname = property(get_name, set_name)

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)