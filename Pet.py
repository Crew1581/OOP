class Pet:
    count = 0
    pets = []

    def __init__(self, name=None):
        self.name = name
        Pet.pets.append(self)
        Pet.count += 1

    @classmethod
    def first_pet(cls):
        if cls.pets:
            return cls.pets[0]
        else:
            return None

    @classmethod
    def last_pet(cls):
        if cls.pets:
            return cls.pets[-1]
        else:
            return None

    @classmethod
    def num_of_pets(cls):
        return cls.count

pet1 = Pet('lol')
pet2 = Pet('lool')
pet3 = Pet('loool')

# Используем методы first_pet, last_pet и num_of_pets
print(Pet.first_pet().name)  # Выведет: lol
print(Pet.last_pet().name)   # Выведет: loool
print(Pet.num_of_pets())     # Выведет: 3
