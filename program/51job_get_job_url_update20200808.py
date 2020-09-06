# coding=utf-8
'''
@Date: 2020-06-23 14:23:18
@Author: YING
@LastEditTime: 2020-07-12 11:26:54
'''

import os
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# 读取本地html文件，输出url和job_title
def get_info(file_name,only_a_tags):
    with open(file_name,'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser", parse_only=only_a_tags)
    l_link = [link.get('href') for link in soup.find_all("a",target="_blank",title=True,href=True)]
    l_title = [link.get('title') for link in soup.find_all("a",target="_blank",title=True,href=True)]
    return l_link,l_title

# 主程序
os.chdir(r'D:\JunZhu\My Downloads\工作\51job列表20200712')
file_lists = os.listdir('.')

only_a_tags = SoupStrainer("span")
job_link = []
job_title = []
l = 1

print('一共有 {} 个html\n'.format(len(file_lists)))

for i in file_lists:
    tempt_link,tempt_title = get_info(i,only_a_tags)
    job_link += tempt_link
    job_title += tempt_title
    print('已完成第 {} 个'.format(l)) 
    l += 1

print('全部html已经读取完成，开始到处excel！\n')

data = {'job_title':job_title,'job_link':job_link}
df = pd.DataFrame(data)

# 分离职位和公司信息
df_company = df.iloc[1::2].reset_index()
df_job = df.iloc[::2].reset_index()

df_all = pd.concat([df_job,df_company],axis=1)


df_all.to_excel(r'D:\JunZhu\My Downloads\工作\51job_url20200712.xlsx')

print('END')