class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []


def numbers(*args):
    for i in args:
        try:
            if type(i) == int:
                num_list.append(i)
            elif i == 'stop':
                print(num_list)
                break
            else:
                raise MyException(f'It is not a digit: {i}')
        except MyException as err:
            print(err)


numbers(45, 67, 9, 89, 'f', 54, 89, 98, 'stop', 15, 56, 85)
# print(num_list)
