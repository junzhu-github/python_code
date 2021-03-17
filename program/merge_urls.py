# coding=utf-8
'''
Date: 2020-10-06 20:23:38
Author: YING
LastEditTime: 2021-03-17 22:14:08
'''

import os
import time

# 文件位置
file_address = r'D:\OneDrive\Attachments'

# 定位文件位置
os.chdir(file_address)

# 查找所有文件
files = os.listdir('.')
# print(files)

urls = []

# 提取url并删除文件
for i in files:
    n = 0
    if i[-3:] == 'txt':
        with open(i, 'r', encoding="utf8") as fr:
            ct = fr.readlines()
            # print(ct)
            # print('-'*50)
               
        for j in ct:
            if j.startswith('http'):
                urls.append(j)
                n += 1
    if n > 0:
        print('%s 已删除！' %i)
        os.remove(i)

# 生成txt文件名
process_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
file_name = file_address + r'\urls_' + str(process_time) + '.txt'

# 输出url
with open(file_name,'w') as fw:
    fw.write('\n'.join(urls))

print('  OK!  ')
