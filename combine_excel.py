import os

import pandas as pd
import xlwings as xw

filelist = []

for root, dirs, files in os.walk(r'C:\Users\Dragon\Desktop\报送数据（2019年3月）', topdown=False):
    for name in files:
        str = os.path.join(root, name)
        if str.split('.')[-1] == 'xls':
            filelist.append(str)

print('\nfind all files,total {} files!'.format(len(filelist)))

# print(filelist)
df = pd.DataFrame()

print('\nbegin to merge xls:')
for i in filelist:
    app = xw.App(visible=False, add_book=False)
    xls = app.books.open(i)
    sht = xls.sheets[0]
    df_tempt = sht.range('A1').options(pd.DataFrame, expand='table').value
    df = df.append(df_tempt)

    xls.close()
    app.quit()
    print('{} is added'.format(i.split('\\')[-1]))

print('\nall xls is merged')

df['身份证号'] = df['身份证号'].str.upper()
# df.drop('逾期',axis=1).to_csv('pandas.txt', header=None, sep=',')
df.drop_duplicates(subset=['合创信用代码', '合同编号', '放贷时间']).drop(
    '逾期', axis=1).to_excel(r'C:\Users\Dragon\Desktop\报送数据（2019年3月）\wancheng.xlsx')

print('\nend')
