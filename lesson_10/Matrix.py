class Matrix:
    def __init__(self, *param):
        self.param = param

    def __str__(self):
        return f'|{self.param[0]}|\n|{self.param[1]}|\n\n|{self.param[2]}|\n|{self.param[3]}|\n' \
               f'|{self.param[4]}|\n\n|{self.param[5]}|\n|{self.param[6]}|\n'


class Matrix2:
    def __init__(self, *param):
        self.param = param

    def __add__(self, other):
        return Matrix2(
            self.param[0] + other.param[0], self.param[1] + other.param[1],
            self.param[2] + other.param[2], self.param[3] + other.param[3])

    def __str__(self):
        return f'|{self.param[0]} {self.param[1]}|\n|{self.param[2]} {self.param[3]}|\n'


mc = Matrix('10 12', '30 41', '16 14 45', '88 36 96', '87 54 21', '12 52 36 89', '64 28 67 47')
print(mc)
mc_1 = Matrix2(10, 32, 15, 20)
mc_2 = Matrix2(35, 10, 15, 20)
print(mc_1)
print(mc_2)
print(mc_1 + mc_2)
