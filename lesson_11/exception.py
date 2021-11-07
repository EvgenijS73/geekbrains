class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('enter the  dividend: '))
b = int(input('enter the divisor: '))

try:
    if b == 0:
        raise MyException('Error divisor = 0! Try again!')
except MyException as err:
    print(err)
else:
    result = a / b
    print(f"Result of division = {result}")
finally:
    print('Program completed')

