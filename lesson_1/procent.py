declination = ['процент', 'процента', 'процентов']
number = int(input('введите число от 1 до 100: '))

if number // 10 == 1:
    print(number, declination[2])
elif number % 10 == 1:
    print(number, declination[0])
elif 0 < number % 10 < 5:
    print(number, declination[1])
else:
    print(number, declination[2])
