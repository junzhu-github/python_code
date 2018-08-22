# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:14:14 2018

@author: YING
"""

import os
import time


#复制文件
source = 'D:\\test\\1'
target_dir = 'D:\\test\\2'

print(os.getcwd())
os.chdir(target_dir)
print(target_dir+time.strftime('%Y%m%d'))

'''
if time.strftime('%Y%m%d') not in os.listdir(target_dir):
    os.mkdir(f"{target_dir}+'\\'+{time.strftime('%Y%m%d')})

name_list = []
for root,dirs,files in os.walk(source):
    for name in files:
        name_path = os.path.join(root,name)
        name_list.append(name_path)  

for i in name_list:
    copy_command = f"copy {i} {target_dir}"
    os.system(copy_command)

#重命名文件
os.chdir(target_dir)

for filename in os.listdir(target_dir):
    portion = os.path.splitext(filename)    # 分离文件名字和后缀
    os.system(f"rename {os.path.abspath(filename)} {portion[0]}({time.strftime('%Y%m%d%H%M%S')}){portion[1]}")
'''