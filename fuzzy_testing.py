# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:01:37 2023

@author: bronner
"""

import pandas as pd
import numpy as np
import string
from rapidfuzz import fuzz
import time

n = 12000
m = 10000
d1 = 1
d2 = 2
l1  = 10
l2 = 10
# df = pd.DataFrame(np.random.randint(0,100,size=(100, 1)), columns=list('A'))
df2 = pd.DataFrame(np.arange(n), columns = ['A']).applymap(lambda x: ''.join(l1*[np.random.choice(list(string.ascii_letters)) for _ in range(d1)]))
df3 = pd.DataFrame(np.arange(n), columns = ['B']).applymap(lambda x: ''.join(l2*[np.random.choice(list(string.ascii_letters)) for _ in range(d2)]))

df2['A'] = df2['A'].apply(lambda x: x.lower())
df3['B'] = df3['B'].apply(lambda x: x.lower())


df2['k'] = 1
df3['k'] = 1

dff = pd.merge(df2, df3, on= ['k'])
dff.drop(columns = ['k'], inplace = True)

def distance_comp(x, y, precomputed = {}, build_dict = False):
    if build_dict:
        if (x,y) not in precomputed:
            precomputed[(x,y)] = fuzz.ratio(x, y)
    return precomputed.get((x,y), fuzz.ratio(x, y))

def distance_pre_comp(x, y, precomputed = {}):
    return precomputed.get((x,y), fuzz.ratio(x, y))


def fr(x, y):
    return fuzz.ratio(x,y)
import numpy as np
fr_vect = np.vectorize(fr)
#####################################################################################################################
t1 = time.time()
dfpp = dff.drop_duplicates()
print(int(time.time()-t1))
dfpp['d'] = fr_vect(dfpp['A'],dfpp['B'])
print(int(time.time()-t1))
#####################################################################################################################
#####################################################################################################################
t1 = time.time()
precomputed = {}
dfs = []
dfp = dff.sample(m).drop_duplicates()
#dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
dfp['d'] = fr_vect(dfp['A'],dfp['B'])
dfff = pd.merge(dff, dfp, on = ['A', 'B'], how = 'left')
dff1 = dfff[~dfff['d'].isnull()]
dfs += [dff1]
print(int(time.time()-t1))
dff2 = dfff[dfff['d'].isnull()][['A', 'B']]

dfp = dff2.sample(m).drop_duplicates()
#dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
dfp['d'] = fr_vect(dfp['A'],dfp['B'])
dfff = pd.merge(dff2, dfp, on = ['A', 'B'], how = 'left')
dff12 = dfff[~dfff['d'].isnull()]
dfs += [dff12]
print(int(time.time()-t1))
dff3 = dfff[dfff['d'].isnull()][['A', 'B']]

dfp = dff3.sample(m).drop_duplicates()
#dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
dfp['d'] = fr_vect(dfp['A'],dfp['B'])
dfff = pd.merge(dff3, dfp, on = ['A', 'B'], how = 'left')
dff12 = dfff[~dfff['d'].isnull()]
dfs += [dff12]
print(int(time.time()-t1))
dffl = dfff[dfff['d'].isnull()][['A', 'B']]
# if len(dff3)> m and False:
#     print(1)
#     dfp = dff3.sample(m).drop_duplicates()
# else:
dfp = dffl.sample(len(dffl)).drop_duplicates()

#dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
dfp['d'] = fr_vect(dfp['A'],dfp['B'])
dfff = pd.merge(dff3, dfp, on = ['A', 'B'], how = 'left')
dff13 = dfff[~dfff['d'].isnull()]
dfs += [dff13]

print(np.sum(list(map(lambda x: len(x), dfs))))
print(int(time.time()-t1))
#####################################################################################################################

# t1 = time.time()
# precomputed = {}
# dfs = []
# dfp = dff.sample(m).drop_duplicates()
# dfp['d'] = dfp[['A', 'B']].apply(lambda x: distance_comp(x[0],x[1], precomputed = precomputed, build_dict = True), axis =1)
# dfff = pd.merge(dff, dfp, on = ['A', 'B'], how = 'left')
# dff1 = dfff[~dfff['d'].isnull()]
# dfs += [dff1]

# dff2 = dfff[dfff['d'].isnull()][['A', 'B']]

# dfp = dff2.sample(m).drop_duplicates()
# dfp['d'] = dfp[['A', 'B']].apply(lambda x: distance_comp(x[0],x[1], precomputed = precomputed, build_dict = True), axis =1)
# dfff = pd.merge(dff2, dfp, on = ['A', 'B'], how = 'left')
# dff12 = dfff[~dfff['d'].isnull()]
# dfs += [dff12]

# dff3 = dfff[dfff['d'].isnull()][['A', 'B']]
# if len(dff3)> m and False:
#     print(1)
#     dfp = dff3.sample(m).drop_duplicates()
# else:
#     dfp = dff3.drop_duplicates()
# dfp['d'] = dfp[['A', 'B']].apply(lambda x: distance_comp(x[0],x[1], precomputed = precomputed, build_dict = True), axis =1)
# dfff = pd.merge(dff3, dfp, on = ['A', 'B'], how = 'left')
# dff13 = dfff[~dfff['d'].isnull()]
# dfs += [dff13]

# print(np.sum(list(map(lambda x: len(x), dfs))))



# t0 = time.time()
# dff['d'] = dff[['A', 'B']].apply(lambda x: distance_pre_comp(x[0],x[1], precomputed = precomputed), axis =1)
# print(time.time()-t0)
# print(time.time()-t1)

# t1 = time.time()
# precomputed = {}

# dff['d'] = dff[['A', 'B']].apply(lambda x: distance_comp(x[0],x[1], precomputed = precomputed, build_dict = True), axis =1)

# print(int(time.time()-t1))


t1 = time.time()
dff['e'] = dff[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
print(int(time.time()-t1))
def fr(x, y):
    return fuzz.ratio(x,y)
import numpy as np
fr_vect = np.vectorize(fr)
t1 = time.time()
dff['f'] = fr_vect(dff['A'],dff['B'])
print(int(time.time()-t1))


def ff(dff, m):
    dfs= []
    while len(dff) > m:
        dfp = dff.sample(m).drop_duplicates()
        dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
        dfff = pd.merge(dff, dfp, on = ['A', 'B'], how = 'left')
        dfs += [dfff[~dfff['d'].isnull()]]
        dff = dfff[dfff['d'].isnull()][['A', 'B']]
    dfp = dff.sample(m).drop_duplicates()
    dfp['d'] = dfp[['A', 'B']].apply(lambda x: fuzz.ratio(x[0],x[1]), axis =1)
    dfff = pd.merge(dff, dfp, on = ['A', 'B'], how = 'left')
    dfs += [dfff[~dfff['d'].isnull()]]
    return dfs