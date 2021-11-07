# import pprint  # более читаемый вывод в консоль
data = []
ip = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        line = line.replace(' - - ', ' ').replace('"', '').split(' ')
        data.append(tuple([line[0], line[3], line[4]]))

# pprint.pprint(data)

# with open('new_nginx.txt', 'w', encoding='utf-8') as f:  # записал новые данные в файл
#     f.write(str(data))

for _ in data:  # создал список ip
    ip.append(_[0])


# pprint.pprint(ip)

# x = max(ip, key=ip.count) # ищем спамера
# print(x)


def max_ip(lst, spammer_ip):  # проверяем количество вхождений ip
    count = 0
    for i in lst:
        if i == spammer_ip:
            count += 1
    return count


spammer = max(ip, key=ip.count)
print(spammer, "is the spammer ", max_ip(ip, spammer), "occurrences")  # весь процесс занимет порядка минуты
