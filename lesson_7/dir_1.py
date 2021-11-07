import os

project_folder = 'my_project'
paths = ['settings', 'minapp', 'adminapp', 'authapp']

for f in paths:
    os.makedirs(os.path.join(os.curdir, project_folder, f), exist_ok=True)
