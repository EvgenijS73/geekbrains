import os
import yaml

with open('config.yaml') as f:
    yaml_list = yaml.load(f, Loader=yaml.FullLoader)
    for k, v in yaml_list.items():
        root_dir = k
        for i, j in v.items():
            os.makedirs(os.path.join(os.curdir, root_dir, i), exist_ok=True)
            for h in j:
                with open(os.path.join(os.curdir, root_dir, i, h), 'w') as fs:
                    pass
