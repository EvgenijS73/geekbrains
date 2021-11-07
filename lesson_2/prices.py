prices = [56.3, 24.36, 85.97, 165, 963.5, 45.11, 325.09, 854.37, 78.58, 458.96, 854, 16.07, 15, 89.01]
print(prices)
print('ID: ', id(prices))

# def print_price():
#     for i in prices:
#         price = f'{i:.2f}'
#         print('цена:', price[:price.index('.')], 'руб', price[price.index('.') + 1:], 'коп', end=", ")

# A
print('\n', 'Задание A')
for i in prices:
    price = f'{i:.2f}'
    print('цена:', price[:price.index('.')], 'руб.', price[price.index('.') + 1:], 'коп.', end=', ')
#   print('цена:', f'{i:.2f}'[:f'{i:.2f}'.index(".")], 'руб.', f'{i:.2f}'[f'{i:.2f}'.index(".") + 1:], 'коп.', end=', ')

# B
print('\n\n', 'Задание B')
prices.sort()
print(prices)
print('ID: ', id(prices))
for i in prices:
    print('цена:', f'{i:.2f}'[:f'{i:.2f}'.index(".")], 'руб.', f'{i:.2f}'[f'{i:.2f}'.index(".") + 1:], 'коп.', end=', ')

# C
print('\n\n', 'Задание C')
reverse_prices = sorted(prices, reverse=True)
print(reverse_prices)
print('ID: ', id(reverse_prices))
for i in reverse_prices:
    print('цена:', f'{i:.2f}'[:f'{i:.2f}'.index(".")], 'руб.', f'{i:.2f}'[f'{i:.2f}'.index(".") + 1:], 'коп.', end=', ')

# D
print('\n\n', 'Задание D')
prices.sort(reverse=True)
print(prices)
for i in prices[0:5]:
    print('цена:', f'{i:.2f}'[:f'{i:.2f}'.index(".")], 'руб.', f'{i:.2f}'[f'{i:.2f}'.index(".") + 1:], 'коп.', end=', ')
