import re

#r'^\b\d{2}.+123asd$'


# regex = re.compile(r'\s+')
# print(type(regex), regex)
# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(type(result), result)
#
# ####  . - Один любой символ, кроме новой строки \n
# result = re.match(r'м.л.', 'молоко')
# print(result.group())
#
# ####  \d - Любая цифра
# result = re.match(r'А\d', 'А9')
# print(result.group())
#
# ####  \D - Любой символ, кроме цифры
# result = re.match(r'\D', '1')
# print(result)
#
# ####  \s - Любой пробельный символ (пробел, табуляция, конец строки и т.п.)
# result = re.match(r'\s', 'молоко')
# print(result)
#
# ####  \w - Любая буква (то, что может быть частью слова), а также цифры и _
# result_one = re.match(r'\w\w\w', 'qwert')
# result_two = re.match(r'\w\w\w', 'Год')
# print(result_one.group(), result_two.group())
#
# ####  [..] - Один из символов в скобках, а также любой символ из диапазона a-b_
# result_one = re.match(r'[0-9][0-9A-Fa-f]', '8c') #zZ0.@zZ0.z
# result_two = re.match(r'[./?,""547]', '7')
# print(result_one.group(), result_two.group())
#
# ####  [^..] - Любой символ, кроме перечисленных
# result_one = re.match(r'<[^>]>', '<a>')
# result_two = re.match(r'<[^0-9]>', '<9>')
# print(result_one.group(), result_two)
#
# ####  {n} - Ровно n повторений
# result_one = re.match(r'\d{4}', '1234123434')
# result_two = re.match(r'\d{4}', '4123')
# print(result_two.group(), result_one)
#
# ####  {m,n} - От m до n повторений включительно
# result_one = re.match(r'\d{2,4}', '1243')
# result_two = re.match(r'\d{2,4}', '1')
# print(result_one.group(), result_two)

# ####  ? - Ноль или одно вхождение, синоним {0,1}
# result_one = re.match(r'валы?', 'валы')
# result_two = re.match(r'валы?', 'волов')
# print(result_one.group(), result_two.group())
#
# """По умолчанию квантификаторы жадные —
# захватывают максимально возможное число символов.
# Добавление ? делает их ленивыми,
# они захватывают минимально возможное число символов"""
#
# ####  * - Ноль или более, синоним {0,}
# result_one = re.match(r'СУ\d*', 'СУ')
# result_two = re.match(r'СУ\d*', 'СУ12')
# print(result_one.group(), result_two.group())
#
# result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# print(result, result.group())
# result = re.search(r'AV', 'AV Analytics Vidhya AV')
# print(result, result.group())
#
# print(re.findall(r'[A-V][a-v]', 'AV Analytics Vidhya AV'))

#########################################################################

# def p_wrapper(func):
#    def tag_wrapper(a):
#        markup = func(a)
#        return f'<p>{markup}</p>'
#
#    return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(username_f)

# def wrap_div(func):
#     def inner(string):
#         print('<div>', end='')
#         func(string)
#         print('</div>')
#     return inner
#
# def wrap_p(func):
#     def inner(string):
#         print('<p>', end='')
#         func(string)
#         print('</p>', end='')
#     return inner
#
# @wrap_div
# @wrap_p
# def wrapped_text(string):
#     print(string, end='')
#
# def another_wrapped_text(string):
#     print(string, end='')
#
# wrapped_text('Text wrapped out with html tags')
# without_syntax_sugar = wrap_div(wrap_p(another_wrapped_text))
# without_syntax_sugar('decorated too')

#######################
# def simple_cache(func):
#    cache = {}
#
#    def wrapper(*args):
#        key = str(*args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]
#
#    return wrapper
#
#
# @simple_cache
# def render_input(field):
#    print(f"call render_input('{field}')")
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)
##########################

def logger(verbosity=0):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           msg = f'\tcall {func.__name__}'
           if verbosity > 0:
               msg = f'{msg}({", ".join(map(str, args))})'
           if verbosity > 1:
               msg = f'{msg} -> {result}'
           return msg

       return wrapper

   return _logger


@logger(verbosity=2)
def render_input(field):
   return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
password_f = render_input('password')
print(username_f)
print(password_f)
