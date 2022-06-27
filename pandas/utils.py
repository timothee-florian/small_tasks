import pandas as pd
import os
import shutil


def string_of_list_to_list_of_string(s):
    l = s.replace('[','').replace(']','').split(',')
    l = list(map(lambda x: x.strip()[1:-1], l))
    return l

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def three_way_copy(copy_path_with_file, root_copy, copy_file, paste_root_path_file):
    l_copy_path_with_file = copy_path_with_file.split('\\')
    l_root_copy = root_copy.split('\\')
    l_copy_path_with_file = l_copy_path_with_file[len(l_root_copy):]
    l_copy_file = copy_file.split('\\')
    root = paste_root_path_file
    print(l_copy_path_with_file)
    for path_with_file in l_copy_path_with_file[:-1]:
        print(path_with_file)
        print(root)
        root = os.path.join(root, path_with_file)
        print(root)
        if not os.path.exists(root):
            os.mkdir(root)
    path_to_paste = os.path.join(root, l_copy_path_with_file[-1])
    print(path_to_paste)
    shutil.copyfile(copy_file, path_to_paste)




a=['C:\\Users\\bronner\\Desktop\\small_tasks\\conda\\environment_handling.py',\
    'C:\\Users\\bronner\\Desktop',
    'C:\\Users\\bronner\\Desktop\\small_tasks\\sql_automation\\get_tables_cols.py',
    'C:\\Users\\bronner\\Dropbox']


three_way_copy(*a)

df = pd.DataFrame([a])
df.apply(lambda x: three_way_copy(*x), axis=1)