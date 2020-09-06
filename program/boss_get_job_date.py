# coding=utf-8
'''
@Date: 2020-05-28 21:42:26
@Author: YING
LastEditTime: 2020-09-02 21:03:54
'''

# @author: ying

import datetime as dt
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

# 切换工作目录
work_url = r'D:\JunZhu\My Downloads\工作'
html_path = 'boss运营20200902'

os.chdir(os.path.join(work_url,html_path))
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

print('全部html已经读取完成！\n')

df = pd.DataFrame(info_list)

# 去重
df = df.drop_duplicates('@id')
print('去重后剩余 {} 条信息!\n'.format(df.shape[0]))

# 筛选更新时间小于15天的信息
df['upDate'] = pd.to_datetime(df['upDate'])
df = df[(dt.datetime.now() - df['upDate']).dt.days<=15]
print('小于15天的信息有 {} 条.\n'.format(df.shape[0]))

# 对更新时间排序
df.sort_values('upDate',ascending=False,inplace=True)


os.chdir(work_url)
file_name = html_path + '.xlsx'
df.to_excel(file_name,index = False)

print('END')
