import re

date_inp = input('enter the data(d-m-y): ')


class Data:
    def __init__(self, data=date_inp):
        self.data = data

    @classmethod
    def get_data(cls, data=date_inp):
        date = re.compile(r"([^\-']\d+)")
        f = date.findall(data)
        d = int(f[0] + f[1] + f[2])
        print(type(d), d)

    @staticmethod
    def valid_data():
        date = re.compile(r"([^\-']\d+)")
        f = date.findall(date_inp)
        d = int(f[1])
        if 0 < d < 13:
            pass
        else:
            print('Incorrect months value. It must be from 1 to 12')
            # raise ValueError(f'months value must be from 1 to 12')


s = Data
s.get_data()
Data.valid_data()
