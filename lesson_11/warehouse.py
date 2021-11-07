class Warehouse:
    def __init__(self, par_1, par_2, par_3):
        self.par_1 = par_1
        self.par_2 = par_2
        self.par_3 = par_3


class Printer(Warehouse):
    def __init__(self, par_1, par_2, par_3, par_p):
        super().__init__(par_1, par_2, par_3)
        self.par_p = par_p


class Scanner(Warehouse):
    def __init__(self, par_1, par_2, par_3, par_s):
        super().__init__(par_1, par_2, par_3)
        self.par_s = par_s


class Copier(Warehouse):
    def __init__(self, par_1, par_2, par_3, par_c):
        super().__init__(par_1, par_2, par_3)
        self.par_c = par_c
