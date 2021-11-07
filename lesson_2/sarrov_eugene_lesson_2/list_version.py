list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(list_1)

for i in list_1:
    if i.isdigit():
        i = f'"{int(i):02d}"'
    elif i[1:].isdigit():
        i = f'"{i[0]}{int(i[1:]):02d}"'
    print(i, end=' ')
