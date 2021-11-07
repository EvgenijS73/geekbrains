def type_logger(func):
    def type_x(x):
        print('calc_cube (', x, ':', type(x), ')')
        return func

    return type_x


@type_logger
def calc_cube(x):
    return x ** 3


f = calc_cube(3.14)
