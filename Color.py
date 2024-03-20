class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self.r = int(self._hexcode[0] + self._hexcode[1],16)
        self.g = int(self._hexcode[2] + self._hexcode[3], 16)
        self.b = int(self._hexcode[4] + self._hexcode[5], 16)
    @property
    def hexcode(self):
        return self._hexcode
    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(self._hexcode[0] + self._hexcode[1],16)
        self.g = int(self._hexcode[2] + self._hexcode[3], 16)
        self.b = int(self._hexcode[4] + self._hexcode[5], 16)

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)