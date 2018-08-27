# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:11:54 2018

@author: shurastogi
"""

import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
list_y=[]
count=0
for val in df['X']:
    if val==0:
        #if 0 value add 0 in list
        list_y.append(0)
        #resetting count
        count=0
    else:
        #increase count till 0 is found
        count=count+1
        list_y.append(count)
#adding new column y and assiging generated list
df['Y']=list_y

df
        
    
    