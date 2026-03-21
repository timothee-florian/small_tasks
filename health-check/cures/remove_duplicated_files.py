#!/usr/bin/env python3
import sys
import os
import pathlib
# print(sys.argv[1])
os.chdir(sys.argv[1])
files = os.listdir()
stat_file = {}
for file_ in files:
    try:
        size = os.path.getsize(file_)
        fname = pathlib.Path(file_)
        mtime = str(fname.stat().st_mtime)
        stat_file[(size, mtime)] = stat_file.get((size, mtime), []) + [file_]
    except:
        pass

for k, files in stat_file.items():
    if len(files) > 1:
        for file_ in files[1:]:
            os.remove(file_)
            print('remove {}, size {}'.format(file_, k[0]//2**20))
