thesaurus = ["Иван Петров", "Мария Иванова", "Петр Мамонов", "Илья Илларионов",
             "Иммануил Политковский", "Митрофан Михайлов", "Пелагея Плакунова",
             "Марфуша Матюшина", "Павсикакий Иртанов", "Мария Иванова", "Павел Истахов",
             "Михаил Пафнутиев", "Ибрагим Махолбеков"]

all_names = {}


def alpha_names(names_list):
    names_i = list(filter(lambda el: el.startswith('И'), names_list))

    names_p = list(filter(lambda el: el.startswith('П'), names_list))

    names_m = list(filter(lambda el: el.startswith('М'), names_list))

    i_dict = dict()
    i_dict['И'] = names_i

    p_dict = dict()
    p_dict['П'] = names_p

    m_dict = dict()
    m_dict['М'] = names_m

    all_names.update(i_dict)
    all_names.update(m_dict)
    all_names.update(p_dict)

    return all_names


def alpha_surnames(names_list):
    surnames_i = list(filter(lambda el: el.split(' ')[-1].startswith('И'), names_list))

    surnames_p = list(filter(lambda el: el.split(' ')[-1].startswith('П'), names_list))

    surnames_m = list(filter(lambda el: el.split(' ')[-1].startswith('М'), names_list))

    i_dict = {'И': surnames_i}
    alpha_names(surnames_i)
    i_dict.update(all_names)
    surname_i = {'И': i_dict}
    print(surname_i)

    p_dict = {'П': surnames_p}
    alpha_names(surnames_p)
    p_dict.update(all_names)
    surname_p = {'П': p_dict}
    print(surname_p)

    m_dict = {'М': surnames_m}
    alpha_names(surnames_m)
    m_dict.update(all_names)
    surname_m = {'М': m_dict}
    print(surname_m)


alpha_surnames(thesaurus)
