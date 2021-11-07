import os
import shutil

folder_way = r'my_project\templates'
for root, dirs, files in os.walk('my_project'):
    if root == folder_way:
        break
    for file in files:
        os.makedirs(os.path.join(folder_way, root.split('\\')[-1]), exist_ok=True)
        shutil.copyfile(os.path.join(root, file), os.path.join(folder_way, os.path.join(root.split('\\')[-1], file)))
