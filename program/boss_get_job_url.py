# coding=utf-8
'''
@Date: 2020-06-01 16:04:41
@Author: YING
LastEditTime: 2020-09-02 20:33:40
'''

import os
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

# 读取本地html文件，输出url和job_title
def get_info(file_name,only_a_tags):
    url = []
    title = []
    area = []
    salary = []
    company = []

    with open(file_name,'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser", parse_only=only_a_tags)
    for i in soup:
        url.append(i.a['href'])
        title.append(i.a['title'])
        area.append(i.find_all('span')[2].contents[0])
        salary.append(i.find_all('span')[4].contents[0])
        company.append(i.find_all('a')[1].contents[0])
    return url,title,area,salary,company

# 主程序

# 切换工作目录
work_url = 'D:\JunZhu\My Downloads\工作'
html_path = 'boss运营列表20200902'

os.chdir(os.path.join(work_url,html_path))
file_lists = os.listdir('.')

only_a_tags = SoupStrainer("div",class_='job-primary')

cum_url = []
cum_title = []
cum_area = []
cum_salary = []
cum_company = []

print('一共有 {} 个html\n'.format(len(file_lists)))

l = 1
for i in file_lists:
    single_data = get_info(i,only_a_tags)
    cum_url += single_data[0]
    cum_title += single_data[1]
    cum_area += single_data[2]
    cum_salary += single_data[3]
    cum_company += single_data[4]

    print('已完成第 {} 个'.format(l)) 
    l += 1

    # print('已收集 {} 个职位信息'.format(len(cum_url)))

data = {}
data['url'] = cum_url
data['title'] = cum_title
data['area'] = cum_area
data['salary'] = cum_salary
data['company'] = cum_company

df = pd.DataFrame(data)

print('url已经全部读取完成,共收集到 {} 条信息!\n'.format(df.shape[0]))

if '数据' in html_path:
    choice = 1
elif '运营' in html_path:
    choice = 2

print('开始过滤关键字...\n')

# 再次切换工作目录
os.chdir(work_url)

# 过滤区域
list_area = pd.read_excel('boss_job_keywords.xlsx',sheet_name='area')
string_area = list_area['区域'].str.cat(sep='|')
filter_area = df['area'].str.contains(string_area)
df = df[~filter_area]
print('区域过滤完成，剩余 {} 条信息!\n'.format(df.shape[0]))

# 保留职位
if choice == 1:
    list_keep_job = pd.read_excel('boss_job_keywords.xlsx',sheet_name='data-keep-job')
elif choice == 2:
    list_keep_job = pd.read_excel('boss_job_keywords.xlsx',sheet_name='op-keep-job')
string_keep_job = list_keep_job['工作'].str.cat(sep='|')
filter_keep_job = df['title'].str.contains(string_keep_job)
df = df[filter_keep_job]
print('保留职位过滤完成，剩余 {} 条信息!\n'.format(df.shape[0]))

# 过滤职位
if choice == 1:
    list_quit_job = pd.read_excel('boss_job_keywords.xlsx',sheet_name='data-quit-job')
elif choice == 2:
    list_quit_job = pd.read_excel('boss_job_keywords.xlsx',sheet_name='op-quit-job')
string_quit_job = list_quit_job['不工作'].str.cat(sep='|')
filter_quit_job = df['title'].str.contains(string_quit_job)
df = df[~filter_quit_job]
print('不保留职位过滤完成，剩余 {} 条信息!\n'.format(df.shape[0]))

# 过滤公司
if choice == 1:
    list_company = pd.read_excel('boss_job_keywords.xlsx',sheet_name='data-company')
elif choice == 2:
    list_company = pd.read_excel('boss_job_keywords.xlsx',sheet_name='op-company')
string_company = list_company['公司'].str.cat(sep='|')
filter_company = df['company'].str.contains(string_company)
df = df[~filter_company]
print('公司过滤完成，剩余 {} 条信息!\n'.format(df.shape[0]))

# 过滤工资
list_salary = pd.read_excel('boss_job_keywords.xlsx',sheet_name='salary')
string_salary = list_salary['工资'].str.cat(sep='|')
filter_salary = df['salary'].str.contains(string_salary)
df = df[~filter_salary]
print('工资过滤完成，最后剩余 {} 条信息!\n'.format(df.shape[0]))

# 去重
df = df.drop_duplicates('url')
print('去重后剩余 {} 条信息!\n'.format(df.shape[0]))

if choice == 1:
    file_name = 'boss_url数据 '+ str(pd.to_datetime('today').strftime('%y-%m-%d')) + '.xlsx'
elif choice == 2:
    file_name = 'boss_url运营 '+ str(pd.to_datetime('today').strftime('%y-%m-%d')) + '.xlsx'

df.to_excel(file_name,index = False)

print('END')