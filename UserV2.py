class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name.isalpha():  # проверка имени перед заменой
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        if isinstance(age, int) and age >= 0 and age <= 110:
            self._age = int(age)
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():  # проверка имени перед заменой
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0 and new_age <= 110:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')

user = User('Гвидо', 61)

user.set_name('Тимур')
user.set_age(10)

print(user.get_name())
print(user.get_age())