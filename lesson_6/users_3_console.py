import csv
from itertools import zip_longest

usr = []
hob = []
users = input('enter filename for users: ')
hobby = input('enter filename for hobby: ')
join = input('enter file name for integration: ')


def users_hobby():
    with open(f'{users}', 'r', encoding='utf-8') as file_1:
        for line in csv.reader(file_1):
            usr.append(str(line))

    with open(f'{hobby}', 'r', encoding='utf-8') as file_2:
        for line in csv.reader(file_2):
            hob.append(line)

    user_data = {k: v for k, v in zip_longest(usr, hob) if k is not None}

    with open(f'{join}', 'w', encoding='utf-8') as f:
        f.write(str(user_data))


if __name__ == '__main__':
    users_hobby()
