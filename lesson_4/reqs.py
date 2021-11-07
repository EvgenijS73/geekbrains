import xml.dom.minidom
from requests import get, utils

r = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(r.headers)
content = r.content.decode(encoding=encodings)
print(content)

dom = xml.dom.minidom.parseString(content)
root = dom.getElementsByTagName("ValCurs")[0]
date = f"Текущий курс валют ЦБ РФ на {root.getAttribute('Date')}г"
print(date)

currency = dom.getElementsByTagName('Valute')

for rate in currency:
    name = rate.getElementsByTagName("Name")[0]
    value = rate.getElementsByTagName("Value")[0]
    nominal = rate.getElementsByTagName("Nominal")[0]
    res = "{0} {1} {2} рубля(-ей)".format(nominal.firstChild.data, name.firstChild.data, value.firstChild.data)
    print(res)
