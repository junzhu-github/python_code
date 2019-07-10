# -*- coding: utf-8 -*- 

# @author: ying

import re
import requests
import random
import time

# 定义函数，输入网址返回其中的数字
def get_size(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
    # true_url = requests.get(url, headers=headers, timeout=5).url  # 针对跳转连接情况，获取真实地址
    # print(true_url)
    r = requests.get(url, headers=headers, timeout=5)
    return url,re.findall(r"[文件大小:|file size:](\d+\.?\d*){1}.MB",r.text)

d = dict()

# 读入txt
with open(r'C:\Users\Dragon\OneDrive\python\python_code\program\get_file_size_url.txt') as f:
    urls = f.readlines()
    print('~~~read_file_ok~~~')

# 去除网址后面的'\n'
urls = [x.rstrip("\n") for x in urls]
print('total {} files'.format(len(urls)))

# 把网址和对应的数字组合成字典
l = 1
for i in urls:
    m,n = get_size(i)
    if len(n):
        d[m] = get_size(i)[1][0]
    else:
        d[m] = 0
    print('{}  {} MB | No.{} | {} min'.format(m,d[m],l,round(float(d[m])*1.56,1)))

    # 暂停几秒
    n2 = random.randint(10,20)
    time.sleep(n2)

    l = l+1
    
print('~~~find_all_file_size~~~')

# # 把结果写入新的txt
# with open('b.txt','w') as f:
#     for k,v in d.items():
#         f.write(k + '   '+ v + '\n')
# print('~~~end~~~')
