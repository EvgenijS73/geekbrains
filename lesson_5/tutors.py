from itertools import zip_longest, islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена' 'Коля',
    'Панкратий', 'Афанасий', 'Акакий', 'Даздраперма'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for i in zip_longest(tutors, klasses):
    print(i)

d = (i for i in zip_longest(tutors, klasses))
print(type(d), *islice(d, 20))
