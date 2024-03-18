class ElectricCar:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def set_owner(self, owner):
        self._owner = owner


car = ElectricCar('Elon')

car.set_owner = 'Gvido'

print(car.owner)