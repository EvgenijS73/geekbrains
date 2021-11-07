import csv
from itertools import zip_longest

usr = []
hob = []

with open('users.csv', 'r', encoding='utf-8') as file_1:
    for line in csv.reader(file_1):
        usr.append(str(line))

with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for line in csv.reader(file_2):
        hob.append(line)

user_data = ((usr, hob) for usr, hob in zip_longest(usr, hob, fillvalue=None))

with open('users_h.txt', 'w', encoding='utf-8') as f:
    for users_h in user_data:
        f.write(f'{users_h[0]}: {users_h[1]}\n')
