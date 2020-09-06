# coding=utf-8
'''
@Date: 2020-06-23 14:23:18
@Author: YING
LastEditTime: 2020-08-08 15:15:11
'''

import os
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# 读取本地html文件，输出url和job_title
def get_info(file_name,only_a_tags):
    with open(file_name,'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser", parse_only=only_a_tags)

    for i in soup:
        if i.input:
            url = i.a['href']
            title = i.span['title']
            area = i.find('span',class_='d at').contents[0]
            company = i.find('a',class_='cname at').contents[0]
    else:
        break

    return url,title,area,company

# 主程序
os.chdir(r'D:\JunZhu\My Downloads\工作\51job列表2020071')
file_lists = os.listdir('.')

only_a_tags = SoupStrainer('div',class_="e")
cum_url = []
cum_title = []
cum_area = []
cum_company = []
l = 1

print('一共有 {} 个html\n'.format(len(file_lists)))

for i in file_lists:
    single_data = get_info(i,only_a_tags)
    cum_url.append(single_data[0])
    cum_title.append(single_data[1])
    cum_area.append(single_data[2])
    cum_company.append(single_data[3])
    print('已完成第 {} 个'.format(l)) 
    l += 1

print('全部html已经读取完成，开始到处excel！\n')


data = {}
data['url'] = cum_url
data['title'] = cum_title
data['company'] = cum_company
data['area'] = cum_area

df = pd.DataFrame(data)

# 分离职位和公司信息
# df_company = df.iloc[1::2].reset_index()
# df_job = df.iloc[::2].reset_index()
# df_all = pd.concat([df_job,df_company],axis=1)


df.to_excel(r'D:\JunZhu\My Downloads\工作\51job_url202007.xlsx')

print('END')