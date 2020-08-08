# coding=utf-8
'''
@Date: 2020-06-01 16:04:41
@Author: YING
@LastEditTime: 2020-08-06 20:56:19
'''

import os
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# 读取本地html文件，输出url和job_title
def get_info(file_name,only_a_tags):
    tempt_dict = {}
    with open(file_name,'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser", parse_only=only_a_tags)
    for i in soup:
        url = i.a['href']
        tempt_dict[url] = i.a['title']
    return tempt_dict

# 主程序
os.chdir(r'D:\JunZhu\My Downloads\工作\boss列表')
file_lists = os.listdir('.')

only_a_tags = SoupStrainer("span",class_='job-name')
job_list = {}
l = 1

print('一共有 {} 个html\n'.format(len(file_lists)))

for i in file_lists:
    d = get_info(i,only_a_tags)
    job_list.update(d)
    print('已完成第 {} 个'.format(l)) 
    l += 1

print('全部html已经读取完成，开始到处excel！\n')

ds = pd.Series(job_list)
ds.to_excel(r'D:\JunZhu\My Downloads\工作\boss_url2020806.xlsx')

print('END')