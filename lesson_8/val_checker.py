from functools import wraps


def val_checker(number):
    def true_val_checker(func):
        @wraps(func)
        def checker(x):
            if number(x):
                return func(x)
            else:
                raise ValueError(f'wrong val: {x}')

        return checker

    return true_val_checker


@val_checker(lambda x: x >= 0)
def calc_cube(x):
    ''' Документация '''
    return x ** 3


f = calc_cube(10)
print(f)
print(calc_cube.__doc__)
print(calc_cube.__name__)
