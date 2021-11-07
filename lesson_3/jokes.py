from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes():
    """Введите число не больше количества слов в первом списке"""
    user_count = int(input('Введите желаемое количество шуток(не более 4-х): '))
    permission = int(input('Введите разрешение на повтор шуток(0 - запрет): '))
    count = 0
    while count < user_count:
        count += 1
        bonus = choice(nouns)
        konus = choice(adverbs)
        monus = choice(adjectives)
        print(bonus, ' ', konus, ' ', monus)
        if permission == 0:
            nouns.remove(bonus)
            adverbs.remove(konus)
            adjectives.remove(monus)



get_jokes()
