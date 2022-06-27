import pandas as pd

def string_of_list_to_list_of_string(s):
    l = s.replace('[','').replace(']','').split(',')
    l = list(map(lambda x: x.strip()[1:-1], l))
    return l