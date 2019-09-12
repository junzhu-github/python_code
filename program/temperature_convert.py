# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:36:23 2017

@author: ye
"""

val=input("请输入带温度表示符号的温度值（例如：32C）：")
if val[-1] in ['c','C']:
    f = 1.8*float(val[0:-1])+32
    print(f"转换后的温度为 {f}F")
elif val[-1] in ['f','F']:
    c=(float(val[0:-1])-32)/1.8
    print(f"转换后的温度为 {c}C")
else:
    print('wrong input')
    35