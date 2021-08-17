#!/usr/bin/env python3

import os
import json
import requests

home_path = os.path.expanduser("~")
folder = '/data/feedback'
text_files = [text_f for text_f in os.listdir(folder) if '.txt' in text_f]
text_files_absolut = [os.path.join(folder, name) for name in text_files]


def create_dict_from_txt(text_file):
    data = dict()
    keys= ['title', 'name', 'date', 'feedback']
    i = 0
    with open(text_file) as f:
        # text = f.read()
        # lines = f.readlines()
        for line in f:
            data[keys[i]] = line
            i += 1
    return data


url = 'http://104.197.114.223/feedback/'
for text_file in text_files_absolut:
    data = create_dict_from_txt(text_file)
    response = requests.post(url, json=data)
    print(response.status_code)
