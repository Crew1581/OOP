class HourClock:
    def __init__(self, hours):
        self.hours = hours
    def get_hour(self):
        return self._hours
    def set_hour(self, hours):                          # сеттер, используется для изменения имени
        if isinstance(hours, int) and hours >= 1 and hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
    hours = property(get_hour, set_hour)
try:
    HourClock(0)
except ValueError as e:
    print(e)