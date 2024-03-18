class Postman:
    def __init__(self):
        self.delivery_data = []
        self.delivery_data1 = {}
    def add_delivery(self, street, house, kv):
        if street not in self.delivery_data1:
            self.delivery_data1[street] = {house: [kv]}
        elif (street in self.delivery_data1) and (house not in self.delivery_data1[street]):
            self.delivery_data1[street][house] = [kv]
        elif (street in self.delivery_data1) and (house in self.delivery_data1[street]) and kv not in self.delivery_data1[street][house]:
            self.delivery_data1[street][house].append(kv)

    def get_houses_for_street(self, street):
        self.keys = []
        if street not in self.delivery_data1:
            return self.keys
        for key in self.delivery_data1[street].keys():
            self.keys.append(key)
        return self.keys
    def get_flats_for_house(self, street, house):
        if street not in self.delivery_data1 or house not in self.delivery_data1[street]:
            return []
        return self.delivery_data1[street][house]

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))