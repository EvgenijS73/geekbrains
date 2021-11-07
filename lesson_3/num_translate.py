nums = {

    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate():
    num = input('Enter the number in English: ')
    if num.istitle():
        num = num.lower()
        for key, val in nums.items():
            if num == key:
                print(val.capitalize())
    else:
        for key, val in nums.items():
            if num == key:
                print(val)


num_translate()
