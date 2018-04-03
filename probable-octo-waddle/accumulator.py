# written by Tasi Cluff
class accumulator:
    def __init__(self):
        self.accumValue = 0
    @property
    def value(self):
        return self.accumValue
    @value.setter
    def value(self, val):
        if val < -9999:
            self.accumValue = -9999
        elif val > 9999:
            self.accumValue = 9999
        else:
            self.accumValue = val
