import csv
import pprint
from itertools import zip_longest

usr = []
hob = []

with open('users.csv', 'r', encoding='utf-8') as file_1:
    for line in csv.reader(file_1):
        usr.append(str(line))

with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for line in csv.reader(file_2):
        hob.append(line)

if len(usr) < len(hob):
    print(1)
else:
    user_data = {k: v for k, v in zip_longest(usr, hob, fillvalue=None)}
    pprint.pprint(user_data)
    with open('new_user_data.csv', 'w', encoding='utf-8') as f:
        f.write(str(user_data))
