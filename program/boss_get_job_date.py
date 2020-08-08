# coding=utf-8
'''
@Date: 2020-05-28 21:42:26
@Author: YING
@LastEditTime: 2020-07-27 20:52:46
'''

# @author: ying

import json
import os
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# 读取本地html文件，输出json信息
def get_info(file_name,only_a_tags):
    with open(file_name,'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser", parse_only=only_a_tags)
    info_dict = json.loads(soup.string)
    return info_dict

# 主程序
os.chdir(r'D:\JunZhu\My Downloads\工作\boss数据20200727')
file_lists = os.listdir('.')

only_a_tags = SoupStrainer("script", type='application/ld+json')
info_list = []
l = 1

print('一共有 {} 个html\n'.format(len(file_lists)))

for i in file_lists:
    d = get_info(i,only_a_tags)
    info_list.append(d)
    print('已完成第 {} 个'.format(l)) 
    l += 1

print('全部html已经读取完成，开始导出excel！\n')

df = pd.DataFrame(info_list)
df.to_excel(r'D:\JunZhu\My Downloads\工作\boss数据20200727.xlsx')

print('END')
