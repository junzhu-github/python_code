# -*- coding: utf-8 -*-

# @author: ying


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# #import data
# def import_data():
#     with pd.ExcelFile('users.xlsx') as x:
#         df = pd.read_excel(x,sheetname = 'Sheet1')
#     return df

# #data standardization
# def data_standardization(dataset):
#     min_col = np.amin(dataset[:,1:],axis = 0)
#     ptp_col = np.ptp(dataset[:,1:],axis = 0)
#     dataset[:,1:] = (dataset[:,1:]-min_col) / ptp_col
#     return dataset

# def run_main():
       
#     #import data
#     dataset = import_data()
#     # print(dataset['money'])

#     dataset = dataset.as_matrix()
#     dataset_std = data_standardization(dataset)

#     x = dataset_std[:,1]
#     y = dataset_std[:,2]
#     z = dataset_std[:,3]


#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     ax.scatter( x, y, z, c='b', marker='o')

#     ax.set_xlabel('money')
#     ax.set_ylabel('date')
#     ax.set_zlabel('fre')

#     plt.show()
    

# if __name__ == '__main__':
#     run_main()

#-----------------------------------------------------------------

# a = np.arange(12).reshape(4,3)

# print(a)

# x = np.mean(a,axis = 0).tolist()[0]
# print('='*10)

# print(x)

# y = [x]
# print('='*10)

# print(type(y))

# print(np.random.randint(0, 13))

# # print(type(a.tolist()))
# print('='*10)

# b = np.mean(a,axis=0).tolist()[0]

# print(b)
# print('='*10)

# print(len([b]))
# print('='*10)

# c = np.mean(a,axis=0)
# print(c)
# print('='*10)

# d = [2]
# d = np.asarray(d)
# print(d)

# for i in range(a.shape[0]):
#     e = np.power((d-a[i,:]),2)
#     print(e)

# d[0] = 5
# print(d)

# d = np.append(d,10)
# print(d)

# e = np.random.randint(10,high = 100,size = (10,3))
# print(e)
# print('='*50)

# print(e[0,:])
# print('='*50)

# print(e[0,:].tolist()[0])
# print('='*50)


# print('|'*50)
# print('0.type_e: ',type(e))
# print('1.e: ',e)

# print('2.e[0,:]: ',type(e[0,:]))
# print('3.e[0,:].tolist(): ',type(e[0,:].tolist()))


# print('4.e[0,:].tolist()[0]: ',e[0,:].tolist()[0])
# print('|'*100)


# coding: utf-8

# ### 导入库

# # In[2]:


# import os
# import pandas as pd


# # 切换工作目录

# # In[5]:


# os.chdir(r'D:\小鸡理财\OneDrive\python')

# # 导入excel
# # In[7]:


# with pd.ExcelFile('a1.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'原始数据')
#     df2 = pd.read_excel(xlsx,'业务员')
    
# print('---------------------------read_ok---------------------------')

# # 给需要合并的两张表做个标记，方便后面统计
# # In[10]:

# # df3 = df2[df2.duplicated('手机号码')]['手机号码'].unique()

# # print(df3)


# # reslut = pd.merge(df1,df2,how = 'left',left_on = '手机号',right_on = '手机号码')




# # with pd.ExcelWriter('a1-1.xlsx') as writer:
# #     reslut.to_excel(writer,sheet_name = 'result',index = False)

   
# print('---------------------------write_ok---------------------------')

# gp = df2.groupby('手机号码').agg(np.size)

# print(gp.sort_values(by='size',ascending=False))

# def funx(x):
#     def funy(y):
#         return x*y
#     return funy(y)      #注意带参数函数的返回格式

# i = funx(5)(8)

# print(i)

# def fun1():      #第一层函数
#     print('fun1 is working...')
#     def fun2():      #第二层函数
#         print('fun2 is working......')
#     return fun2()      #调用fun2

# fun1()

# def Fun1():
#     x = 5
#     print('0:',x)
#     def Fun2():
#         nonlocal x
#         print('1:',x)
#         x *= 5
#         print('2:',x)
#         return x
#     return Fun2

# a = Fun1()


# print(a())
# print('='*10)

# # print(type(a()))
# # print(Fun1()())

# print('='*10)
# print(a())

# p = {1,2,3,4,5}
# o = {1,2,6}

# p_o = p - o

# print(p_o)

# print('='*50)

# p_1 = {1,2,3,4,5}
# o_1 = {1,2,6}

# p_o_1 = p & o

# print(p_o_1)
# list1 = [1,2,3,4,5] 

# x1 = np.random.shuffle(list1)   #输出None
# print('x:\n',list1)

# arr = np.arange(9).reshape(3,3)  
# print('x:\n',arr)
# x2 = np.random.shuffle(arr) #对于多维数组，只沿着第一条轴打乱顺序  
# print('x:\n',arr)

# x3 = np.random.choice(5,(2,3))  #生成一个2x3数组  
# print('x:\n',x3)

# x4 = np.random.choice(np.array(['a','b','c','f']))  #生成一个np.array(['a','b','c','f']中随机元素  
# print('x:\n',x4)

# x5 = np.random.choice(np.array(['a','b','c','f']),(2,3))    #生成2x3数组  
# print('x:\n',x5)

# x6 = np.random.choice(5,p=[0,0,0,0,1])  #生成的始终是4 
# print('x:\n',x6)

# x7 = np.random.choice(5,3,p=[0,0.5,0.5,0,0])    #生成shape=3的一维数组，元素取值为1或2的随机数
# print('x:\n',x7)

# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings'],
#          'Rank': [1, 2, 2, 3, 3],
#          'Points':[876,789,863,673,741]}

# df = pd.DataFrame(ipl_data)

# print(df)
# print('='*50)

# gp = df.groupby(by = 'Team')

# # for name,group in gp:      #类似字典
# #     print(name)
# #     print(group)

# # print(gp.agg(np.size))

# df1 = df[['Rank','Team']].sort_values(by = 'Rank',ascending = False).drop_duplicates('Team')
# print(df1)
# print('='*50)

# df2 = df[['Rank','Team']].drop_duplicates('Team')
# print(df2)
# print('='*50)

# df3 = gp.apply(lambda t: t[t.Rank == t.Rank.max()])
# print(df3)

# ipl_data1 = {'Team': [ 'Devils', 'Devils','Riders', 'Riders', 'Kings'],
#          'Rank': [1, 2, 2, 3, 3],
#          'Points':[876,789,863,673,741]}

# df1 = pd.DataFrame(ipl_data1)

# print(df1.Points == df.Points)

# df1 = pd.DataFrame({'a': range(-5,0), 'b': range(10,15), 'c': range(20,25)})
# df2 = pd.DataFrame({'a': range(-5,0), 'b': range(10,15), 'c': [20] + list(range(101,105))})

# condition = df1['c'] != df2['c']

# diff1 = df1[condition]

# diff2 = df2[condition]

# x = diff1.merge(diff2, on=['a','b'], suffixes=('_before', '_after'))


# print(x)
#-------------------------------------------------------------------------------

# with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
#     df3 = pd.read_excel(xlsx,'投资')
   
# print('---------------------------read_ok---------------------------')

# print(df1.shape)

# df4 = pd.merge(df1,df2,how = 'left',on = '手机号码')
# df5 = pd.merge(df4,df3,how = 'left',on = '用户名')

# print('---------------------------merge_ok---------------------------')

# print(df5.shape)

# if df1.shape[0] == df5.shape[0]:
#     print('begin to write!!!')
#     df5.to_csv('001.csv')

    
# print('---------------------------write_ok---------------------------')

#-------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'a':[4,2,1,3,2],
#     'b':[i for i in range(5) if i < 10],
#     })

# print(df['b'])

# print(df['b'].notnull())

# df = df[df['b'].notnull()]
# print(df)

# gp = df.groupby(by = 'a')

# x = gp.agg(np.size)

# df.set_index('a',inplace = True)
# df['count'] = x

# print(x)
# print('='*50)

# print(df)

# s = pd.Series([1,2,3,4,5,6])
# print(df)

# df = df.set_index('a')

# print(df)


# df = pd.read_csv('02.csv')

# gp = df.groupby('A').agg({'A':np.size})

# gp.to_csv('002.csv')

# print(gp.head())

# class New_int(int):
#     def __add__(self,other):
#         print(self)
#         print('*'*50)
#         print(other)
#         return int.__sub__(self,other)

# a = New_int(1)
# print('-'*50)
# b = New_int(3)
# print('-'*50)
# print(a+b)

# df = pd.DataFrame({
#     'a':[4,2,1,3,2],
#     'b':[i for i in range(5) if i < 10],
#     })

# print(df)

# import tkinter as tk

# window = tk.Tk()
# window.title('my window')
# window.geometry('200 x 100')

# l = tk.Label(window,
#     text = 'OMG!,this is TK!',
#     bg = 'green',
#     font = ('Arial',12),
#     width = 15,
#     height = 2)

# l.pack()

# window.mainloop()

# df = pd.DataFrame ({'a' : np.random.randn(6),
#     'b' : ['foo', 'bar'] * 3,
#     'c' : np.random.randn(6)})

# def my_test(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
 
# # df['Value'] = df.apply(my_test(df['a'], df['c']))
# # df['Value'] = df.apply(my_test(df['a'], df['c']))
# df['Value'] = df.apply(lambda row: my_test(row['a'], row['c']), axis=1)

# print(df)

# lst = [1,2,3,1,2,3,4]
# s = pd.DataFrame({'a':[1,2,3,10,20,30,40],
#     'b':[1,1,1,1,1,1,1],
#     'c':[1,2,3,1,2,3,4]}
#     )

# print(s)
# print('='*50)

# g = s.groupby(by = 'c')

# print(g.first())
# print('='*50)

# print(g.last())
# print('='*50)

# print(g.sum())

# l1 = ['a','b']
# l2 = pd.date_range(start='20160101',end='20160103')
# l3 = []


# for i in l1:
#     for j in l2:
#         s = i + '+' + str(j)
#         l3.append(s)
# print(l3)

# df = pd.DataFrame({'name':l3})

# temp = df['name'].str.split('+', expand=True)

# df0['Year'] = df0['Year'].astype('datetime64')


# df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils',],
#          'Rank': [1, 2, 2,],
#          'Year': [2014,2015,2014],
#          'Points':[876,789,863]})


# gp = df.groupby('Team').transform(np.size)

# print(gp)

# left2 = pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','c','e'],columns=['Ohio’','Neveda']) 

# right2 = pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['b','c','d','e'],columns=['Missouri','Alabma'])
# print(left2) 
# print(right2) 
# result = pd.merge(left2,right2,how='outer',left_index=True,right_index=True) 
# print(result)

# np.random.seed(0)
# df = pd.DataFrame({'state': ['CA', 'WA', 'CO', 'AZ'] * 3,
#                    'office_id': list(range(1, 7)) * 2,
#                    'sales': [np.random.randint(100000, 999999)
#                              for _ in range(12)]})

# print(df)
# print('='*50)

# state_office = df.groupby(['state', 'office_id']).agg({'sales': 'sum'})
# print(state_office)
# print('='*50)

# state_pcts = state_office.groupby(level=0).apply(lambda x:100 * x / float(x.sum()))
# print(state_pcts)
# print('='*50)

# state = state_office.groupby(level=0).apply(lambda x:x.sum())
# print(state)
# print('='*50)

# import time


# timeStamp = 1381419600
# time_local = time.localtime(timestamp)

# print(time_local)
#coding:UTF-8



# import time

# def time_change(x):
#     timestamp = x
#     time_local = time.localtime(timestamp)
#     dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
#     return dt


# os.chdir(r'D:\小鸡理财\OneDrive\python')


# with pd.ExcelFile('backmoney.xlsx') as xlsx:
#     df = pd.read_excel(xlsx,'Sheet1')
# print('rd_ok')

# df['new_add_time'] = df['add_time'].apply(time_change)
# df['new_deadline'] = df['deadline'].apply(time_change)
# df['ben_jin'] = df['next_repay'] - df['interest']

# print('begin_write')

# print(df.info())

# df.to_excel('070707.xlsx',index=False)  


# df = pd.DataFrame([[0,1435, np.nan],
#                    [0,1435, 'YES'],
#                    [0,1435, np.nan],
#                    [1,1435, np.nan],
#                    [1,1435, 'COOL'],
#                    [1,1817, np.nan],
#                    [1,1817, 'YES']],
#                    columns=['x','Number', 'Other'])

# print(df)

# gp = df.groupby(['x','Number']).fillna(method='ffill')

# print(gp)


# import os
# import re
# # import datetime,time
 
# # tm1 = time.localtime(time.time())
# # STRDATE = '20161205'#time.strftime("%Y%m%d", tm1) 
# # INPUTPATH = u"E:\\对接wind资讯\\" + STRDATE

# os.chdir(r'C:\Users\Xiaoji\Downloads\新建文件夹')
# print('1_ok')
 

# def readxmldata():
#     #strstock = os.path.join(INPUTPATH,"GBXX_"+STRDATE+".XML")
#     # strstock = os.path.join(INPUTPATH,"ZQXX_"+STRDATE+".XML")
#     fp = open('01.xls', "rb")


#     file_data = fp.read()
#     # print(file_data)

#     data0 = re.findone(b'<Row>([\s\W\w\S]*?)</Row>',file_data)
#     print(len(data0))

#     # data1 = re.findall(b'<Data ss:Type="String">([\s\W\w\S]*?)</Data></Cell>',file_data)
#     # print (len(data1))
#     # print (data1[:10])


#     # len_axis = 50
#     # re_data=[]
#     # for ii in range(0,int(len(data1)/len_axis)):
#     #     re_data.append(data1[ii*len_axis:(ii+1)*len_axis])
#     # print (int(len(data1)/len_axis)-1)
#     # print (re_data[int(len(data1)/len_axis)-1],len(re_data))
 
# if __name__ == '__main__':
#     readxmldata()

# ------------------------------------------------------------------

# os.chdir(r'C:\Users\Xiaoji\Downloads\新建文件夹')

# df = pd.read_table('01.xls')
# print(df.head(10))

# ------------------------------------------------------------------

# import re

# # regular expression
# pattern1 = "cat"
# pattern2 = "bird"
# string = "dog runs to cat"
# print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# print(re.search(pattern2, string))  # None

# print(re.search(r"\B runs \B", "dog   runs  to cat"))

# print('usage of 3 operators /, // and % in python 3.4')
# print('1). usage of /')
# print ('10/4 = ', 10/4)
# print ('-10/4 = ', -10/4)
# print ('10/-4 = ', 10/-4)
# print ('-10/-4 = ', -10/-4)

# print('\n2). usage of //')
# print ('10//4 = ', 10//4)
# print ('-10//4 = ', -10//4)
# print ('10//-4 = ', 10//-4)
# print ('-10//-4 = ', -10//-4)

# print('\n3). usage of %')
# print ('10%4 = ', 10%4)
# print ('-10%4 = ', -10%4)
# print ('10%-4 = ', 10%-4)
# print ('-10%-4 = ', -10%-4)

# ------------------------------------------------------------------

print(1+1)

print('hello')