class Gun:
    def __init__(self):
        self.shots_counter = 0
    def shots_count(self):
        return self.shots_counter
    def shots_reset(self):
        self.shots_counter = 0
    def shoot(self):
        if self.shots_counter % 2 == 0:
            print('pif')
            self.shots_counter += 1
        else:
            print('paf')
            self.shots_counter += 1

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())