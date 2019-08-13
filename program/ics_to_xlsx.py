# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:14:14 2018

@author: YING
"""

import pandas as pd

data = []

with open(r'C:\Users\Dragon\OneDrive\文档\home@google.ics','r', encoding='UTF-8') as f:
    content = f.readlines()
    cnt = 1
    tp_list = []
    for i in content:
        
        if i.startswith('DTSTART'):           
            tp_list.append(cnt)
            cnt += 1
            tp_list.append(i.strip().split(':')[1].split('T')[0])
            
        elif i.startswith('SUMMARY'):          
            tp_list.append(i.strip().split(':')[1])
            data.append(tp_list)
            tp_list = []    
        else:
            pass

df = pd.DataFrame(data)
df.to_excel('calender.xlsx')

print('Finish')