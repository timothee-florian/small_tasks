import re

def clean_write(in_file, out_file, writing_mode):
    with open(file, 'r') as f:
        code = f.read()
    c_code = re.search(r'(create or replace view.*?;)', code, re.DOTALL|re.IGNORECASE).group(1)
    c_code = f'--{file}\n' + c_code + '\n'
    with open(out_file, writing_mode) as f:
        f.write(c_code)

out_file = 'views.sql'
with open(out_file, 'w') as f:
    f.write('')
for file in files_code:
    clean_write(in_file = file, out_file = out_file, writing_mode = 'a')