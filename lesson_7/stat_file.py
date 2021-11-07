from os import walk, path, stat
import json

file_size = {}
for root, dirs, files in walk('some_data'):
    for file in files:
        file_val = stat(path.join(root, file)).st_size // 100
        file_extn = file.split('.')[-1]
        if file_val in file_size:
            file_size[file_val][-1].append(file_extn)
            file_size[file_val] = (file_size[file_val][0] + 1, file_size[file_val][1])
        else:
            file_size.setdefault(file_val, (1, [file_extn]))

result = {v: file_size[v] for v in sorted(file_size.keys())}
with open('result.json', 'w') as f:
    json.dump(result, f)

with open('result.json', 'r') as f:
    print(json.load(f))
