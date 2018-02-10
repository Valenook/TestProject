import numpy as np
import random
"""
DATA SET, SMALL
6 7 1 5
TMMMTTT
MMMMTMM
TTMTTMT
TMMTMMM
TTTTTTM
TTTTTTM
"""
min, max = 1, 5
data = [['TMMMTTT'],['MMMMTMM'],['TTMTTMT'],['TMMTMMM'],['TTTTTTM'],['TTTTTTM']]
data_np = np.zeros((6,7), dtype='str')
data_bool = np.ones((6,7), dtype='bool')
tomatos = 0
mush = 0
for i in range(0,6):
    tomatos = tomatos + data[i][0].count('T')
    mush = mush + data[i][0].count('M')
    data_np[i] = np.array(list(data[i][0]))
MV = 'T' if tomatos > mush else 'M'

data_bool = (data_np == MV)
"""
data_bool[:,0]    - columns
data_bool[0]      - rows          
"""
check_r_list = []
for i in range(0, 6):
    if False in data_bool[i]:
        check_r_list.append(True)
    else:
        check_r_list.append(False)

if False in check_r_list:
    print('badcheck')
    check_c_list = []
    for i in range(0, 7):
        if False in data_bool[:,i]:
            check_c_list.append(True)
        else:
            check_c_list.append(False)
    #ДОПИСЫВАТЬ
else:
    ost = len(check_r_list)%max
    size_n = int((len(check_r_list) - ost)/max)
    sizes = np.ones((max))
    if ost/ost<max:
        for a in range(0,ost):
            ri = random.randint(0,len(sizes))
            sizes[ri] = sizes[ri] + ost



