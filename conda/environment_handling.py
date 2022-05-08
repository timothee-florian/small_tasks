"""Spyder Editor."""

import os
import sys
import argparse
# os.system(r'conda activate C:\Users\me\anaconda3')
# os.system(r'pip freeze > C:\Users\me\Desktop\test\requ.txt')


# os.system(r'conda create --prefix C:\Users\me\Desktop\test\test_env2 python=3.8.8')

# os.system(r'conda activate C:\Users\me\Desktop\test\test_env2')

# os.system(r'pip install -r C:\Users\me\Desktop\test\requ.txt')

def create_activate_env(path : str, python_version) -> None:
    """For now only create."""
    os.system(rf'conda create -y --prefix {path} python={python_version}')
    os.system(r'y')
    os.system(rf'conda activate {path}')
    os.system(r'conda env list')

def clone_env(old_path : str, new_path : str) -> None:
    """Clone a conda environment.
    
    Args_:
        - old_path - path of the env to clone
        - new_path - path of the wanted clone
        
    """
    os.system(rf'conda create --name {new_path} --clone {old_path}')
    # python_version = sys.version_info
    # python_version = f'{python_version.major}.{python_version.minor}.{python_version.micro}'
    # os.system(rf'conda activate {old_path}')
    # os.system(r'pip freeze > requ.txt')
    # create_activate_env(path = new_path, python_version = python_version)
    # os.system(r'pip install -r requ.txt')
    # if os.path.exists("requ.txt"):
    #     os.remove("requ.txt")
    

  
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='create and activate a new conda environment')
    parser.add_argument('-p', '--path', type = str, help = 'path name of the new environment')
    args = parser.parse_args()
    
    python_version = sys.version_info
    python_version = f'{python_version.major}.{python_version.minor}.{python_version.micro}'
    create_activate_env(path = rf'{args.path}', 
                        python_version = python_version)
    
    
# getVersion =  subprocess.Popen(rf'conda env list', shell=True, stdout=subprocess.PIPE).stdout
# version =  getVersion.read()
# print(version.decode())