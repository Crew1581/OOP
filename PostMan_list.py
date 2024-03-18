class Postman:
    def __init__(self):
        self.delivery_data = []
    def add_delivery(self, street, house, kv):
        if (street,house,kv) not in self.delivery_data:
            self.delivery_data.append((street,house,kv))

        #print(self.delivery_data)
    def get_houses_for_street(self, street):
        self.dic = {}
        self.h = []
        self.houses = [h[1] for h in self.delivery_data if h[0] == street]
        for self.i in self.houses:
            if self.i not in self.dic:
                self.dic[self.i] = None
                self.h.append(self.i)
        return self.h

    def get_flats_for_house(self, street, house):
        self.dic = {}
        self.h = []
        self.flat = [h[2] for h in self.delivery_data if h[0] == street and h[1] == house]
        for self.i in self.flat:
            if self.i not in self.dic:
                self.dic[self.i] = None
                self.h.append(self.i)
        return self.h

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))