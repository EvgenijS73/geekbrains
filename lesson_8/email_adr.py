import re


# def email_parse(email_adr):
#     pars_email_adr = re.compile(r'(.+)@(\w+\..+)')
#     for adr in [email_adr]:
#         assert pars_email_adr.match(adr), f'wrong email address {adr}'
#     req = pars_email_adr.findall(email_adr)
#     for i in req:
#         email_dict = {'user name': i[0], 'domain': i[1]}
#         print(email_dict)


def email_parse(email_adr):
    pars_email_adr = re.compile(r'(?P<username>.+)@(?P<domain>\w+\..+)')
    for adr in [email_adr]:
        assert pars_email_adr.match(adr), f'wrong email address {adr}'
        print(*map(lambda x: x.groupdict(), pars_email_adr.finditer(email_adr)), sep=', ')


if __name__ == '__main__':
    email_adr = input('enter your email address: ')
    email_parse(email_adr)
