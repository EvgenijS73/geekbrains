# z = a + bi
# z = z1 + z2 = (a1 + a2) + (b1 + b2)i

# z = z1 * z2 = (a1 + b1) * (a2 + b2)i


class Complex_Number_Add:
    def __init__(self, *value):
        self.value = value

    def __add__(self, other):
        return Complex_Number_Add(self.value[0] + other.value[0], self.value[1] + other.value[1])

    def __str__(self):
        return f'{self.value[0]} + {self.value[1]}i'



class Complex_Number_Mul:
    def __init__(self, *value):
        self.value = value

    def __mul__(self, other):
        return Complex_Number_Mul(self.value[0] + self.value[1], other.value[0] + other.value[1])

    def __str__(self):
        return f'{self.value[0]} * {self.value[1]}i'


mc = Complex_Number_Add(12, 7)
mc_1 = Complex_Number_Add(9, 17)

print(mc + mc_1)

mc = Complex_Number_Mul(12, 7)
mc_1 = Complex_Number_Mul(9, 17)

print(mc * mc_1)
