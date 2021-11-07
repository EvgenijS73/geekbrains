import re
from pprint import pprint

with open('nginx_logs.txt', 'r') as file:
    for logs in file:
        parse_logs = re.compile(r'([\d\.]+) - - \[([\d.\/\w\:\s\+\d]+)\] \"([\w]+) (.+) .+\s+([\d]+) ([\d]+)')
        pprint(parse_logs.findall(logs))
