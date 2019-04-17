# -*- coding: utf-8 -*- 

# @author: ying

import re
import requests
import random

# 定义函数，输入网址返回其中的数字
def get_size(url):
    n = random.randint(25,45)
    r = requests.get(url, timeout=n)
    return re.findall(r"文件大小:(\d+\.?\d*){1}\sMB",r.text)

d = dict()

# 读入txt
with open('get_file_size_url.txt') as f:
    urls = f.readlines()
    print('~~~read_file_ok~~~')

# 去除网址后面的'\n'
urls = [x.rstrip("\n") for x in urls]
print('total {} files'.format(len(urls)))

# 把网址和对应的数字组合成字典
# l = len(urls)
for i in urls:
    s = get_size(i)
    if len(s):
        d[i] = get_size(i)[0]
    else:
        d[i] = 0
    print('{}   {} MB'.format(l,i,d[i]))
    # l = l-1
print('~~~find_all_file_size~~~')

# # 把结果写入新的txt
# with open('b.txt','w') as f:
#     for k,v in d.items():
#         f.write(k + '   '+ v + '\n')
print('~~~end~~~')