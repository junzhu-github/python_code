# coding=utf-8
'''
Date: 2020-10-06 20:23:38
Author: YING
LastEditTime: 2020-10-06 20:35:02
'''

import os

# 文件位置
file_address = r'C:\Users\me\Desktop'

# 定位文件位置
os.chdir(file_address)

# 查找所有文件
files = os.listdir('.')
# print(files)

urls = []

# 提取url
for i in files:
    if i[-3:] == 'txt':
        with open(i, 'r', encoding="utf8") as fr:
            url = fr.readline()
        urls.append(url)

# 输出url
with open(r'C:\Users\me\Desktop\urls.txt','w') as fw:
    fw.write('\n'.join(urls))

print('  OK!  ')