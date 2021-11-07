class Cell:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return f'{self.value + other.value}'

    def __sub__(self, other):
        if self.value - other.value > 0:
            return f'{self.value - other.value}'
        else:
            print('invalid value')

    def __mul__(self, other):
        return f'{self.value * other.value}'

    def __truediv__(self, other):
        return f'{self.value / other.value}'

    def __floordiv__(self, other):
        return f'{self.value // other.value}'

    # def make_order(self):
    #     for i in range(1, self.value + 1):
    #         print(i)
    #
    # __setattr__
    # __iter__


mc = Cell(12)
mc_1 = Cell(3)
print(mc - mc_1)
print(mc + mc_1)
print(mc * mc_1)
print(mc / mc_1)
print(mc // mc_1)

