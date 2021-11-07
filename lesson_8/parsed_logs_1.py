import re

logs = '''raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1"
        304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"' '''

parse_logs = re.compile(r'\'([^\'][\d\.]+) - - \[([\d.\/\w\:\s\+\d]+)\] \"([\w]+) (.+) .+\s+([\d]+) ([\d]+)')

print(parse_logs.findall(logs))
