# -*- coding: utf-8 -*- 

# @author: ying


import os
import re
import sys
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

#

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
#--------------

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

#--------------

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



# os.chdir(r'C:\Users\Xiaoji\Downloads\新建文件夹')

# df = pd.read_table('01.xls')
# print(df.head(10))



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

# from pyspark import SparkConf , SparkContext
# conf = SparkConf().setMaster('local').setAppName('MyApp')
# sc = SparkContext(conf = conf)

# print(sc)

# study from here.

# def hannoi(n,x,y,z):
#     if n == 1:
#         print(x,'->',z)
#     else: 
#         hannoi(n-1,x,z,y)
#         print(x,'-->',z)
#         hannoi(n-1,y,x,z)

# num = int(input('number:  '))

# hannoi(num,'x','y','z')

# ---------------------------------------------------------------

# dict1 = {'李宁':'一切皆有可能','耐克':'just do it','阿迪达斯':'impossible is nothing'}

# dict2 = dict((('f',70),('i',105),('s',115),('h',104),('c',67)))

# dict3 = dict(小甲鱼='让编程改变世界',哈哈='呵呵哈哈哈')

# dict4 = dict(one='1',two='2',three='3')

# dict5 = dict('1'='one','2'='two')

# dict1.fromkeys((1,2,3),('good','better','best'))

# ---------------------------------------------------------------

# list1 = [0,1,2,3,4,5,5,3,1]

# for i in list1:
#     for j in list1.remove(i):
#         if i == j:

# ---------------------------------------------------------------           

# f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")

# boy = []
# girl = []
# num = 1

# for i in f:
#     if i[:3] == '小甲鱼':
#         boy.append(i.split('：')[1])
    
#     if i[:3] == '小客服':
#         girl.append(i.split('：')[1])


#     if i[:3] == '===':
#         boy_file = "boy_" + str(num) + ".txt"
#         girl_file = "girl_" + str(num) + ".txt"
        
#         b = open(boy_file,"w")
#         b.writelines(boy)
#         b.close()
#         print("boy_file saved")
        
#         g = open(girl_file,"w")
#         g.writelines(girl)
#         g.close()
#         print("girl_file saved")
      
#         boy = []
#         girl = []
#         num += 1


# boy_file = "boy_" + str(num) + ".txt"
# girl_file = "girl_" + str(num) + ".txt"
        
# b = open(boy_file,"w")
# b.writelines(boy)
# b.close()
# print("last boy_file saved")

# g = open(girl_file,"w")
# g.writelines(girl)
# g.close()
# print("last girl_file saved")
  
# print('byebye!')

# --------------------------------------------------------------- 

# f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
# l = [f.read().split()]

# boy = []
# girl = []
# num = 1
# boy_file = "boy_{0}.txt".format(num)
# girl_file = "girl_{0}.txt".format(num)


# for i in range(len(l[0])):
#     list1 = l[0][i]
# #    print(list1)
# #    print('-'*50)
    
#     if list1[:3] == '小甲鱼':
#         boy.append(list1.split('：')[1])
    
#     if list1[:3] == '小客服':
#         girl.append(list1.split('：')[1])


#     if list1[:3] == '===':
#         b = open(boy_file,"w")
#         b.write("\n".join(boy))
#         b.close()
#         print("boy_file saved")
        
#         g = open(girl_file,"w")
#         g.write("\n".join(girl))
#         g.close()
#         print("girl_file saved")
      
#         boy = []
#         girl = []
#         list1 = []
#         num += 1
#         boy_file = "boy_{0}.txt".format(num)
#         girl_file = "girl_{0}.txt".format(num)


# b = open(boy_file,"w")
# b.write("\n".join(boy))
# b.close()
# print("last boy_file saved")

# g = open(girl_file,"w")
# g.write("\n".join(girl))
# g.close()
# print("last girl_file saved")

# print('byebye!')

# --------------------------------------------------------------- 

# f = open('123456789.txt','w')

# l = ['1','2','3']

# f.writelines(l)

# f.close()

# --------------------------------------------------------------- 

# def save_file(boy,girl,num):
#     boy_file = "boy_" + str(num) + ".txt"
#     girl_file = "girl_" + str(num) + ".txt"
    
#     b = open(boy_file,"w")
#     b.writelines(boy)
#     b.close()
#     print("boy_file saved")
    
#     g = open(girl_file,"w")
#     g.writelines(girl)
#     g.close()
#     print("girl_file saved")
 
# def split_file(file_name):
#     f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
    
#     boy = []
#     girl = []
#     num = 1
    
#     for i in f:
#         if i[:3] == '小甲鱼':
#             boy.append(i.split('：')[1])   
#         if i[:3] == '小客服':
#             girl.append(i.split('：')[1]
#         if i[:3] == '===':
#             save_file(boy,girl,num)
            
#             boy = []
#             girl =[]
#             num += 1
    
#     save_file(boy,girl,num)
#     f.close()  
#     print('byebye!')


# split_file('111.txt')

# --------------------------------------------------------------- 

# import pickle

# first_list = [1,2,'a','b',['一','二']]

# f = open('my_list.pkl','wb')
# pickle.dump(first_list,f)
# f.close()

# j = open('my_list.pkl','rb')
# second_list = pickle.load(j)
# print(second_list)

# --------------------------------------------------------------- 

# class Person:
#     def hell(self):
#         print('father is running...')


# class Other:
#     def hello(self):
#         print('other is running')

    
# class Child(Person):
#     def hello(self):
#         super().hell()
#         print('child is running...')

# a = Person()
# a.hell()

# ---------------------------------------------------------------

# class B:
#     def pb(self):
#         print('nozuonodie')

# B.pb(B)
# c = B()
# c.pb()
# print(c.__dict__)

# ---------------------------------------------------------------

# class A(str):
#     def __new__(cls,string):
#         string = string.upper()
#         print('-'*20,string)
#         return str.__new__(cls,string)

# a1 = A('abc')
# print(a1)

# ---------------------------------------------------------------

# class C:
#     def __init__(self):
#         print(self)
#         print('__init__ is running')
#     def __del__(self):
#         print('__del__ is running')

# c1 = C()

# c2 = C()

# ---------------------------------------------------------------  

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

# ---------------------------------------------------------------  

# class Try_int(int):
#     def __add__(self,other):
#         print(type(self))
#         print('*'*50)
#         print(type(other))
#         return int(self) + int(other)

# a = Try_int(1)
# print('-'*50)
# b = Try_int(3)
# print('-'*50)
# print(a+b)

# ---------------------------------------------------------------  

# class Try_int(int):   
#     def __add__(self,other):
#         return Try_int.__add__(self,other)


# a=Try_int(5)
# b=Try_int(10)

# print(a+b)

# --------------------------------------------------------------- 

# class A(int):
#     def __add__(self,other):
#         print('A is running')
#         return int(self) + int(other)
    
# a1 = A(5)
# print(a1)
# print('-'*5)
# a2 = A(10)
# print(a2)
# print('-'*10)
# print(a1+a2)

# --------------------------------------------------------------- 

# class Rec:
#     def __init__(self,width = 0,heig = 0):
#         self.width = width
#         print(self.width,'-')
#         self.heig = heig
#         print(self.heig)
       
#     def __setattr__(self,name,value):
#         print('__setattr__')
#         if name == "square":
#             print(value)
#             self.width = value
#             self.name = value
#         else:
#             print("else")
#             #self.name = value
#             super().__setattr__(name,value)
            
#     def getArea(self):
#         return self.width * self.heig
        
# a = Rec(4,5)
# print('-'*50)
# a.square = 10
# print(a.getArea())

# --------------------------------------------------------------- 

# string = 'hello|world'
# it =iter(string)
# print(it)
# for i in it:
#     print(next(it))

# --------------------------------------------------------------- 

# class Fib(object):
#     def __init__(self,n = 100):
#         print('0'*20)
#         self.a = 0
#         self.b = 1
#         self.n = n
#         print('-'*50)
        
#     def __iter__(self):
#         print('1'*20)
#         return self
            
#     print('/'*50)
    
#     def __next__(self):
#         print('2'*20)
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > self.n:
#             print('3'*20)
#             raise StopIteration
#         print('4'*20)
#         return self.a
    
# fib = Fib(3)
# print(next(fib))
# print(next(fib))
# print(next(fib))


# --------------------------------------------------------------- 

# import numpy as np 
# a = np.array([[1,2],[4,5]])
# b = np.arange(4).reshape(2,2)  

# print('a:\n',a)
# print('b:\n',b)


# print('-'*50)
# print(a*b)

# c_dot = np.dot(a,b)
# print('-'*50)
# print(c_dot)

# print('-'*50)
# print(np.sum(a,axis = 1))

# print('-'*50)
# print(a.reshape(1,4))

# print('-'*50)
# print(type(a))

# --------------------------------------------------------------- 

# f1 = open('01.mp3','rb')

# c = f1.readlines(
# print(c)

# f2 = open('01.txt','wb')

# f2.write(c)

# f2.close()

# --------------------------------------------------------------- 

# with open('out.txt','r') as f:
#     for each_line in f.readlines():
#         print(each_line,'|')
    
# f.close()

# --------------------------------------------------------------- 

# import pandas as pd
# import numpy as np

# df1 = pd.DataFrame(np.ones((3,4))*0,columns = ['A','B','C','D'])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns = ['A','B','C','D'])
# df3 = pd.DataFrame(np.ones((3,4))*2,columns = ['A','B','C','D'])
# df4 = pd.DataFrame(np.ones((3,4))*3,columns = ['E','B','C','D'])


# print(df1)
# print(df2)
# print(df3)
# print(df4)
# print('1-1'*50)

# res1 = pd.concat([df1,df2,df3,df4])

# print(res1)
# print('2-2'*50)

# res2 = pd.concat([df1,df2,df3,df4],ignore_index = True)

# print(res2)
# print('3-3'*50)

# res3 = pd.concat([df1,df2,df3,df4],join = 'inner',ignore_index = True)

# print(res3)
# print('4-4'*50)

# res4  = pd.merge(df3,df4,on = 'B',how = 'outer',suffixes = ('_df3','_df4'),indicator = True)

# print(res4)
# print('5-5'*50)

# --------------------------------------------------------------- 

# import os

# dir_num = 0
# zi = {}

# for root, dirs, files in os.walk(r'D:\OneDrive\python\book'):
# #    print(root)
# #    print(dirs)
# #    print(files)
# #    print('-'*50)
#     dir_num += len(dirs)
#     for i in files:
#         k = os.path.splitext(i)[1]
#         if k in zi:
#             zi[k] += 1
#         else:
#             zi[k] = 1

# for key,value in zi.items():
#     print('该文件夹下共有类型为【%s】的文件 %s 个' % (key,value))
# print('该文件夹下共有类型为【文件夹】的文件 %s 个' % (dir_num))

# --------------------------------------------------------------- 

# import numpy as np

# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 
# print(x)
# print('='*50)

# y = np.random.rand(4,3)
# print(y)
# print('='*50)

# print(y[x>5])
# print('='*50)

# print(y[(x>5) & (x%2==0)] )
# print('='*50)

# print(y[(x>5) | (x%2==0)] )
# print('='*50)

# print(np.extract(x>5,y))
# print('='*50)

# --------------------------------------------------------------- 

# b = [11,12,13,14,15]

# for i,j in enumerate(b):
#     print(i,':',j)

# --------------------------------------------------------------- 

# import csv

# # 数据集路径
# data_path = r'D:\wait_for_study\小象学院-python数据分析\第一周\codes\01\object\survey.csv'


# def run_main():
#     """
#         主函数
#     """
#     male_set = {'male', 'm'}  # “男性”可能的取值
#     female_set = {'female', 'f'}  # “女性”可能的取值

#     # 构造统计结果的数据结构 result_dict
#     # 其中每个元素是键值对，“键”是国家名称，“值”是列表结构，
#     # 列表的第一个数为该国家女性统计数据，第二个数为该国家男性统计数据
#     # 如 {'United States': [20, 50], 'Canada': [30, 40]}
#     # 思考：这里的“值”为什么用列表(list)而不用元组(tuple)
#     result_dict = {}

#     with open(data_path, 'r', newline='') as csvfile:
#         # 加载数据
#         rows = csv.reader(csvfile)
#         for i, row in enumerate(rows):
#             print(i,':',row)
# #            input('press enter to continue...')

#             if i == 0:
#                 # 跳过第一行表头数据
#                 continue

#             if i != 0:
#                 print('正在处理第{}行数据...'.format(i))
#             # 性别数据
#             gender_val = row[2]
#             country_val = row[3]

#             # 去掉可能存在的空格
#             gender_val = gender_val.replace(' ', '')
#             # 转换为小写
#             gender_val = gender_val.lower()

#             # 判断“国家”是否已经存在
#             if country_val not in result_dict:
#                 # 如果不存在，初始化数据
#                 result_dict[country_val] = [0, 0]

#             # 判断性别
#             if gender_val in female_set:
#                 # 女性
#                 result_dict[country_val][0] += 1
#             elif gender_val in male_set:
#                 # 男性
#                 result_dict[country_val][1] += 1
#             else:
#                 # 噪声数据，不做处理
#                 pass

#     # 将结果写入文件
#     with open('gender_country.csv', 'w', newline='', encoding='utf-16') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=',')
#         # 写入表头
#         csvwriter.writerow(['国家', '男性', '女性'])

#         # 写入统计结果
#         for k, v in list(result_dict.items()):
#             csvwriter.writerow([k, v[0], v[1]])

# if __name__ == '__main__':
#     run_main()

# --------------------------------------------------------------- 

# import math
# import random

# class Sample(object):
#     """
#         样本点类
#     """
#     def __init__(self, coords):
#         self.coords = coords    # 样本点包含的坐标
#         self.n_dim = len(coords)    # 样本点维度

#     def __repr__(self):
#         """
#             输出对象信息
#         """
#         return str(self.coords)


# def gen_random_sample(n_dim, lower, upper):
#     """
#         生成随机样本
#     """
#     sample = Sample([random.uniform(lower, upper) for _ in range(n_dim)])
#     return sample

# samples = [gen_random_sample(2, 0, 200) for _ in range(1000)]

# print(len(samples))

# --------------------------------------------------------------- 

# from sklearn import datasets
# from sklearn.model_selection import cross_val_predict
# from sklearn import linear_model
# import matplotlib.pyplot as plt

# lr = linear_model.LinearRegression()
# boston = datasets.load_boston()
# y = boston.target

# # cross_val_predict returns an array of the same size as `y` where each entry
# # is a prediction obtained by cross validation:
# predicted = cross_val_predict(lr, boston.data, y, cv=10)

# fig, ax = plt.subplots()
# ax.scatter(y, predicted, edgecolors=(0, 0, 0))
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()

# --------------------------------------------------------------- 

# df = pd.DataFrame(np.random.randn(1000,4),
#                   index = range(1000),
#                   columns = list('ABCD'))
# df = df.cumsum()
# #print(df)
# #df.plot()
# ax = df.plot.scatter(x ='A',y='B',color = 'lightblue')
# df.plot.scatter(x ='C',y='D',color = 'yellow',ax = ax)
# plt.show()

# --------------------------------------------------------------- 

# x = np.linspace(-3,3,50)
# y1 = x*2+1
# y2 = x**3

# #plt.figure()
# #plt.plot(x,y1)


# plt.figure(num = 3,figsize = (15,12))
# l1, = plt.plot(x,y1,label = 'L1')
# l2, = plt.plot(x,y2,linewidth = 5.0,linestyle = '--',label = 'L2')

# #plt.legend(handles = [l1,l2],labels = ['aaa','bbb'],loc = 'best')
# plt.legend()


# #plt.xlim(-4,4)
# #plt.ylim(0,30)

# plt.xlabel('i am x')
# plt.ylabel('i am y')

# x0 = 2
# y0 = x0*2+1
# plt.scatter(x0,y0,s=50,color='b')
# #plt.plot([x0,x0],[y0,0],'k--',lw=2.5)


# plt.annotate(r'$2 * %s +1 = %s$' %(x0,y0),
#              xy=(x0,y0),
#              xycoords='data',
#              xytext=(+30,-30),
#              textcoords='offset points',
#              fontsize=16,
#              arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
#              )

# plt.text(-2.7,3,
#          r'$this\ is\ some\ text$',
#          fontdict={'size':16,'color':'r'})

# #plt.xticks(np.linspace(-4,4,10))
# #plt.yticks([0,5,10,15,20,25,30],
# #           ['a','b','c','d','e','f','g'])

# #ax = plt.gca()
# #ax.spines['right'].set_color('none')
# #ax.spines['top'].set_color('none')
# #ax.xaxis.set_ticks_position('bottom')
# #ax.yaxis.set_ticks_position('left')
# #
# #ax.spines['bottom'].set_position(('data',0))
# #ax.spines['left'].set_position(('data',0))


# plt.show()

# --------------------------------------------------------------- 

# n = 1024
# X = np.random.randn(n)
# Y = np.random.randn(n)
# T = np.arctan2(Y,X) #for color value

# plt.scatter(X,Y,
#             c=T,
#             alpha = 0.5)

# plt.xlime((-2,2))
# plt.ylime((-2,2))

# plt.xticks(())
# plt.yticks(())


# plt.show()

# --------------------------------------------------------------- 

# x = np.random.randn(5)
# y = np.random.randn(5)

# plt.figure()

# plt.subplot(211)
# plt.plot(x,y)

# plt.subplot(234)
# plt.plot(y,x)

# plt.subplot(235)
# plt.plot(x,x)

# plt.subplot(236)
# plt.plot(y,y)

# --------------------------------------------------------------- 

# #需要展现的数据
# data = np.arange(100, 201)

# #设定x，y轴的最大、最小值
# plt.axis([0,100,50,300])

# #另一种设定x，y轴的最大、最小值的方式
# #plt.xlim(0,100)
# #plt.ylim(50,300)

# #设定x，y轴标记号
# plt.xticks(np.linspace(0,100,5,endpoint=True),['$zero$','$one$','one','two','three'])
# plt.yticks(np.linspace(50,300,5,endpoint=True))



#  #设定图表标题
# plt.title('Easy as 1, 2, 3')

# #设定x，y轴标签的字体，颜色
# plt.xlabel('x numbers',fontsize=14, color='red')      
# plt.ylabel('y numbers',fontsize=14, color='red')

# #在图表内增加公式
# plt.text(20, 250, r'$\mu=100,\ \sigma=15,\bigcap $')

# #设置背景网格线
# plt.grid(True)

# #设置打印线段的颜色、线宽、线型
# fig,ax = plt.subplots(1,1,figsize=(8,4))
# print(fig)
# print(ax)


# plt.show()

# --------------------------------------------------------------- 

# os.chdir(r'D:\JunZhu\My Downloads\code_data\code_data\data')

# df = pd.read_csv('stock_data_sample.csv',encoding = 'gbk')

# print(df.head())
# print('='*50)

# print(df.info())
# print('='*50)

# data = df[df['交易日期'] > pd.to_datetime('20160101')]
# print(data.head())
# print('='*50)

# --------------------------------------------------------------- 

# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#       'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)

# df['three'] = np.where(df['one'] >= df ['two'],'one','two')

# print(df)

#--------------------------------------------------------------- 

# dtnow = pd.to_datetime('today')

# timediff = pd.Timedelta(1,unit='d')
# dt_ff = dtnow + timediff

# df = dt_ff.strftime('%Y-%m-%d')
# print(df)

#--------------------------------------------------------------- 
# #stuff = {'name':'zad','age':39,'height':6*12+2}
# #print(stuff['name'])


# #!/usr/bin/python3 

# dict = {'Name': 'Runoob', 'Age': 27}

# print ("Age 值为 : %s" %  dict.get('Age'))  #how to use .get
# print ("Sex 值为 : %s" %  dict.get('Sex'))


# #!/usr/bin/python3

# dict = {'Name': 'Runoob', 'Age': 7}

# print ("Value : %s" %dict.items())


# def add(a,b):
#     sum = a+b
#     print(sum)
    
# add(5,4)    
# add(5,5)    


# def convert_number(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None
    
# print(convert_number("a"))


# import os
 
# try:
#      os._exit(0)
# except:
#      print ('die.')


# i = 5
# print(i)
# i = i+1
# print(i)

# s = this is a mutli-line string.\
# this is the second line.

# print(s)


# number=23
# guess=int(input('Enter an integer : '))
# if guess==number:
#     print ('Congratulations, you guessed it.') # New block starts here
#     print ("(but you do not win any prizes!)") # New block ends here
# elif guess<number:
#     print ('No, it is a little higher than that') # Another block
# # You can do whatever you want in a block ...
# else:
#     print ('No, it is a little lower than that')
# # you must have guess > number to reach here
# print ('Done')
# # This last statement is always executed, after the if statement is executed


# import sys
# print('the command line arguments are:')
# for i in sys.argv:
#     print(i)

# print('*'*10)
# print("\n\nThe pythonpath is ",sys.path,'\n')


# # 'ab' is short for 'a'ddress'b'ook
# ab = { 'Swaroop' :'swaroopch@byteofpython.info',
#       'Larry' : 'larry@wall.org',
#       'Matsumoto' : 'matz@ruby-lang.org',
#       'Spammer' : 'spammer@hotmail.com'
#       }

# print(len(ab),'-'*10)
# print("Swaroop's address is %s" %ab['Swaroop'])

# # Adding a key/value pair
# ab['Guido'] = 'guido@python.org'

# # Deleting a key/value pair
# del ab['Spammer']
# print('\nThere are %d contacts in the address-book\n' %len(ab))

# for name,address in ab.items():
#     print('Contact %s at %s' % (name, address))

# if 'Guido' in ab: # OR ab.has_key('Guido')
#     print("\nGuido's address is %s" % ab['Guido'])


# shoplist = ['apple', 'mango', 'carrot', 'banana']

# # Slicing on a list
# print('Item 1 to 3 is', shoplist[1:3])
# print('Item 2 to end is', shoplist[2:])
# print('Item 1 to -1 is', shoplist[1:-1])
# print('Item start to end is', shoplist[:])


# # Slicing on a string
# name = 'swaroop'
# print('characters 1 to 3 is', name[1:3])
# print('characters 2 to end is', name[2:])
# print('characters 1 to -1 is', name[1:-1])
# print('characters start to end is', name[:])


# print('Simple Assignment')   
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist # mylist is just another name pointing to the same object!
# del shoplist[0]
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# # notice that both shoplist and mylist both print the same list without
# # the 'apple' confirming that they point to the same object

# print('\nCopy by making a full slice')
# mylist = shoplist[:] # make a copy by doing a full slice
# del shoplist[0] # remove first item
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# # notice that now the two lists are different


# name = 'Swaroop'   # This is a string object
# if name.startswith('Swa'):
#     print('Yes, the string starts with "Swa"')
# if 'a' in name:
#     print('Yes, it contains the string "a"')
# if name.find('war') != -1:
#     print('Yes, it contains the string "war"')
# delimiter = '_*_'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))


# import os
# print(os.getcwd())   
# print(os.system('1'))

# os.chdir('C:\FDownload')
# print(os.getcwd())

# os.chdir('../dowloads')
# print(os.getcwd())

# os.mkdir('a')
# print(os.listdir())
# print(os.getcwd())

# os.makedirs('b/c/d')
# print(os.listdir())
# print(os.getcwd())

# os.remove('a/1.txt')
# os.removedirs('d')

# print(os.name)
# for i in os.listdir():
#     print(i)
    
# print('-'*100)

# os.rename('新建文本文档.txt','123.txt')

# for i in os.listdir():
#     print(i)


# import os 
# def robocopy(source, target, thread=8):
#     os.system( "robocopy %s %s /MT:%d /E"% (source.replace( "/", ""), target.replace( "/", ""), thread))
    
# robocopy( "D:/source_test", "D:/copy_test")


# #获取时间函数
# import time
# print
# (time.strftime('%Y%m%d%H%M%S'))


# import os

# a = os.getcwd()
# print(a)
# print(os.listdir('.'))
# print('-'*50)

# b = os.chdir('D:\\222')
# print(os.getcwd())

# os.makedirs('D:\\222\\home\\monthly\\daily')

# print(os.listdir())
# print('-'*50)



# print(a)
# print('-'*50)
# b = os.listdir('.')
# print(b)
# print(os.path.getmtime(a))


# try:
#     x = input('->')
#     print(int(x))
#     if x < 10:
#         raise("invalid x")
# except ValueError as x:
#     print(f"{x} is not a number")
# except("invalid"):
#     print(f"{x} is invalid")
# else:
#     print(f"number is {x}")


# list = ['a','b','c']
# print(f'before:{list}')

# list.append('d')
# print(f'after append:{list}')

# add = ['e','f']
# list.extend(add)
# print(f'after extend:{list}')

# list.insert(0,'0')
# print(f'after insert:{list}')




# list = ['a','b','c','e','f']
# print(f'before:{list}')

# pop1 = list.pop()
# print(f'pop1:{pop1}')
# print(f'after pop1:{list}')

# pop2 = list.pop(0)
# print(f'pop2:{pop2}')
# print(f'after pop2:{list}')

# remove = list.remove('b')
# print(remove)
# print(f'after remove:{list}')

# del list[0]
# print(f'after del:{list}')

# del list
# print(f'after del:{list}')


# list = ['a','b','b','c','e','f']
# print(list.count('b'))

# print(list)


# import xlrd

# data= xlrd.open_workbook("C:\\Users\\ye\\xlrd\\nan.xlsx")
# print(data.nsheets)

# for s in data.sheets():
#     print('Sheet:',s.name)
#     print("行数：",s.nrows)
#     print("列数：",s.ncols)
#     for row in range(s.nrows):
#         print('the row is:',row)
#         values = []
#         for col in range(s.ncols):
#             print("row:",row," col:",col)
#             print(s.cell(row,col))
#             print("-",s.cell(row,col).value)
# #            values.append(s.cell(row,col).value)
# #        print(values)  


# import xlrd

# book = xlrd.open_workbook("D:\\小鸡理财\\OneDrive\\python\\xlrd\\learn_xlrd.xlsx")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))

# list = []

# for i in range(book.nsheets):
#     print("-{0}-".format(i))
#     sh = book.sheet_by_index(i)
#     print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
#     for rx in range(sh.nrows):
#         list.append(sh.row(rx))
#         print(sh.row(rx))
#     print(r"++++++++++")
    
# for n in list:
#     print(n)
   

# from xlrd import open_workbook

# wb = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls')

# for s in wb.sheets():
#     print('Sheet:',s.name)
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(','.join(values))
#     print()



# from xlrd import open_workbook
# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls')

# print("0 book.nsheets is {0}".format(book.nsheets))

# for sheet_index in range(book.nsheets):
#     print("1",book.sheet_by_index(sheet_index))
#     print("2",book.sheet_names())

# for sheet_name in book.sheet_names():
#     print("3",book.sheet_by_name(sheet_name))

# for sheet in book.sheets():
#     print("4",sheet)



# from xlrd import open_workbook,cellname

# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
# sheet = book.sheet_by_index(0)
    
# print("1 sheet.name:{}".format(sheet.name))
# print("2 sheet.nrows:{}".format(sheet.nrows))
# print("3 sheet.ncols:{}".format(sheet.ncols))
# print("-"*20)

# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         print('cellname:',cellname(row_index,col_index))        
#         print('cellvalue:',sheet.cell(row_index,col_index).value)
#         print("-"*10)



# from xlrd import open_workbook,XL_CELL_TEXT

# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
# sheet = book.sheet_by_index(1)

# cell = sheet.cell(0,0)

# print('1 cell:',cell)
# print('2 cell value:',cell.value)
# print('3 cell type:',cell.ctype)
# print(cell.ctype == XL_CELL_TEXT)

# for i in range(sheet.ncols):
#     print(sheet.cell_type(1,i))
#     print(sheet.cell_value(1,i))
#     print('-'*10)



# from xlrd import open_workbook
# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
# sheet0 = book.sheet_by_index(0)
# sheet1 = book.sheet_by_index(1)
# print(sheet0.row(0))
# print(sheet0.row_values(0))
# print(sheet0.col(0))
# print(sheet0.col_values(0))

# print()
# print(sheet0.row_slice(0,1))
# print(sheet0.row_slice(0,1,2))
# print(sheet0.row_values(0,1))
# print(sheet0.row_values(0,1,2))
# print(sheet0.row_types(0,1))
# print(sheet0.row_types(0,1,2))
# print()
# print(sheet1.col_slice(0,1))
# print(sheet0.col_slice(0,1,2))
# print(sheet1.col_values(0,1))
# print(sheet0.col_values(0,1,2))
# print(sheet1.col_types(0,1))
# print(sheet0.col_types(0,1,2))



# from xlrd import cellname, cellnameabs, colname
# print(cellname(0,0),cellname(10,10),cellname(100,100))
# print(cellnameabs(3,1),cellnameabs(41,59),cellnameabs(265,358))
# print(colname(0),colname(10),colname(100))



# from datetime import date,datetime,time
# from xlrd import open_workbook,xldate_as_tuple

# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
# sheet = book.sheets()[0]

# date_value = xldate_as_tuple(sheet.cell(3,2).value,book.datemode)
# print(sheet.cell(3,2).value)
# print(date_value)
# print(datetime(*date_value),'|',date(*date_value[:3]))
# print('-'*30)

# datetime_value = xldate_as_tuple(sheet.cell(3,3).value,book.datemode)
# print(sheet.cell(3,3).value)
# print(datetime_value)
# print(datetime(*datetime_value),'|',date(*date_value[:3]))
# print('-'*30)

# time_value = xldate_as_tuple(sheet.cell(3,4).value,book.datemode)
# print(sheet.cell(3,4).value)
# print(time(*time_value[3:]))

# #print(datetime(*time_value))



# from xlrd import open_workbook,error_text_from_code
# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
# sheet = book.sheet_by_index(0)

# print(error_text_from_code[sheet.cell(5,2).value])
# print(error_text_from_code[sheet.cell(5,3).value])



# from xlrd import open_workbook,empty_cell

# print('-',empty_cell.value,'-')


# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
# sheet = book.sheet_by_index(0)
# empty = sheet.cell(6,2)
# blank = sheet.cell(7,2)
# print(empty is blank, empty is empty_cell, blank is empty_cell)

# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls',formatting_info=True)
# sheet = book.sheet_by_index(0)
# empty = sheet.cell(6,2)
# blank = sheet.cell(7,2)
# print(empty.ctype,repr(empty.value))
# print(blank.ctype,repr(blank.value))



# from xlrd import open_workbook

# def cell_contents(sheet,row_x):
#     result = []
#     for col_x in range(2,sheet.ncols):
#         cell = sheet.cell(row_x,col_x)
#         result.append((cell.ctype,cell,cell.value))
#     return result

# sheet = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls').sheet_by_index(0)


# print('XL_CELL_TEXT',cell_contents(sheet,1))
# print('XL_CELL_NUMBER',cell_contents(sheet,2))
# print('XL_CELL_DATE',cell_contents(sheet,3))
# print('XL_CELL_BOOLEAN',cell_contents(sheet,4))
# print('XL_CELL_ERROR',cell_contents(sheet,5))
# print('XL_CELL_BLANK',cell_contents(sheet,6))
# print('XL_CELL_EMPTY',cell_contents(sheet,7))
# print()


# sheet = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls',formatting_info=True).sheet_by_index(0)

# print('XL_CELL_TEXT',cell_contents(sheet,1))
# print('XL_CELL_NUMBER',cell_contents(sheet,2))
# print('XL_CELL_DATE',cell_contents(sheet,3))
# print('XL_CELL_BOOLEAN',cell_contents(sheet,4))
# print('XL_CELL_ERROR',cell_contents(sheet,5))
# print('XL_CELL_BLANK',cell_contents(sheet,6))
# print('XL_CELL_EMPTY',cell_contents(sheet,7))



# from xlrd import open_workbook

# book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls',on_demand=True)
# for name in book.sheet_names():
#     if name.endswith('2'):
#         sheet = book.sheet_by_name(name)
#         print(sheet.cell_value(0,0))
#         book.unload_sheet(name)
#         print(sheet.cell_value(0,0))



# from tempfile import TemporaryFile
# from xlwt import Workbook

# book = Workbook()
# sheet1 = book.add_sheet('Sheet 1')
# book.add_sheet('Sheet 2')

# sheet1.write(0,0,'A1')
# sheet1.write(0,1,'B1')
# row1 = sheet1.row(1)
# row1.write(0,'A2')
# row1.write(1,'B2')
# sheet1.col(0).width = 10000

# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0,'Sheet 2 A1')
# sheet2.row(0).write(1,'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1,0,'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True

# book.save('simple.xls')
# book.save(TemporaryFile())



# def test(*params,exp):
#     print('参数的长度是:',len(params))
#     print('第二个参数是：',params[1])
    
# test(1,'工作簿',3.14,50,88,exp=60)



# def fun1():
#     print('fun1 is working...')
#     def fun2():
#         print('fun2 is working......')
#     fun2()
        
# fun1()



# def funx(x):
#     def funy(y):
#         return x*y
#     return funy

# i = funx(5)(8)
# print(i)


# def funx(x):
#     print(x)
#     def funy(y):
#         return x*y
#     funy
    

# u = funx(5)
# print(u)



# def fun1():
#     x = 5
#     def fun2():
#         nonlocal x
#         x *= x
#         return x
#     return fun2()

# i = fun1()
# print(i)



# def ds(x):
#     return 3*x+10

# print(ds(10) )

# a = lambda x : 3*x+10
# print(a(10))



# def odd(x):
#     return x % 2

# temp = range(10)

# show = map(odd,temp)

# list(show)



# def square(x):
#     return x ** 2

# temp = range(10)

# show = map(square,temp)

# list(show)



# def cheng(x):
#     result = 1
#     for i in range(1,x+1):
#         result = result * i
        
#     return result
        

# num = int(input("输入一个数字:"))


# print(num,"的阶乘是:",cheng(num))


# def cheng(x):
#     if x == 1:
#         return 1
#     else:
#         return x * cheng(x-1)
    
# num = int(input("输入一个数字:"))


# print(num,"的阶乘是:",cheng(num))



# result = [1,1]

# a , b = 1 , 1

# for i in range(10):
#     a , b = b , a+b
#     result.append(b)
    
# print(result)



# def hannoi(n,x,y,z):
#     if n == 1:
#         print(x,'>',z)
#     else:
#         hannoi(n-1,x,z,y)
#         print(x,'>',z)
#         hannoi(n-1,y,x,z)
        
# num = int(input('please enter a number:'))

# hannoi(num,'X','Y','Z')



# from xlwt import Workbook

# book = Workbook()

# sheet1 = book.add_sheet('sheet 1',cell_overwrite_ok=True)
# sheet1.write(0,0,'original')
# sheet = book.get_sheet(0)
# sheet.write(0,0,'new')

# #sheet2 = book.add_sheet('sheet 2')
# #sheet2.write(0,0,'original')
# #sheet2.write(0,0,'new')

# book.save('1.xls')



# from datetime import date,time,datetime
# from decimal import Decimal
# from xlwt import Workbook,Style

# wb = Workbook()

# ws = wb.add_sheet('Type examples')

# ws.row(0).write(0,u'\xa3')
# ws.row(0).write(1,'Text')

# ws.row(1).write(0,3.1415)
# ws.row(1).write(1,15)
# ws.row(1).write(2,265)
# ws.row(1).write(3,Decimal('3.65'))

# ws.row(2).set_cell_number(0,3.1415)
# ws.row(2).set_cell_number(1,15)
# ws.row(2).set_cell_number(2,265)
# ws.row(2).set_cell_number(3,Decimal('3.65'))


# ws.row(3).write(0,date(2009,3,18))
# ws.row(3).write(1,datetime(2009,3,18,17,0,1))
# ws.row(3).write(2,time(17,1))
# ws.row(4).set_cell_date(0,date(2009,3,18))
# ws.row(4).set_cell_date(1,datetime(2009,3,18,17,0,1))
# ws.row(4).set_cell_date(2,time(17,1))


# ws.row(5).write(0,False)
# ws.row(5).write(1,True)
# ws.row(6).set_cell_boolean(0,False)
# ws.row(6).set_cell_boolean(1,True)

# ws.row(7).set_cell_error(0,0x17)
# ws.row(7).set_cell_error(1,'#NULL!')

# ws.row(8).write(
#     0,'',Style.easyxf('pattern: pattern solid, fore_colour green;'))
# ws.row(8).write(
#     1,None,Style.easyxf('pattern: pattern solid, fore_colour blue;'))
# ws.row(9).set_cell_blank(
#     0,Style.easyxf('pattern: pattern solid, fore_colour yellow;'))

# ws.row(10).set_cell_mulblanks(
#     5,10,Style.easyxf('pattern: pattern solid, fore_colour red;')
#     )

# wb.save('types.xls')



# from xlwt.Utils import rowcol_to_cell
# from xlwt import Workbook, easyxf


# book = Workbook()
# sheet = book.add_sheet('A Date')

# sheet.write(1,1,rowcol_to_cell(1,1))

# book.save('1111111.xls')



# dict1 = {'李宁':'一切皆有可能','耐克':'just do it','阿迪达斯':'impossible is nothing'}

# dict2 = dict((('f',70),('i',105),('s',115),('h',104),('c',67)))

# dict3 = dict(one='1',two='2',three='3')



# def gd(n):
#     list1 = []
#     string = str(n)
# #    length = len(string)
#     for each in string:
#         list1.append(each)
        
#     return list1

# a = gd(123456)
# print(a)



# import xlwt
# from datetime import datetime
 
# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
# style1 = xlwt.easyxf(num_format_str='yyyy/m/d h:mm;@')
 
# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test Sheet')
 
# ws.write(0, 0, 1234.56, style0)
# ws.write(1, 0, 1234.56,style1)
# ws.write(1, 2, datetime.now(),style1)
# ws.write(2, 0, 1)
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))
 
# wb.save('example.xls')



# import xlrd
# #import xlwt
# from xlutils.copy import copy

# copy_wb = xlrd.open_workbook("2.xls",formatting_info=True)
# copy_ws = copy_wb.sheets()[0]

# list1 = []

# for i in range(copy_ws.nrows):
#     list1.append(copy_ws.row_values(i)) 
    

# to_wb = xlrd.open_workbook("1.xls",formatting_info=True)
# to_ws = to_wb.sheet_by_index(0)

# new_wb = copy(to_wb)
# new_ws = new_wb.get_sheet(0)

# row_num = to_ws.nrows
   
# for j in range(len(list1)):
#     for k in range(len(list1[j])):
#         new_ws.write(row_num,k,list1[j][k])
#     row_num += 1
        
# new_wb.save("11.xls")
# print("SAVE SUCCESS!!!")



# import xlwt
# import xlrd
# from xlutils.copy import copy


# wb = xlwt.Workbook()
# ws = wb.add_sheet('destination')
# ws.write(0, 0, "Header")
# ws.write(0, 1, "CatalogNumber")
# ws.write(0, 2, "PartNumber")
# wb.save('destination.xls')



# oldWb = xlrd.open_workbook('1.xls', formatting_info=True)
# print(oldWb)             #<xlrd.book.Book object at 0x000000000315C940>

# newWb = copy(oldWb)
# print(newWb)                #<xlwt.Workbook.Workbook object at 0x000000000315F470>

# newWs = newWb.get_sheet(0)
# newWs.write(1, 0, "value1")
# newWs.write(1, 1, "value2")
# newWs.write(1, 2, "value3")
# print("write new values ok")

# newWb.save('1.xls');
# print("save with same name ok")



# f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
# l = [f.read().split()]

# boy = []
# girl = []
# num = 1
# boy_file = "boy_{0}.txt".format(num)
# girl_file = "girl_{0}.txt".format(num)


# for i in range(len(l[0])):
#     list1 = l[0][i]
# #    print(list1)
# #    print('-'*50)
    
#     if list1[:3] == '小甲鱼':
#         boy.append(list1.split('：')[1])
    
#     if list1[:3] == '小客服':
#         girl.append(list1.split('：')[1])


#     if list1[:3] == '===':
#         b = open(boy_file,"w")
#         b.write("\n".join(boy))
#         b.close()
#         print("boy_file saved")
        
#         g = open(girl_file,"w")
#         g.write("\n".join(girl))
#         g.close()
#         print("girl_file saved")
      
#         boy = []
#         girl = []
#         list1 = []
#         num += 1
#         boy_file = "boy_{0}.txt".format(num)
#         girl_file = "girl_{0}.txt".format(num)


# b = open(boy_file,"w")
# b.write("\n".join(boy))
# b.close()
# print("last boy_file saved")

# g = open(girl_file,"w")
# g.write("\n".join(girl))
# g.close()
# print("last girl_file saved")

# print('byebye!')



# f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")

# boy = []
# girl = []
# num = 1

# for i in f:
#     if i[:3] == '小甲鱼':
#         boy.append(i.split('：')[1])
    
#     if i[:3] == '小客服':
#         girl.append(i.split('：')[1])


#     if i[:3] == '===':
#         boy_file = "boy_" + str(num) + ".txt"
#         girl_file = "girl_" + str(num) + ".txt"
        
#         b = open(boy_file,"w")
#         b.writelines(boy)
#         b.close()
#         print("boy_file saved")
        
#         g = open(girl_file,"w")
#         g.writelines(girl)
#         g.close()
#         print("girl_file saved")
      
#         boy = []
#         girl = []
#         num += 1


# boy_file = "boy_" + str(num) + ".txt"
# girl_file = "girl_" + str(num) + ".txt"
        
# b = open(boy_file,"w")
# b.writelines(boy)
# b.close()
# print("last boy_file saved")

# g = open(girl_file,"w")
# g.writelines(girl)
# g.close()
# print("last girl_file saved")
  
# print('byebye!')



# try:
#     1/0
# except ZeroDivisionError as reason:
#     print('you are wrong because ' + str(reason))
# except OSError:
#     print('操作系统错误')
# finally:
#     raise ZeroDivisionError('除数为零的异常') x is {self.p.x},



# class Person():
#     def __init__(self):
#         pass      
#     def printx(self,x):
#         print('father\'x is: ',x)
        
        
# class Child():
#     def __init__(self,x,y):
#         self.x = Person().printx(x)
#         self.y = y
        
#     def printy(self):
#         print(f'y is {self.y}')


# a1 = Child(10,5)
# print('-'*50)
# a1.printy()



# class Person():
#     def __init__(self):
#         print('__init__')      
#     def printx(self,x):
#         print('father\'x is: ',x)
        
# p1 = Person()
# p1.printx(5)



# class CC():
#     def setXY(self,x,y):
#         self.x = x
#         self.y = y
#         print(self.x,self.y)

# c1 = CC()
# c1.setXY(11,99)

# del CC
# c1.setXY(11,99)
# c2 = CC



# import numpy as np 
# x = np.empty((3,2,1), dtype =  np.int)  
# print(x)
# print(x.ndim)



# # 从列表中获得迭代器  
# import numpy as np 
# list = range(5) 
# it = iter(list)  
# # 使用迭代器创建 ndarray 
# x = np.fromiter([0, 1, 2, 3, 4], dtype =  float)  
# print(x)

# import numpy as np
# l = list(range(5))


# x = np.fromiter(l,dtype = float)
# print(x)



# class A(str):
#     def __new__(cls,string):
#         string = string.upper()
#         return str.__new__(cls,string)

# a1 = A('abc')
# print(a1)



# class A:
#     def __new__(cls):
#         return 1
#     def __init__(self):
#         print('__init__ is running...')

# class B(A):
#     def __new__(cls,b):
#         b = b*10
#         return A.__new__(cls)


# a1 = A()
# print(a1)


# b1 = B(1)
# print(b1)



# class Word(str):
#     def __eq__(self,other):
#         return len(self) == len(other)
    
# a1 = Word('a')
# b1 = Word('b')

# print(a1==b1)



# class Word(str):
#     ''单词类，按照单词长度来定义比较行为''

#     def __new__(cls, word):
#         # 注意，我们只能使用 __new__ ，因为str是不可变类型
#         # 所以我们必须提前初始化它（在实例创建时）
#         if ' ' in word:
#             print("Value contains spaces. Truncating to first space.")
#             word = word[:word.index(' ')]
#             # Word现在包含第一个空格前的所有字母
#         return str.__new__(cls, word)

#     def __gt__(self, other):
#         return len(self) < len(other)
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __ge__(self, other):
#         return len(self) >= len(other)
#     def __le__(self, other):
#         return len(self) <= len(other)


# a1 = Word('abc')
# a2 = Word('abcd')

# print(a1 > a2)
# print(len('abc') < len('abcd'))



# import numpy as np 
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
# print('我们的数组是：'  )
# print(x )
# print('\n') 
# rows = np.array([[3,3],[0,1],[1,1]]) 
# cols = np.array([[0,2],[1,1],[0,0]]) 
# y = x[rows,cols]  
# print([rows,cols])
# print('这个数组的每个角处的元素是：'  )
# print( y)



# class Person():
#     def printx(self,x):
#         print('father\'x is: ',x)


         
# class Child(Person):
#     def __init__(self,x,y):
#         self.y = y
#     def printy(self):
#         Person.printx(x)      #！与上面的区别
#         print(f'y is {self.y}')

# a1 = Child(10,5)      #->  father'x is:  10
# a1.printy()      #->  y is 5



# y = int(input('give a year:'))

# if (y%4==0 and y%100 != 0) or ( y%400 == 0):
#     print('闰年')
# else:
#     print('no')



# import numpy as np 
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
# print(  '我们的数组是：' ) 
# print( x )
# print(  '\n'  )


# # 切片
# z = x[1:4,1:3]  
# print(  '切片之后，我们的数组变为：' ) 
# print( z )
# print(  '\n'  )
# # 对列使用高级索引 
# y = x[1:4,[1,2]] 
# print(  '对列使用高级索引来切片：' ) 
# print( y)



# import numpy as np 
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 

# print(x[x>5])



# import numpy as np 
# a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
# b = np.array([1.0,2.0,3.0])  

# print(  '第一个数组：' ) 
# print( a )
# print(  '\n' ) 
# print(  '第二个数组：')  
# print( b )
# print(  '\n'  )
# print(  '第一个数组加第二个数组：' )
# print(b-a)



# import numpy as np
# a = np.arange(0,60,5) 
# a = a.reshape(4,3)  
# print(  '原始数组是：' ) 
# print( a )
# print(  '\n'  )
# print(  '修改后的数组是：')  
# for x in np.nditer(a):  
#     print(x,end = ',')
# print()
# for y in np.nditer(a, flags =  ['external_loop'], order ='F'):
#     print(y)



# import numpy as np 
# a = np.arange(0,60,5) 
# a = a.reshape(3,4)  
# print(  '原始数组是：')  
# print( a )
# print(  '\n'  )
# print(  '修改后的数组是：')  
# for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):  
#     print( x,)



# import numpy as np 
# a = np.arange(0,60,5).reshape(4,3)

# b = np.array([1,  2,  3])  

# print(  '修改后的数组是：' ) 
# for x,y in np.nditer([a,b]):  
#     print  (x,':',y,end='||')



# X = np.reshape(np.arange(24), (2, 3, 4))
# print(X)

# print('-'*50)

# print(X[:,:,0])
# print(X.shape)



# for x in range(1,101):
#     m = lambda x: x if x % 2 == 1 else ','
#     print(m(x),end = '')



# #m = lambda i: i if i % 2 == 1 else continue



# x = 7
# i = 1
# flag = 0
	
# while i <= 100:
#     if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
#         flag = 1
#     else:
#         x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
#         i += 1
    
# if flag == 1:
#     print('阶梯数是：', x)
# else:
#     print('在程序限定的范围内找不到答案！')



# z = 0
# list1 = []

# for x in range(4):
#     for y in range(4):
#         if (x + y) >=2:
#             z = 8-(x+y)
#             list1.append((x,y,z))
            
# print(list1)



# print('red\tyellow\tblue')
# for red in range(0, 4):
#     for yellow in range(0, 4):
#         for green in range(2, 7):
#             if red + yellow + green == 8:
#                 # 注意，下边不是字符串拼接，因此不用“+”哦~
#                 print(red, '\t', yellow, '\t', green)



# for i in range(100, 1000):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp%10) ** 3
#         temp //= 10         # 注意这里要使用地板除哦~
#     if sum == i:
#         print(i)



# # 创建了三维的 ndarray
# import numpy as np
# a = np.arange(8).reshape(2,2,2)

# print( '原数组：')
# print( a)
# print( '\n')
# # 将轴 2 滚动到轴 0(宽度到深度)



# print( '调用 rollaxis 函数：')
# print( np.swapaxes(a,2,0))



# import numpy as np
# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])  

# # 对 y 广播 x
# b = np.broadcast(x,y)  
# # 它拥有 iterator 属性，基于自身组件的迭代器元组

# print( '对 y 广播 x：')
# r,c = b.iters
# print( r.next(), c.next())
# print( r.next(), c.next())
# print ('\n'  )
# # shape 属性返回广播对象的形状


# print( '广播对象的形状：')
# print( b.shape)
# print( '\n'  )
# # 手动使用 broadcast 将 x 与 y 相加
# b = np.broadcast(x,y)
# c = np.empty(b.shape)

# print( '手动使用 broadcast 将 x 与 y 相加：')
# print (c.shape)
# print( '\n'  )
# c.flat = [u + v for (u,v) in b]

# print( '调用 flat 函数：')
# print( c)
# print ('\n'  )
# # 获得了和 NumPy 内建的广播支持相同的结果

# print( 'x 与 y 的和：')
# print( x + y)



# import numpy as np  
# x = np.arange(9).reshape(1,3,3)

# print( '数组 x：')
# print( x)
# print( '\n'  )
# y = np.squeeze(x)

# print( '数组 y：')
# print( y)
# print( '\n'  )

# print( '数组 x 和 y 的形状：')
# print( x.shape, y.shape)



# list1 = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

# #member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

# add = [88,90,85,90,88]

# member = []

# for i in range(len(list1)):
#     member.append(list1[i])
#     member.append(add[i])
    
# for j in member:
#     print(j)



# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

# count = 0
# length = len(member)
# while count < length:
#     print(member[count], member[count+1])
#     count += 2



# list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
# print(list1)

# list2 = []
# for x in range(10):
#     for y in range(10):
#         if x%2==0 and y%2!=0:
#             list2.append((x, y))
# print(list2)            



# import numpy as np
# a = np.array([[1,2],[3,4],[5,6]])

# print( '第一个数组：')
# print( a)
# print( '\n' ) 

# print( '未传递 Axis 参数。 在插入之前输入数组会被展开。')
# print( np.insert(a,3,[11,12]))
# print( '\n'  )
# print( '传递了 Axis 参数。 会广播值数组来配输入数组。')

# print( '沿轴 0 广播：')
# print( np.insert(a,1,[11],axis = 0))
# print( '\n' ) 

# print( '沿轴 1 广播：')
# print( np.insert(a,1,11,axis = 1))



# import numpy as np
# a = np.arange(8)

# print( '第一个数组：')
# print( a)
# print( '\n'  )

# print( '将数组分为三个大小相等的子数组：')
# b = np.split(a,4)
# print( b)
# print( '\n' ) 

# print( '将数组在一维数组中表明的位置分割：')
# b = np.split(a,[4,7])
# print( b)



# import numpy as np
# a = np.array([[1,2],[3,4]])

# print( '第一个数组：')
# print( a)
# print( '\n'  )

# print( '未传递 Axis 参数。 在插入之前输入数组会被展开。')
# print( np.insert(a,3,[11,12]))
# print( '\n'  )
# print( '传递了 Axis 参数。 会广播值数组来配输入数组。')

# print( '沿轴 0 广播：')
# print( np.insert(a,1,[11],axis = 0))
# print( '\n'  )

# print( '沿轴 1 广播：')
# print( np.insert(a,1,11,axis = 1))



# import numpy as np
# a = np.array([5,2,6,2,7,5,6,8,2,9])

# print( '第一个数组：')
# print( a)
# print( '\n'  )

# print( '第一个数组的去重值：')
# u = np.unique(a)
# print( u)
# print( '\n'  )

# print( '去重数组的索引数组：')
# u,indices = np.unique(a, return_index = True)
# print( indices)
# print( '\n'  )

# print( '我们可以看到每个和原数组下标对应的数值：')
# print (a)
# print( '\n'  )

# print( '去重数组的下标：')
# u,indices = np.unique(a,return_inverse = True)
# print( u)
# print ('\n')

# print( '下标为：')
# print( indices)
# print( '\n'  )

# print( '使用下标重构原数组：')
# print( u[indices])
# print( '\n'  )

# print( '返回去重元素的重复数量：')
# u,indices = np.unique(a,return_counts = True)
# print( u)
# print( indices)



# # 密码安全性检查代码
# #
# # 低级密码要求：
# #   1. 密码由单纯的数字或字母组成
# #   2. 密码长度小于等于8位
# #
# # 中级密码要求：
# #   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# #   2. 密码长度不能低于8位
# #
# # 高级密码要求：
# #   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
# #   2. 密码只能由字母开头
# #   3. 密码长度不能低于16位

# symbols = r'`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = '0123456789'

# passwd = input('请输入需要检查的密码组合：')

# # 判断长度
# length = len(passwd)

# while (passwd.isspace() or length == 0) :
#     passwd = input("您输入的密码为空（或空格），请重新输入：")

# if length <= 8:
#     flag_len = 1
# elif 8 < length < 16:
#     flag_len = 2
# else:
#     flag_len = 3

# flag_con = 0

# # 判断是否包含特殊字符
# for each in passwd:
#     if each in symbols:
#         flag_con += 1
#         break
    
# # 判断是否包含字母
# for each in passwd:
#     if each in chars:
#         flag_con += 1
#         break

# # 判断是否包含数字
# for each in passwd:
#     if each in nums:
#         flag_con += 1
#         break    

# # 打印结果
# while 1 :
#     print("您的密码安全级别评定为：", end='')
#     if flag_len == 1 or flag_con == 1 :
#         print("低")
#     elif flag_len == 2 or flag_con == 2 :
#         print("中")
#     else :
#         print("高")
#         print("请继续保持")
#         break

#     print("请按以下方式提升您的密码安全级别：\n\
#     \t1. 密码必须由数字、字母及特殊字符三种组合\n\
#     \t2. 密码只能由字母开头\n\
#     \t3. 密码长度不能低于16位'")
#     break



# import numpy as np 
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
# print(  '我们的数组是：' ) 
# print( a )
# print(  '\n'  )
# print ( '调用 amin() 函数：'  )
# print( np.ptp(a)  )
# print(  '\n'  )
# print(  '再次调用 amin() 函数：'  )
# print( np.ptp(a,axis = 0)  )
# print( np.ptp(a,axis = 1)  )



# import numpy as np 
# from matplotlib import pyplot as plt 

# x = np.arange(1,11) 
# y = x**2+5
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y,'m') 
# plt.show()



# import numpy as np 
# import matplotlib.pyplot as plt 

# # 计算正弦和余弦曲线上的点的 x 和 y 坐标 
# x = np.arange(0,  3  * np.pi,  0.1) 
# y_sin = np.sin(x) 
# y_cos = np.cos(x)  

# # 建立 subplot 网格，高为 2，宽为 1  

# # 激活第一个 subplot
# plt.subplot(2,  1,  1)  
# # 绘制第一个图像 
# plt.plot(x, y_sin) 
# plt.title('Sine')  

# # 将第二个 subplot 激活，并绘制第二个图像
# plt.subplot(2,  1,  2) 
# # 绘制第二个图像
# plt.plot(x, y_cos) 
# plt.title('Cosine')  

# # 展示图像
# plt.show()



# from matplotlib import pyplot as plt 
# x =  [5,8,10] 
# y =  [12,16,6] 
# x2 =  [6,9,11] 
# y2 =  [6,15,7] 
# plt.bar(x, y, align =  'center') 
# plt.bar(x2, y2, color =  'g', align =  'center') 

# plt.title('Bar graph') 
# plt.ylabel('Y axis') 
# plt.xlabel('X axis') 
# plt.show()



# import numpy as np 
# a = np.array([1,2,3,4,5]) 
# np.save('outfile',a)
# b = np.load('outfile.npy')
# print(b)



# import numpy as np 

# a = np.array([1,2,3,4,5]) 
# np.savetxt('out.txt',a) 
# b = np.loadtxt('out.txt')  
# print(b)



# import pandas as pd
# import numpy as np

# dates = pd.date_range('20170101', periods=7)

# df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
# #print(df)

# #print(df.head())
# #print("" * 10)

# #print('*'*50)
# #print(range(len(df)))
# #print(df.tail(0))
# #print('*'*50)

# for i in range(len(df)):
#     print(df.tail(i+1))
#     print('-'*10)



# import pandas as pd
# import numpy as np

# dates = pd.date_range('20170101', periods=6)
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# print(df.iloc[0:2,0:2])
# print('-'*50)
# print(df)



# def gcd(x,y):
#     if x % y == 0:
#         return y
#     else:
#         while (x % y):
#             x , y = y , x % y
#         return y

# a = gcd(147,7)
# print(a)



# def bin1(x):
#     m = '1'
#     if x == 0:
#         return 0
#     while (x // 2 != 0):
#         m += str(x % 2)
#         x = x // 2
        
#     return m


# a1 = bin1(0)
# print(a1,'B')



# def Dec2Bin(dec):
#     temp = []
#     result = ''
    
#     while dec:
#         quo = dec % 2
#         dec = dec // 2
#         temp.append(quo)

#     while temp:
#         result += str(temp.pop())
    
#     return result

# print(Dec2Bin(62))

# def bin1(x):
#     m = ''
# #    if x == 0:
# #        return 0
#     while x:
#         m += str(x % 2)
#         x = x // 2
        
#     return m

# print(bin1(62))




# import numpy as np
# import pandas as pd

# s = pd.Series(np.random.randn(10),index = ['a','b','c','d','e','f','g','h','i','j'])

# print(s)
# print('-'*10)

# print(s.axes)
# print('-'*10)

# print(s.empty)
# print('-'*10)

# print(s.ndim)
# print('-'*10)

# print(s.values)
# print('-'*10)

# print(s.head(2))
# print('-'*10)

# print(s.tail(2))



# import numpy as np
# import pandas as pd

# data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack'],
#         'Age':[25,26,25,23,30,29,23],
#         'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]
#         }

# df = pd.DataFrame(data)

# print(df[1])
# print('-'*10)

# print(df.T)
# print('-'*10)

# print(df)
# print('-'*10)

# print(df.axes)
# print('-'*10)

# print(df.dtypes)
# print('-'*10)

# print(df.empty)
# print('-'*10)

# print(df.ndim)
# print('-'*10)

# print(df.shape)
# print('-'*10)

# print(df.size)
# print('-'*10)

# print(df.values)
# print('-'*10)

# print(df.head(2))
# print('-'*10)

# print(df.tail(2))
# print('-'*10)



# def Hui(x):
#     for i in range(len(x)):
#         if x[i] == x[(len(x)-1)-i]:
#             continue
#         else:
#             return 'not huiwenlian'
#     return 'huiwenlian111'


# str1 =input('give a string:')
# print(Hui(str1))



# zimu = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# shuzi = '0123456789'
# kongge = ' '

# z = 0
# s = 0
# k = 0
# q = 0

# s1 = input('pass a string:')

# for i in s1:
#     if i in zimu:
#         z +=1
#     elif i in shuzi:
#         s +=1
#     elif i in kongge:
#         k +=1  
#     else:
#         q += 1

# print(f'zimu {z} , shuzi {s} , kongge {k} , qita {q} .')



# car = 'Hi'

# def fun1():
#     global var
#     var = 'Baby'
#     return fun2(var)

# def fun2(var):
#     var += 'i love you'
#     fun3(var)
#     return var

# def fun3(var):
#     var = 'xiaojiy'
    
# print(fun1())
# print('-'*50)

# def fun(var):
#     var = 1314
#     print(var)

# var = 520
# fun(var)

# print(var)



# def Hui(string):
#     list1 = list(string)
#     list2 = reversed(list1)
#     if list1 == list(list2):
#         return 'HuiWen'
#     else:
#         return 'NotHuiWen'
    
# print(Hui('上海自来水来自海上'))



# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.arange(1,7).reshape(3,2),
#    index = pd.date_range('1/1/2019', periods=3),
#    columns = ['A', 'B'])

# print(df)

# print('-'*10)

# print (df.expanding(min_periods=2).mean())



# import pandas as pd
# import numpy as np

# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#          'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#          'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#          'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#          'Points':[876,789,863,673,741,812,756,788,694,701,804,690]
#          }
# df = pd.DataFrame(ipl_data)

# print (df)

# print (df.groupby('Year'))
# print('-'*10)

# print (df.groupby('Year').groups)
# print('-'*10)

# print (df.groupby(['Year','Team']).groups)
# print('-'*10)

# grouped = df.groupby('Year')

# for name,group in grouped:
#     print (name)
#     print (group)
# print('-'*10)

# print (grouped.get_group(2014))
# print('-'*10)

# agg = grouped['Points'].agg([np.sum, np.mean, np.std])
# print (agg)
# print('-'*20)

# filter = df.groupby('Team').filter(lambda x: len(x) >= 3)
# print (filter)
# print('-'*50)



# def Fun1():
#     x = 5
#     def Fun2():
#         nonlocal x
#         x *= 5
#         return x
#     return Fun2

# a = Fun1()

# print(a)
# print(a)
# print(a)

# print('-'*50)

# print(a())
# print(a())
# print(a())



# def funout():
#     def funin():
#         print('bingo!')
#     return funin

# funout()()   



# import pandas as pd
# import numpy as np

# df = pd.read_csv("temp.csv")

# print("type of df",type(df))
# value=df.values
# print("type of value:",type(value))
# print("shape of value:",value.shape)
# print(df)
# print('-'*50)

# df2 = pd.read_csv("temp.csv")
# print(df2.ix[:,1:3])



# def power(x,y):
#     if y == 1:
#         return x
#     else:
#         return x * power(x,y-1)

# power(3,2)



# #求最大公约数的递归函数 
# def gcd1(x,y):
#     if x % y == 0:
#         return y
#     else:
#         return gcd(y,x%y)



# #十进制转二进制的递归函数
# def bin2(x):
#     m = ''

#     if x//2 <2:
#         return m + str(x % 2) 
#     else:
#         return m + str(bin(x // 2))



# def get_digits(n):
#     l = []
#     if n < 10:
#         return [n]
#     else:
#         return [n%10]+get_digits(n//10)



# def sui(n):
#     if n == 1:
#         return 10
#     else:
#         return sui(n-1)+2
# sui(5)



# import pandas as pd
# import numpy as np


# df = pd.DataFrame(np.arange(15).reshape(5,3),index = [0,2,4,1,3],columns=['col2','col1','col3'])

# print(df)
# print('-'*50)
    
# sorted_df=df.sort_values(by='col1',ascending=False)
# print(sorted_df)



# print('
#       |- 欢迎进入通讯录程序 -|
#       |- 1：查询联系人资料 -|
#       |- 2：插入新的联系人 -|
#       |- 3：删除已有联系人 -|
#       |- 4：退出通讯录程序 -|
#       ')

# txl = {}

# def one():
#     name = input('请输入联系人姓名：')
#     if name in txl:
#         print(name,':',txl.get(name))
#         give_code()
#     else:
#         print('查无此人')
#         give_code()

# def two():
#     name = input('请输入联系人姓名：')
#     if name in txl:
#         print('输入的姓名在通讯录中已存在 ->>  ',name,':',txl.get(name)) 
#         change = input('是否修改用户资料（YES/NO）：')
#         if change == 'YES':
#             number = input('请输入用户联系电话：')
#             txl[name] = number
#             print('修改成功！')
#             give_code()
#         else:
#             give_code()         
#     else:
#         number = input('请输入用户联系电话：')
#         txl[name] = number
#         print('插入成功！') 
#         give_code()
        
# def three():
#     name = input('请输入联系人姓名：')
#     if name in txl:
#         print('确认删除这条记录吗？ ->>  ',name,':',txl.get(name)) 
#         change = input('确认（YES/NO）：')
#         if change == 'YES':
#             del txl[name]
#             print('删除成功！')
#             give_code()
#         else:
#             print('取消删除！')
#             give_code()
#     else:
#         print('查无此人') 
#         give_code()

# def four():
#     print('|- 感谢使用通讯录程序 -|')


# def give_code():  
#     code = input('请输入相关的指令代码：')
#     if code == '1':
#         one()
#     elif code == '2':
#         two()
#     elif code == '3':
#         three()
#     elif code == '4':
#         four()
#     else:
#         print('指令输入错误!!!')


# give_code()



# import pandas as pd
# import numpy as np

# s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t', 'Alber@t'])

# print(s)
# print('-'*50)

# print (s.str.cat(sep=' <=> '))
# print('-'*50)

# print (s.str.get_dummies())
# print('-'*50)

# print (s.str.contains(' '))
# print('-'*50)

# print (s.str.replace('@','$'))
# print('-'*50)

# print (s.str.repeat(2))
# print('-'*50)

# print (s.str.count('m'))
# print('-'*50)

# print (s.str.findall('i'))
# print('-'*50)

# print (s.str.swapcase())
# print('-'*50)



# import numpy as np
# import pandas as pd

# data = {'Name':['Tom','James','Ricky'],
#         'Age':[25,26,25],
#         'Rating':[4.23,3.24,3.98]
#         }

# df = pd.DataFrame(data)

# print(df)
# print('-'*50)

# print (df['Age'].pct_change())      #想应用到行上，那么可使用axis = 1参数
# print('-'*50)

# print (df['Age'].corr(df['Rating']))
# print('-'*50)

# print (df.corr())
# print('-'*50)

# print (df['Age'].rank(method = 'min'))
# print('-'*50)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.arange(15).reshape(5,3),index = ['a','b','c','d','e'],columns = ['col1','col2','col3'])

# print(df)
# print('-'*50)

# #print (df.rolling(window=3,min_periods=2).mean())
# print('-'*50)

# #print (df.rolling(window=3).mean())
# print('-'*50)

# #print (df.expanding(min_periods=3).mean())
# print('-'*50)

# #print (df['col1'].mean())
# print('-'*50)

# #print (df.ewm(com=1).mean())
# #print('-'*50)

# #print (df.ewm(com=10).mean())
# #print('-'*50)

# r = df.rolling(window=3,min_periods=1)

# print (r[['col1','col2']].aggregate([np.sum,np.mean]))
# print('-'*50)

# print (r.aggregate({'col1' : np.sum,'col2' : np.mean}))
# print('-'*50)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.arange(6).reshape(2,3),index = ['a','b'],columns = ['col1','col2','col3'])

# df = df.reindex(['a','new','b'])

# print(df)
# print('-'*50)

# print(df.isnull())
# print('-'*50)

# #print (df.notnull())
# #print('-'*50)

# print (df.fillna(0))
# print('-'*50)

# print (df.fillna(method='pad'))
# print('-'*50)

# print (df.fillna(method='backfill'))
# print('-'*50)

# print (df.dropna())
# print('-'*50)

# print (df.replace({3:333,5:555}))
# print('-'*50)



# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils',],
#          'Rank': [1, 2, 2,],
#          'Year': [2014,2015,2014],
#          'Points':[876,789,863]})

# print(df)
# print('-'*50)

# print (df.groupby('Team'))
# print('-'*50)

# print (df.groupby(['Team','Year']).groups)
# print('-'*50)

# for name,group in df.groupby(['Team','Year']):
#     print(name)
#     print(group)
# print('-'*50)

# print (df.groupby('Team').get_group('Riders'))
# print('-'*50)

# print (df.groupby('Team')['Points'].agg([np.mean,np.sum,np.size]))
# print('-'*50)
# #
# print (df.groupby('Team').agg(np.size))
# print('-'*50)

# grouped = df.groupby('Team')
# score = lambda x: (x - x.mean()) / x.std()*10
# print (grouped.transform(score))
# print('-'*50)

# filter = df.groupby('Team').filter(lambda x:  len(x) >= 2)
# print (filter)



# str1 = input('>>>')

# list1 = str1.split('\n')

# print('-'*50)
# print(list1)
# print('-'*50)

# #for i in list1:
# #    print (i)
# #    print('-'*50)



# file_name = input('请输入文件名：')

# f = open(file_name + '.txt','w')
# list1 = []

# content = input('请输入内容【单独输入“:w”保存退出】：')
# new = content[:-2]  

# f.write(new)

# f.close()



# str1 = input('请输入2个文件名，用“,”分隔：')

# f1,f2 = str1.split(',')[0],str1.split(',')[1]

# c1 = open(f1+'.txt','r')
# c2 = open(f2+'.txt','r')
# xu = 0
# count = 0
# l = []

# len1 = len(c1.readlines())
# c1.seek(0,0)

# for i in range(len1):
#     xu += 1 
#     if c1.readline() == c2.readline():
#         continue
#     else:
#         count += 1
#         l.append(xu)
        
# print('两个文件共有【',count,'】处不同：')
# for i in l:
#     print('第',i,'行不一样')

   

# file_name = input('请输入要打开的文件：')
# #D:\\小鸡理财\\OneDrive\\python\\01.txt
# row = int(input('请输入要显示的文件行数：'))

# print('文件 ',file_name,' 的前',row,'行的内容如下：')

# f= open(file_name)

# for i in range(row):
#     print(f.readline())

# f.close()

  

# file_name = input('请输入要打开的文件：')
# #D:\\小鸡理财\\OneDrive\\python\\01.txt
# f= open(file_name)

# row = input('请输入要显示的文件行数：').split(':')

# def p1():
#     print('文件 ',file_name,' 的第',row[0],'行到第',row[1],'行的内容如下：')
#     gap = int(row[1])-int(row[0])
#     for i in range(int(row[0])-1):
#         f.readline()
#     for j in range(gap):
#         print(f.readline())
        
# def p2():
#     print('文件 ',file_name,' 开始到第',row[1],'行的内容如下：')
#     for i in range(int(row[1])):
#         print(f.readline())
   
# def p3():
#     print('文件 ',file_name,' 第',row[0],'行到结尾的内容如下：')
#     for i in range(int(row[0])-1):
#         f.readline()
#     for j in range(20):
#         print(f.readline())    


# if row[0] == '':
#     p2()
# elif row[1] == '':
#     p3()
# else:
#     p1()

 

# file_name = input('请输入要打开的文件：')
# #D:\\小鸡理财\\OneDrive\\python\\01.txt
# f= open(file_name)
# str_all = f.read()

# str_old = input('请输入要替换的单词或字符：')
# str_new = input('请输入新的单词或字符：')

# c = str_all.count(str_old)

# print('文件 ',file_name,' 中共有',c,'个【',str_old,'】\n'\
#       '确定要把所有的替换为',str_new,'吗？\n'\
#       )
# choose = input('[YES/NO]:')

# if choose == 'yes':
#     str_all_new = str_all.replace(str_old,str_new)
#     print(str_all_new)    

 

# import pandas as pd

# left = pd.DataFrame({
#          'id':[1,2,3,4,5],
#          'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#          'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame(
#          {'id':[1,2,3,4,5],
#          'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#          'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print (left)
# print("========================================")
# print (right)
# print('-'*50)

# #rs = pd.merge(left,right,on='id')
# #print(rs)
# print('-'*50)

# #rs = pd.merge(left,right,on=['id','subject_id'])
# #print(rs)
# print('-'*50)

# #rs = pd.merge(left, right, on='subject_id', how='left')         #same as how = 'right'
# #print (rs)
# print('-'*50)

# rs = pd.merge(left, right, how='outer', on='subject_id')
# print (rs)
# print('-'*50)

# rs = pd.merge(left, right, on='subject_id', how='inner')
# print (rs)

 

# import pandas as pd
# import numpy as np

# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[0,1,2])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['e','b','c','d'],index=[1,2,3])
# #df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

# print (df1)
# print("========================================")
# print (df2)
# print("========================================")
# #print (df3)
# #print('-'*50)

# #rs = pd.concat([df1,df2])
# #print(rs)
# print('-'*50)


# #rs = pd.concat([df1,df2],ignore_index=True,join='inner')
# #print(rs)
# print('-'*50)

# #rs = pd.concat([df1,df2],axis=1)
# #print(rs)
# print('-'*50)

# #rs = pd.concat([df1,df2],axis=1,join_axes = [df1.index])
# #print(rs)
# print('-'*50)

# rs = df1.append([df2,df1],ignore_index=True)
# print(rs)
# print('-'*50)

# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
# rs = df1.append(s1,ignore_index=True)
# print(rs)
# print('-'*50)

# rs = pd.merge()

 

# import os

# dir_num = 0
# zi = {}

# for root, dirs, files in os.walk(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据'):
# #    print(root)
# #    print(dirs)
# #    print(files)
# #    print('-'*50)
#     dir_num += len(dirs)
#     for i in files:
#         k = os.path.splitext(i)[1]
#         if k in zi:
#             zi[k] += 1
#         else:
#             zi[k] = 1

# for key,value in zi.items():
#     print('该文件夹下共有类型为【%s】的文件 %s 个' % (key,value))
# print('该文件夹下共有类型为【文件夹】的文件 %s 个' % (dir_num))

 

# import os

# for root,dirs,files in os.walk(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据'):
#     os.chdir(root)
    
#     for i in files:
#         size = os.path.getsize(i)
#         print('%s [ %s Bytes]' %(i,size))

 

# import os

# file_add = input('请输入待查找的初始目录：')
# video = ['.mp4','.rmve','.avi']
# video_list = []

# for root,dirs,files in os.walk(file_add):
#     for i in files:
#         k = os.path.splitext(i)[1]
#         if k in video:
#             add = root + '\\' + i
#             video_list.append(add)

# #print(video_list)

# f = open('video_list.txt','w')
# for j in video_list:
#     f.write(j)
#     f.write('\n')
# #f.writelines(video_list)
# f.close()

# #D:\VDownload

 

# import os

# all_files = os.listdir(os.curdir)
# type_dict = dict()

# print(all_files)

 

# def futou(n):
#     if n == 1:
#         return 14000*1.2
#     else:
#         return futou(n-1)*1.2


# a = int(input('enter years: '))

# money = 0
 
# for i in range(a):
#     money += futou(i+1)

# print(money)

 

# import pandas as pd
# import numpy as np

# df = pd.read_csv('01.csv')

# print(df)
# print('-'*50)

# df1=pd.read_csv("01.csv",index_col=['S.No'])
# print (df1)
# print(df1.dtypes)
# print('-'*50)

# df2=pd.read_csv("01.csv",index_col=['S.No'],dtype = {'Salary':np.float64})
# print (df2)
# print(df2.dtypes)
# print('-'*50)

# df3=pd.read_csv("01.csv",names=['a','b','c','d','e'],header=0)
# print (df3)
# print('-'*50)

# df4=pd.read_csv("01.csv", skiprows=2)
# print (df4)

 

# try:
#     for i in range(3):
#         for j in range(3):
#             if i == 2:
#                 raise KeyboardInterrupt
#             print(i,j)
# except KeyboardInterrupt:
#     print('out!')
#     print('6')

 

# import pandas as pd
# import numpy as np

# #df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'))
# #print(df)

# #df.plot()

# #df.plot.bar()

# #df.plot.bar(stacked=True)


# #df.plot.barh()

# #df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

# #df.plot.hist(bins=50)
# #df.hist(bins=20)
# #df.plot.box()
# #df.plot.area()
# #df.plot.scatter(x='a', y='b')

# df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
# df.plot.pie(subplots=True)
# df.plot.pie()

 
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# *- coding: utf-8 -*-

# import pandas as pd

# with pd.ExcelFile('01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'Sheet1')
#     df2 = pd.read_excel(xlsx,'Sheet2')
    
# print(df1.info())

# df3 = pd.merge(df1,df2,how = 'left',on = '身份证')
# df3.to_excel('用户画像数据_合并2.xlsx')

    

# #df1 = pd.read_csv(r'D:\小鸡理财\OneDrive\01.csv',sep = '\\n',engine='python',encoding = 'utf-8')
# #df2 = pd.read_csv(r'D:\小鸡理财\OneDrive\02.csv',sep = '\\n',engine='python',encoding = 'utf-8')

# #df1.rename(columns={'身份证' : 'c1'},inplace = True)
# #df2.rename(columns={'身份证' : 'c1'},inplace = True)            

# #print(len(df1))

# #df1['a'] = pd.Series(np.arange(len(df1)))
# #df2['b'] = pd.Series(np.arange(len(df2)))

# #df3 = pd.merge(df1,df2,how = 'left',on = '身份证')
# #print(df3)
# #df3.to_excel('000.xlsx')

 

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'total_bill':np.random.randint(10,size = 5),
#                     'sex':np.random.choice(np.array(['male','female']),5),
#                     'id':pd.Series(np.arange(5))
#                     })
                    

# print(df)
# print('='*50)

# #print(df.info())

# print(df.tips[['id','sex']])

 

# import matplotlib.pyplot as plt
# import numpy as np

# np.random.seed(19680801)
# data = np.random.randn(2, 100)
# #print(data.shape)
# #print('='*50)

# fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# #print(fig)
# #print('='*50)
# #print(axs)
# #print('='*50)


# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])

# plt.show()1投资标的

 

# import pandas as pd

# with pd.ExcelFile('01.xlsx') as xlsx:
# #    df1 = pd.read_excel(xlsx,'经典注册用户')
# #    df2 = pd.read_excel(xlsx,'经典投资记录')
#     df3 = pd.read_excel(xlsx,'存管注册用户')
#     df4 = pd.read_excel(xlsx,'存管投资记录')
    
# #print(df1.info())
# print('-read_ok-')


# #df5 = pd.merge(df1,df2,how = 'left',left_on = '用户名',right_on = '投资用户')
# df5 = pd.merge(df3,df4,how = 'left',left_on = '手机号码',right_on = '手机号')
# #df7 = pd.merge(df6,df4,how = 'left',left_on = '用户名',right_on = '投资用户')
# print('-merge_ok-')

# with pd.ExcelWriter('001.xlsx') as writer:
#     df5.to_excel(writer,sheet_name = 'jingdian',index = False)
# #    df7.to_excel(writer,sheet_name = 'cunguan',index = False)
    
# #df7.to_excel('001.xlsx')
# print('-write_ok-')

 

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [3, 6, 9], '-r')

# plt.plot([1, 2, 3], [2, 4, 9], ':g') 

# plt.show()

 

# a = dict(a=1,b=2,c=3)

# try:
#     print(a['a'])
# except KeyError as reason:
#     print(': %s' %reason)
# else:
#     print('else')
# finally:
#     print('end')

 

# class Person():
#     def __init__(self,name):
#         self.name = name
        
#         print(self.name)

# a = Person('xiaojiayu')

 

# class Rectangle():
#     def __init__(self):
#         self.length = 5
#         self.width = 4
        
#     def getRect(self):
#         print('这个矩形的长是： %s ，宽是： %s ' %(self.length,self.width))
        
#     def setRect(self):
#         print('请输入矩形的长和宽...')
#         self.length = float(input('长： '))
#         self.width = float(input('宽： '))        
        
#     def getArea(self):
#         area = self.length * self.width
#         print('面积是：',area)


# rect = Rectangle()
# rect.getRect()

# rect.setRect()

# rect.getRect()

# rect.getArea()

 

# import os
# os.chdir('D:\VDownload\新建文件夹\我的解析任务1804241345\合并')

# for root,dirs,files in os.walk('D:\VDownload\新建文件夹\我的解析任务1804241345\合并'):
#     for i in files:
#         l = i.split(' ',1)[1].strip()
#         print(l)

#         os.rename(i,l)

 

# class ticket:
#     def __init__(self,adult,child,day_type):
#         self.adult = int(adult)
#         self.child = int(child)
#         self.day = day_type
        
#     def money(self):
#         x = 'non_week'
#         money = self.adult * 100 + self.child * 50
#         if self.day == x:
#             return money
#         else:
#             return money * 1.2
        
# adult = input('adult:')
# child = input('child:')        
# day_type = input('day_type:')

# a = ticket(adult,child,day_type)

# print(a.money())

 

# import random as r

# legal_x = [0,100]
# legal_y = [0,100]

# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
        
#         #初始位置        
#         self.x = r.randint(legal_x[0],legal_x[1])
#         self.y = r.randint(legal_y[0],legal_y[1])
        
#     def move(self):
#         #随机计算方向并移动到新的位置(x,y)
#         new_x = self.x + r.choice([1,-1,2,-2])
#         new_y = self.y + r.choice([1,-1,2,-2])
        
#         #检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x    

#         #检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
            
#         #体力消耗
#         self.power -= 1
        
#         #返回移动后的新位置
#         return (self.x,self.y)
    
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
            
# class Fish:
#     def __init__(self):
#         #初始位置      
#         self.x = r.randint(legal_x[0],legal_x[1])
#         self.y = r.randint(legal_y[0],legal_y[1])    

#     def move(self):
#         #随机计算方向并移动到新的位置(x,y)
#         new_x = self.x + r.choice([1,-1])
#         new_y = self.y + r.choice([1,-1])
        
#         #检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x    

#         #检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y

#         #返回移动后的新位置
#         return (self.x,self.y)

# turtle = Turtle()
# fish = []
# count = 1

# for i in range(100):
#     new_fish = Fish()
#     fish.append(new_fish)
    
# while True:
#     if not len(fish):
#         print('鱼儿都吃完了，游戏结束')
#         break
#     if not turtle.power:
#         print('乌龟体力耗尽，挂掉了！')
#         break
        
#     pos = turtle.move()
    
#     #在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     #这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    
#     for each_fish in fish[:]:
        
#         if each_fish.move() == pos:
#             #鱼儿被吃掉了
#             turtle.eat()
            
#             fish.remove(each_fish)
#             print('第 %s 条鱼儿被吃掉了...' %count)
#             count += 1

 

# import random as r

# legal_x = [0,10]
# legal_y = [0,10]

# class Turtle_or_Fish:
#     def __init__(self,turtle = False,fish = False):
#         # 初始体力
#         self.power = 100
#         self.turtle = turtle
#         self.fish = fish
        
#         #初始位置        
#         self.x = r.randint(legal_x[0],legal_x[1])
#         self.y = r.randint(legal_y[0],legal_y[1])
        
#     def move(self):
#         if self.turtle:
#             #随机计算方向并移动到新的位置(x,y)
#             new_x = self.x + r.choice([1,-1,2,-2])
#             new_y = self.y + r.choice([1,-1,2,-2])
#         else:
#             #随机计算方向并移动到新的位置(x,y)
#             new_x = self.x + r.choice([1,-1])
#             new_y = self.y + r.choice([1,-1])            
                
#         #检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x    

#         #检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
            
#         #体力消耗
#         self.power -= 1
        
#         #返回移动后的新位置
#         return (self.x,self.y)
    
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
            

# turtle = Turtle_or_Fish(turtle = True)
# fish = []
# count = 1

# for i in range(10):
#     new_fish = Turtle_or_Fish(fish = True)
#     fish.append(new_fish)
    
# while True:
# #    print(len(fish))
#     if not len(fish):
#         print('鱼儿都吃完了，游戏结束')
#         break
#     if not turtle.power:
#         print('乌龟体力耗尽，挂掉了！')
#         break
        
#     pos = turtle.move()
    
#     #在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     #这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    
#     for each_fish in fish[:]:
        
#         if each_fish.move() == pos:
#             #鱼儿被吃掉了
#             turtle.eat()
            
#             fish.remove(each_fish)
#             print('第 %s 条鱼儿被吃掉了...' %count)
#             count += 1

 

# a = 0
# a = 1
# class f:
# #    global a
#     a = 2
#     def f1(self):
#         print(a+5)
        
# ff = f()
# ff.f1()


# b = 0

# class l:
#     def __init__(self,b):
#         self.b = b
    
#     def l1(self):
#         print(self.b + 5)
        
# ll = l(10)
# ll.l1()



# import matplotlib.pyplot as plt
# import numpy as np

# labels1 = ['Man', 'Women']

# data1 = [18278,16852]

# plt.pie(data1, labels=labels1, autopct='%1.1f%%')
# plt.axis('equal')
# plt.legend()

# plt.show()



# import pandas as pd
# import numpy as np


# # 数据集路径
# df = pd.read_csv('survey.csv')

# # 去掉可能存在的空格
# df['Gender'] = df['Gender'].str.replace(' ','')
# # 转换为小写
# df['Gender'] = df['Gender'].str.lower()
# #数据清洗
# df['Gender'] = df['Gender'].replace({'m':'male','f':'female'})
# #数据值合并
# df = df[(df['Gender'] == 'male') | (df['Gender'] == 'female')]

# table = pd.pivot_table(df, values=['Age'], index=['Country'],columns=['Gender'], aggfunc=np.size)

# table.to_excel('666.xlsx')



# import pandas as pd
# import numpy as np

# df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','MN','ON'],
#                         'City' : ['Toronto','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
#                         'Sales' : [13,6,16,8,4,3,1]})
    
# print(df)
# print('='*50)

# table = pd.pivot_table(df,values=['City'],index=['Province'],columns=['City'],aggfunc=np.size)

# print(table)
# print('='*50)

# print(table.stack('City'))



# import math

# class Point():
#     def __init__(self,x = 0,y = 0):
#         self.x = x
#         self.y = y
        
#     def getX(self):
#         return self.x
    
#     def getY(self):
#         return self.y

# class Line(Point):
#     def __init__(self,p1,p2):
#         self.x = p1.getX() - p2.getX()
#         self.y = p1.getY() - p2.getY()
#         self.len = math.sqrt(self.x * self.x + self.y * self.y)
        
#     def getLen(self):
#         return self.len
    
# p1 = Point(3,4)
# p2 = Point(5,6)

# line = Line(p1,p2)
# print(line.getLen())        

  

# import pandas as pd
# import numpy as np

# df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','$','ON'],
#                         'City' : ['?','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
#                         'Sales' : [13,6,16,8,np.NaN,3,1]})

# print(df)
# print('='*50)

# df1 = df.replace({'$':1,'?':1})
# print(df1)
# print('='*50)

# df2 = df.replace({0:'?'},np.nan)
# print(df2)
# print('='*50)

  

# import numpy as np
# import matplotlib.pyplot as plt

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)

# # the histogram of the data
# n, bins, patches = plt.hist(x, 100, normed=1, facecolor='g', alpha=0.8)


# plt.xlabel('Smarts',fontsize=14, color='red')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(20, .02, r'$\mu=100,\ \sigma=15,\bigcap $')
# plt.axis([0, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

 

# import matplotlib.pyplot as plt
# import numpy as np

# #需要展现的数据
# data = np.arange(100, 201)

# #设定x，y轴的最大、最小值
# #plt.axis([0,100,50,300])

# #另一种设定x，y轴的最大、最小值的方式
# plt.xlim(0,100)
# plt.ylim(50,300)

# #
# plt.xticks(np.linspace(0,100,5,endpoint=True))
# plt.yticks(np.linspace(50,300,5,endpoint=True))

# plt.title('Easy as 1, 2, 3')      #补充，设定标题

# #设定x，y轴标签,标签字体，颜色
# plt.xlabel('x numbers',fontsize=14, color='red')      
# plt.ylabel('y numbers',fontsize=14, color='red')

# #在图表内增加公式
# plt.text(20, 250, r'$\mu=100,\ \sigma=15,\bigcap $')

# #设置背景网格线
# plt.grid(True)

# plt.plot(data,color="blue", linewidth=1.0, linestyle="-")

# plt.show()

 

# # 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
# from pylab import *

# # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# figure(figsize=(8,6), dpi=80)

# # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
# subplot(1,1,1)

# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)

# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# plot(X, S, color="green", linewidth=1.0, linestyle="-")

# # 设置横轴的上下限
# xlim(-4.0,4.0)

# # 设置横轴记号
# xticks(np.linspace(-4,5,9,endpoint=True))

# # 设置纵轴的上下限
# ylim(-1.0,1.0)

# # 设置纵轴记号
# yticks(np.linspace(-1,1,5,endpoint=True))

# # 以分辨率 72 来保存图片
# # savefig("exercice_2.png",dpi=72)

# # 在屏幕上显示
# show()

 

# # 载入绘图模块
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # 加载数据
# iris_data = sns.load_dataset('iris')

# # 散点图
# #sns.lmplot(x='petal_length', y='petal_width', hue='species', data=iris_data)

# #查看两个维度数据之间的关系
# #sns.PairGrid(data=iris_data).map(plt.scatter)
# #区分种类
# #sns.PairGrid(data=iris_data, hue='species').map(plt.scatter)

# #查看两个维度数据之间的关系
# #sns.JointGrid(data=iris_data, x='sepal_length', y='sepal_width').plot(sns.regplot, sns.distplot)

# #绘制单变量的核密度估计图
# #sns.kdeplot(data=iris_data["sepal_length"])
# #sns.kdeplot(data=iris_data["sepal_length"], shade=True, color='y')

# #绘制二元变量的核密度估计图
# #sns.kdeplot(data=iris_data["sepal_length"], data2=iris_data["sepal_width"], shade=True)

# #绘制热力图
# #matrix_data = np.random.rand(10, 10)
# #sns.heatmap(data=matrix_data)

# #层次聚类热图
# iris_data.pop("species")  #去掉了花的类别列
# sns.clustermap(iris_data)

# plt.show()

 

# import pandas as pd

# data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack'],
#         'Age':[25,26,25,23,30,29,23],
#         'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]
#         }

# df = pd.DataFrame(data)

# print(df)
# print('='*50)

# print(df['Age'].value_counts())
# print('='*50)
    
# print(df.count())
# print('='*50)

# print(df.dtypes)
# print('='*50)


# df['Age'] = df['Age'].astype('float64')
# print(df.dtypes)
# print('='*50)

# print(df.index)
# print(df.columns)
# print('='*50)

# x = df.loc[df['Name'].isin(['James','Tom']),['Name','Age']]
# print(x)

 

# import pandas as pd
# import numpy as np

# with pd.ExcelFile('01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
#     df3 = pd.read_excel(xlsx,'投资')
    
# print('-read_ok-')

# df2['add'] = 1

# #print(df2)
# #print(df2.columns)
# #print(df3.columns)

# df4 = pd.merge(df2,df3,how = 'left',on = '下线手机号')
# df5 = pd.merge(df1,df4,how = 'left',left_on = '上线手机号',right_on = '上线邀请人')
# df6 = df5[(df5['下线邀请渠道'] != '业务邀请')]

# #print('select ok')
# #print(df6)

# #print(df5.head(20))
# #print(df5.shape)
# #print(df4['下线邀请渠道'].drop_duplicates())

# gp = df6.groupby(['上线手机号','上线真实姓名'])
# result = gp.agg({'add':np.sum,'标记':np.sum}).sort_values(by = ['add','标记'],ascending=False)
# #print(result)

# print('-merge_ok-')

# with pd.ExcelWriter('001.xlsx') as writer:
#     result.to_excel(writer,sheet_name = 'result')

    
# print('-write_ok-')

 

# import numpy as np
# import pandas as pd


# rng = pd.date_range('1/1/2018', periods=5, freq='M')
# print()
# print(rng)

# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print('\nts')
# print (ts)

# ps = ts.to_period()
# print('\nps')
# print(ps)

# print('\nps')
# print(ps.to_timestamp())
# print('='*100)


# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(data, index=labels)

# print(df)
# print()

# print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])
# print()

# print(df[df['animal'].isin(['cat', 'dog'])])
# print()

# print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
# print()

# df2 = df['priority'].map({'yes': True, 'no': False})
# print(df2)
# print()
# print('='*100)


# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
#                                'Budapest_PaRis', 'Brussels_londOn'],
#               'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
#               'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
#                    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
#                                '12. Air France', '"Swiss Air"']})
# print(df)
# print()

# #数据列拆分
# temp = df.From_To.str.split('_', expand=True)
# temp.columns = ['From', 'To']
# print(temp)
# print()

# #删除坏数据加入整理好的数据
# df = df.drop('From_To', axis=1)
# df = df.join(temp)
# print(df)
# print()

# #去除多余字符
# df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
# print(df)
# print()

# #格式规范
# """
# 在 RecentDelays 中记录的方式为列表类型，由于其长度不一，这会为后期数据分析造成很大麻烦。这里将 RecentDelays 的列表拆开，取出列表中的相同位置元素作为一列，若为空值即用 NaN 代替
# """
# delays = df['RecentDelays'].apply(pd.Series)
# print('delays:')
# print(delays)
# delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
# print('delays:')
# print(delays)
# df = df.drop('RecentDelays', axis=1).join(delays)
# print('df:')
# print(df)
# print()

 

# df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','$','ON'],
#                         'City' : ['?','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
#                         'Sales' : [13,6,16,8,np.NaN,3,1]})
# print(df.corr())


# print(df.index)

# df2 = df.set_index('City')
# print(df2)

# df3 = df2.reset_index()
# print(df3)

# s = pd.Series(np.range(7))
# print(s)
# print()

# df4 = pd.concat([df,s],axis = 1)
# print(df4)
# print()

# print('idxmax:',df4['Sales'].idxmax())

 

# data = {'Name':['Tom','James','Ricky'],
#         'Age':[25,26,25],
#         'Rating':[4.23,3.24,3.98]
#         }

# df = pd.DataFrame(data)


# print(df)
# print('_'*50)

# max_index = df[['Age','Rating']].idxmax()
# print(max_index)

# min_index = df[['Age','Rating']].idxmin()
# print(min_index)



 

# df = pd.read_csv('country_additives.csv',encoding = 'gbk',names = ['country','point'])

# print(df.info())
# #print('='*50)
 
# #print(df.dtypes)
# #print('='*50)
 
# df2 = df['country'].str.split(',',expand=True)
# #print(df2.head())
# #print('='*50)
 
# df3 = pd.concat([df,df2],axis = 1)
# #print(df3.head())
# #print('='*50)
# #print(df3.shape)
 
# df4 = df3[['point',0]]
 
# for i in range(1,14):
#     df_temp = df3[['point',i]]
#     df_temp = df_temp.rename(columns={i:0})
# #    print(i,':df_temp:',df_temp.columns)
#     df4 = df4.append(df_temp)
 
# #print(df4.info())

 

# df = pd.DataFrame({'date': pd.date_range('2015-01-01', freq='W',periods=5),'a': np.arange(5)},
#     index=pd.MultiIndex.from_arrays([[1,2,3,4,5],pd.date_range('2015-01-01', freq='W',periods=5)],names=['v','d']))


# date_sum = df.resample('M', on='date').sum()
# print(date_sum)
# print('='*50)

# index_date_sum = df.resample('M', level='d').sum()
# print(index_date_sum)
# print('='*50)

# print(df)

 

# with pd.ExcelFile('01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
#     df3 = pd.read_excel(xlsx,'投资')
    
# print('-read_ok-')

# df4 = pd.merge(df2,df3,how = 'left',on = '下线手机号')
# df5 = pd.merge(df1,df4,how = 'left',left_on = '上线手机号',right_on = '上线邀请人')
# df6 = df5[(df5['下线邀请渠道'] != '业务邀请')]

# gp = df6.groupby(['上线手机号','上线真实姓名'])
# result = gp.agg({'注册标记':np.sum,'投资标记':np.sum}).sort_values(by = ['注册标记','投资标记'],ascending=False)

# print('-merge_ok-')

# with pd.ExcelWriter('001.xlsx') as writer:
#     result.to_excel(writer,sheet_name = 'result')

    
# print('-write_ok-')

 

# sum_offset = pd.tseries.offsets.Week(2)

# print(pd.date_range('1/1/2018', periods=5, freq=sum_offset))
# #ts = pd.Series(np.arange(10), index=rng)
# #
# #print(ts.index)
# #print('-'*50)

# #print(ts[ts.index[2]])
# #print('-'*50)

# #print(ts[::2])
# #print('-'*50)

# #print(ts.index.is_unique)
# #print('-'*50)

# #print(ts['2018/01/13'])
# #print('-'*50)

# #print(ts['2018-2'])
# #print('-'*50)

# #print(ts.truncate(before='2018-3-1'))
# #print('-'*50)
# #
# #print(ts.truncate(after='2018-3-1'))
# #print('-'*50)

# #print(ts.shift(1))
# #print('-'*50)
# #
# #print(ts.shift(-1))
# #print('-'*50)

 

# df = pd.DataFrame(np.arange(5),
#                  index=pd.date_range('20170101', periods=5),
#                  columns=['S1'])

# print(df.head())
# print('-'*50)

# #print(df.resample('M', level=0).sum())
# #print('-'*50)

# print(df['S1'].diff(2))
# print('-'*50)
# #
# #print(df.groupby(lambda x: x.month).sum())
# #print('-'*50)
# #
# #print(df.groupby(lambda x: x.weekday).sum())
# #print('-'*50)

 

# with pd.ExcelFile('a1.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'原始数据')
#     df2 = pd.read_excel(xlsx,'业务员')
#     df3 = pd.read_excel(xlsx,'推广')
   
# print('-read_ok-')

# df2['mark_2'] = 1
# df3['mark_3'] = 1

# #print(df1.info())
# #print(df2.info())
# #print(df3.info())

# df4 = pd.merge(df1,df2,how = 'left',left_on = '邀请人',right_on = '业务员')
# df5 = pd.merge(df4,df3,how = 'left',left_on = '用户名',right_on = '推广渠道用户名')

# print('-merge_ok-')

# df5['mark_2'] = df5['mark_2'].fillna(df5['邀请渠道'])
# df5['mark_2'] = df5['mark_2'].replace(1,'业务邀请')

# df5['mark_3'] = df5['mark_3'].fillna(df5['mark_2'])
# df5['mark_3'] = df5['mark_3'].replace(1,'自主注册')

# print('-modify_ok-')

# reslut = df5.rename(columns={'mark_3' : 'new_邀请渠道'})

# print('-rename_ok-')

# with pd.ExcelWriter('a1.xlsx') as writer:
#     reslut.to_excel(writer,sheet_name = 'result')

    
# print('-write_ok-')

 

# a = np.zeros((5,5))
# #
# #print('a:',a)
# #print('='*10)
# ##
# ##b = np.matrix(np.arange(10).reshape((5,2)))
# ##print('b:',b)
# ##print('='*10)
# ##
# ##for i in range(5):
# ##    print('i:',i)
# ##    c = b[:,0].A
# ##    print('c:',c)
# ##    print('='*10)  
# ##    d = np.nonzero(b[:,0].A == i)[0]
# ##    print('d:',d)
# ##    print('='*10)            
# ##    p = a[np.nonzero(b[:,0].A == i)[0]]
# ##    print(p)
# ##    print('='*10)
# #
# ##e = np.arange(4,step = 2)
# ##print(a[e])
# #
# #for i in range(5):
# #    a[:,i] = np.random.randint(10)
# #    
# #print('a:',a)
# #print('='*10)
# #
# #
# #f = np.array([[30,40,70],[80,20,10],[50,90,60]]) 
# #print('f:',f)
# #print(np.mean(f,axis = 0))


# #df = pd.DataFrame(np.arange(12).reshape(3,4),
# #                 index=pd.date_range('20170101', periods=3)
# #                 )
# #
# #print(df)
# #print(type(df))
# #
# #fo1 = pd.DataFrame.as_matrix(df)
# #
# #print(fo1)
# #print(type(fo1))
# #
# #fo2 = df.as_matrix()
# #
# #print(fo2)
# #print(type(fo2))
# #
# #fo3 = df.values
# #
# #print(fo3)
# #print(type(fo3))



# #dir_add = r'D:\小鸡理财\百度云同步盘\小鸡理财\数据报告\VIP报告\vip'
# #
# #num = 0
# #for root,dirs,files in os.walk(dir_add):
# #    x = os.path.split(root)
# #    print(x[1])
# #    print(type(x[1]))



# #VIP数据
# with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
# #    df3 = pd.read_excel(xlsx,'投资')
   
# print('-read_ok-')

# print(df1.shape)

# df4 = pd.merge(df1,df2,how = 'left',left_on = '邀请人',right_on = '手机号码')
# #df5 = pd.merge(df4,df3,how = 'left',on = '用户名')

# print('-merge_ok-')

# print(df4.shape)

# if df1.shape[0] == df4.shape[0]:
#     result = df4[df4['mark'].notnull()]
    
#     print('begin to write!!!')
#     result.to_csv('001.csv')
#     print('-write_ok-') 



# with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
#     df3 = pd.read_excel(xlsx,'投资')

# print(df1.shape)   
# print('-read_ok-')

# df4 = pd.merge(df2,df3,how = 'left',left_on = '下线',right_on = '手机号码')
# #gp = df4.groupby(by = '上线').agg({'下线':np.size,'mark':np.sum})
# df5 = pd.merge(df4,df1,how = 'inner',left_on = '上线',right_on = '手机号')
# #df1 = df1.set_index('手机号')


# #df1['下线注册数'] = gp['下线']
# #df1['下线投资人数'] = gp['mark']

# print('-merge_ok-')

# print(df1.shape)

# if True:   
#     print('begin to write!!!')
#     df5.to_csv('001.csv')
#     print('-write_ok-') 



# with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
#     df = pd.read_excel(xlsx,'名单')


# for i in range(1,df.shape[1]):
#     x = np.arange(5)
#     y = df.iloc[:,i]
# #    plt.ylim(0,100)
    
#     group_labels = ['2018.01', '2018.02', '2018.03', '2018.04', '2018.05']
    
#     plt.subplot(3, 2, i)
    
#     plt.plot(y,label = y.name)
    
#     plt.xticks(x, group_labels , rotation=0)
# #    plt.legend(loc='upper right')
#     plt.legend()
# #    plt.grid() 
    
   
# from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题    

    
# #plt.suptitle('当月新增下线人数', fontsize=26) 
# plt.show()



# with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
#     df1 = pd.read_excel(xlsx,'名单')
#     df2 = pd.read_excel(xlsx,'注册')
# #    df3 = pd.read_excel(xlsx,'投资')

# print(df1.shape)   
# print('-read_ok-')

# df4 = pd.merge(df1,df2,how = 'left',on = '用户名')
# #gp = df4.groupby(by = '上线').agg({'下线':np.size,'mark':np.sum})
# #df5 = pd.merge(df4,df1,how = 'inner',left_on = '上线',right_on = '手机号')
# #df1 = df1.set_index('手机号')


# #df1['下线注册数'] = gp['下线']
# #df1['下线投资人数'] = gp['mark']

# print('-merge_ok-')

# #print(df1.shape)

# if True:   
#     print('begin to write!!!')
#     df4.to_csv('001.csv')
#     print('-write_ok-') 



# import os

# dir_path = 'G:\wangwangduilidagong\汪汪队立大功 第四季'

# os.chdir(dir_path)

# for i in os.listdir('.'):
#     s = i.split(' ',3)[3]
#     os.rename(i,s)
#     print ("重命名成功。")



# #df = pd.DataFrame({'Sp':['a','b','c','d','e','f'], 
# #                   'Mt':['s1', 's1', 's2','s2','s2','s3'], 
# #                   'Value':[1,2,3,4,5,6], 
# #                   'Count':[3,2,5,10,10,6]})
# #    
# #print(df)
# #print('='*50)
# #
# ##df_max = df.sort_values(by = 'Count',ascending = False).drop_duplicates('Mt')
# #
# ##print(df_max)
# #
# ##print( df.groupby(['Mt'])['Count'].agg(max))
# # 
# ##idx=df.groupby(['Mt'])
# ##for i in idx:
# ##    print(i)
# ##idx1 =  idx == df['Count']
# ##print idx1
# ## 
# ##df[idx1] ['Count'].transform(max)
# #
# #
# #score = lambda x: (x - x.mean()) / x.std()*10
# #print(df.groupby('Mt').transform(score) )


# df = pd.DataFrame ({'a' : np.random.randn(6),
#              'b' : ['foo', 'bar'] * 3,
#              'c' : np.random.randn(6)})
 
# def my_test(a, b):
#     return a + b
 
# df['Value'] = df.apply(lambda row: my_test(row['a'], row['c']), axis=1)
# print( df)



# path = 'C:\\Users\\ye\\Downloads\\excel转csv\\'
# os.chdir(path)

# filenames = os.listdir(path)
# dd = []


# for i in filenames:
#     dd.append(pd.read_csv(i,engine = 'python')) 

# #另一种读取方法    
# #for i in filenames:
# #    f = open(i,'r')
# ##    res = pd.read_csv(f)
# #    dd.append(pd.read_csv(f)) 

# df = pd.concat(dd)

# print(df.shape)

# df.to_csv('002.csv',index = False)
# print('ok')



# df = pd.DataFrame({'id':[i for i in range(1,6)],
#                          'gender':np.random.choice(['f','m'],5),
#                          'age':np.random.randint(20,30,size = 5),
#                          'level':np.random.choice(['v1','v2','v3','v4'],5)
#                          })

# print(df)

# df_dum = pd.get_dummies(df,columns = ['gender','level'])

# print(df_dum)



# age = np.random.randint(12,80,size = 1000)

# #df = pd.DataFrame({'id':[i for i in range(len(age))],
# #                        'age':age
# #                        })
# #
# #print(df.describe())

# s = pd.Series(age)
# #print(s.describe())
# #print('='*50)

# age_cut = pd.cut(s,bins = [0,18,45,60,80],right = False,
#                  labels = ['未成年','青年','中年','老年'])

# print(age_cut.head())



# from lxml import objectify

# xml = objectify.parse('tt.xls')
# #print(xml)

# root = xml.getroot()

# print(root.Worksheet.Table.Row.Cell.Data)

# #print('getchildren:',root.Worksheet.Table.Row.getchildren())

# for i in root.Worksheet.Table.Row:
#     x = i.getchildren()
#     for j in x:
#         print(j.getchildren().text)



# os.chdir(r'D:\小鸡理财\OneDrive\python')
# df = pd.read_csv('02.csv',header = None,engine = 'python')

# print(len(df))

# l = [1,2,3,4,5,6,7,8]*428

# df['m'] = l

# #print(df.head(50))


# df.to_pickle('df.pkl')
# print('ok')



# import matplotlib.dates as mdates

# s = pd.Series(pd.date_range(start='20180723',periods = 100))
# x = np.random.randint(200,size=100)

# months = mdates.MonthLocator()
# days = mdates.DayLocator()

# timeFmt = mdates.DateFormatter('%Y-%m')

# fig,ax = plt.subplots()

# plt.plot(s,x)

# ax.xaxis.set_major_locator(months)
# ax.xaxis.set_major_formatter(timeFmt)
# ax.xaxis.set_major_locator(days)

# #plt.show()



# from sklearn import datasets
# import matplotlib.patches as mpatches

# iris = datasets.load_iris()

# print(iris)
# print('='*50)
# #
# #print(iris.target_names)
# #print('='*50)

# x = iris.data[:,2]
# y = iris.data[:,3]
# species = iris.target

# x_min,x_max = x.min()-0.5,x.max()+0.5
# y_min,y_max = y.min()-0.5,y.max()+0.5

# plt.figure()
# plt.title('iris datasets')
# plt.scatter(x,y,c=species)
# plt.xlabel('length')
# plt.ylabel('width')
# plt.xlim(x_min,x_max)
# plt.ylim(y_min,y_max)
# plt.xticks(())
# plt.legend()
# plt.yticks(())



# from sklearn.decomposition import PCA
# from sklearn import datasets
# from mpl_toolkits.mplot3d import Axes3D

# iris = datasets.load_iris()
# x = iris.data[:,1]
# y = iris.data[:,2]
# species = iris.target

# x_reduced = PCA(n_components=3).fit_transform(iris.data)

# #SCARRERPLOT 3D
# fig = plt.figure()
# ax = Axes3D(fig)

# ax.set_title('iris datasets')
# ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
# ax.set_xlabel('first')
# ax.set_ylabel('second')
# ax.set_zlabel('third')

# ax.w_xaxis.set_ticklabels(())
# ax.w_yaxis.set_ticklabels(())
# ax.w_zaxis.set_ticklabels(())

# from sklearn import datasets

# np.random.seed(0)
# iris = datasets.load_iris()
# x = iris.data
# y = iris.target
# i = np.random.permutation(len(iris.data))
# #print(i)

# x_train = x[i[:-10]]
# print(x_train)


# y_train = y[i[:-10]]
# #print(y_train)

# x_test = x[i[-10:]]
# y_test = y[i[-10:]]

# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier()
# knn.fit(x_train,y_train)
# print(knn.fit(x_train,y_train))
# print('='*50)

# print(knn.predict(x_test))
# print(y_test)

# ----------------------------------------------------------

# from sklearn.preprocessing import Imputer  # 导入sklearn.preprocessing中的Imputer库

# # 生成缺失数据
# df = pd.DataFrame(np.random.randn(6, 4), columns=['col1', 'col2', 'col3', 'col4'])  # 生成一份数据
# df.iloc[1:2, 1] = np.nan  # 增加缺失值
# df.iloc[4, 3] = np.nan  # 增加缺失值
# # print (df)

# # 查看哪些值缺失
# nan_all = df.isnull()  # 获得所有数据框中的N值
# # print (nan_all)  # 打印输出

# nan_col1 = df.isnull().any()  # 获得含有NA的列
# nan_col2 = df.isnull().all()  # 获得全部为NA的列
# print (nan_col1)  # 打印输出
# print (nan_col2)  # 打印输出

# ----------------------------------------------------------

# # 生成异常数据
# df = pd.DataFrame({'col1': [1, 120, 3, 5, 2, 12, 13],
#                    'col2': [12, 17, 31, 53, 22, 32, 43]})
# print (df,'\n')  # 打印输出

# # 通过Z-Score方法判断异常值
# df_zscore = df.copy()  # 复制一个用来存储Z-score得分的数据框
# cols = df.columns  # 获得数据框的列名
# for col in cols:  # 循环读取每列
#     df_col = df[col]  # 得到每列的值
#     z_score = (df_col - df_col.mean()) / df_col.std()  # 计算每列的Z-score得分
#     df_zscore[col] = z_score.abs() > 2.2  # 判断Z-score得分是否大于2.2，如果是则是True，否则为False
# print (df_zscore)  # 打印输出

# ----------------------------------------------------------

# from sklearn.preprocessing import OneHotEncoder  # 导入OneHotEncoder库

# # 生成数据
# df = pd.DataFrame({'id': [3566841, 6541227, 3512441],
#                    'sex': ['male', 'Female', 'Female'],
#                    'level': ['high', 'low', 'middle']})
# print (df,'\n')  # 打印输出原始数据框
# print(list(enumerate(df)))


# # 自定义转换主过程
# df_new = df.copy()  # 复制一份新的数据框用来存储转换结果
# for col_num, col_name in enumerate(df):  # 循环读出每个列的索引值和列名
#     col_data = df[col_name]  # 获得每列数据
#     col_dtype = col_data.dtype  # 获得每列dtype类型
#     if col_dtype == 'object':  # 如果dtype类型是object（非数值型），执行条件
#         df_new = df_new.drop(col_name, 1)  # 删除df数据框中要进行标志转换的列
#         value_sets = col_data.unique()  # 获取分类和顺序变量的唯一值域
#         for value_unique in value_sets:  # 读取分类和顺序变量中的每个值
#             col_name_new = col_name + '_' + value_unique  # 创建新的列名，使用原标题+值的方式命名
#             col_tmp = df.iloc[:, col_num]  # 获取原始数据列
#             new_col = (col_tmp == value_unique)  # 将原始数据列与每个值进行比较，相同为True，否则为False
#             df_new[col_name_new] = new_col  # 为最终结果集增加新列值
# print (df_new)  # 打印输出转换后的数据框

# res = pd.get_dummies(df,columns = ['sex','level'])
# print(res)

# ----------------------------------------------------------

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.decomposition import PCA

# # 读取数据文件
# data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter3\data1.txt')  # 读取文本数据文件
# x = data[:, :-1]  # 获得输入的x
# y = data[:, -1]  # 获得目标变量y
# print (x[0], y[0])  # 打印输出x和y的第一条记录

# # 使用sklearn的DecisionTreeClassifier判断变量重要性
# model_tree = DecisionTreeClassifier(random_state=0)  # 建立分类决策树模型对象
# model_tree.fit(x, y)  # 将数据集的维度和目标变量输入模型
# feature_importance = model_tree.feature_importances_  # 获得所有变量的重要性得分
# print (feature_importance)  # 打印输出

# # 使用sklearn的PCA进行维度转换
# model_pca = PCA()  # 建立PCA模型对象
# model_pca.fit(x)  # 将数据集输入模型
# model_pca.transform(x)  # 对数据集进行转换映射
# components = model_pca.components_  # 获得转换后的所有主成分
# components_var = model_pca.explained_variance_  # 获得各主成分的方差
# components_var_ratio = model_pca.explained_variance_ratio_  # 获得各主成分的方差占比
# print (components[:2])  # 打印输出前2个主成分
# print (components_var[:2])  # 打印输出前2个主成分的方差
# print (components_var_ratio)  # 打印输出所有主成分的方差占比

# ----------------------------------------------------------

# import random  # 导入标准库

# 简单随机抽样
# data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter3\data3.txt')  # 导入普通数据文件
# data_sample = random.sample(list(data), 2000)  # 随机抽取2000个样本
# print (data_sample[:2])  # 打印输出前2条数据
# print (len(data_sample))  # 打印输出抽样样本量

# # 等距抽样
# data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter3\data3.txt')  # 导入普通数据文件
# sample_count = 2000  # 指定抽样数量
# record_count = data.shape[0]  # 获取最大样本量
# width = record_count / sample_count  # 计算抽样间距
# data_sample = []  # 初始化空白列表，用来存放抽样结果数据
# i = 0  # 自增计数以得到对应索引值
# while len(data_sample) <= sample_count and i * width <= record_count - 1:  # 当样本量小于等于指定抽样数量并且矩阵索引在有效范围内时
#     data_sample.append(data[i * width])  # 新增样本
#     i += 1  # 自增长
# print (data_sample[:2])  # 打印输出前2条数据
# print (len(data_sample))  # 打印输出样本数量

# ----------------------------------------------------------

# 分层抽样
# import random  # 导入标准库
# # 导入有标签的数据文件
# data2 = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter3\data2.txt')  # 导入带有分层逻辑的数据
# each_sample_count = 200  # 定义每个分层的抽样数量
# label_data_unique = np.unique(data2[:, -1])  # 定义分层值域
# sample_list = []  # 定义空列表，用于存放临时分层数据
# sample_data = []  # 定义空列表，用于存放最终抽样数据
# sample_dict = {}  # 定义空字典，用来显示各分层样本数量
# for label_data in label_data_unique:  # 遍历每个分层标签
#     for data_tmp in data2:  # 读取每条数据
#         if data_tmp[-1] == label_data:  # 如果数据最后一列等于标签
#             sample_list.append(data_tmp)  # 将数据加入到分层数据中
#     each_sample_data = random.sample(sample_list, each_sample_count)  # 对每层数据都随机抽样
#     sample_data.extend(each_sample_data)  # 将抽样数据追加到总体样本集
#     sample_dict[label_data] = len(each_sample_data)  # 样本集统计结果
# print (sample_dict)  # 打印输出样本集统计结果

# ----------------------------------------------------------

# from sklearn import preprocessing

# data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter3\data6.txt', delimiter='\t')  # 读取数据

# # Z-Score标准化
# zscore_scaler = preprocessing.StandardScaler()  # 建立StandardScaler对象
# data_scale_1 = zscore_scaler.fit_transform(data)  # StandardScaler标准化处理

# # Max-Min标准化
# minmax_scaler = preprocessing.MinMaxScaler()  # 建立MinMaxScaler模型对象
# data_scale_2 = minmax_scaler.fit_transform(data)  # MinMaxScaler标准化处理

# # MaxAbsScaler标准化
# maxabsscaler_scaler = preprocessing.MaxAbsScaler()  # 建立MaxAbsScaler对象
# data_scale_3 = maxabsscaler_scaler.fit_transform(data)  # MaxAbsScaler标准化处理

# # RobustScaler标准化
# robustscalerr_scaler = preprocessing.RobustScaler()  # 建立RobustScaler标准化对象
# data_scale_4 = robustscalerr_scaler.fit_transform(data)  # RobustScaler标准化标准化处理

# # 展示多网格结果
# data_list = [data, data_scale_1, data_scale_2, data_scale_3, data_scale_4]  # 创建数据集列表
# scalar_list = [15, 10, 15, 10, 15, 10]  # 创建点尺寸列表
# color_list = ['black', 'green', 'blue', 'yellow', 'red']  # 创建颜色列表
# merker_list = ['o', ',', '+', 's', 'p']  # 创建样式列表
# title_list = ['source data', 'zscore_scaler', 'minmax_scaler', 'maxabsscaler_scaler', 'robustscalerr_scaler']  # 创建标题列表
# for i, data_single in enumerate(data_list):  # 循环得到索引和每个数值
#     plt.subplot(2, 3, i + 1)  # 确定子网格
#     plt.scatter(data_single[:, :-1], data_single[:, -1], s=scalar_list[i], marker=merker_list[i],
#                 c=color_list[i])  # 子网格展示散点图
#     plt.title(title_list[i])  # 设置子网格标题
# plt.suptitle("raw data and standardized data")  # 设置总标题
# plt.show()  # 展示图形

# ----------------------------------------------------------

# print('begin_to_work!')

# # - 修改工作目录
# file_add = r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据'
# file_name = '8月派券.xlsx'
# os.chdir(file_add)

# # - 导入待派券名单
# with pd.ExcelFile(os.path.abspath(file_name)) as xlsx:
#     df_jd_bj = pd.read_excel(xlsx,'经典本金')
#     df_jd_lx = pd.read_excel(xlsx,'经典利息')
#     df_cg = pd.read_excel(xlsx,'存管回款')
# # df_cg.info()


# print('import_ok!')

# # - 合并回款表
# df_hk = df_jd_bj.append([df_jd_lx,df_cg], ignore_index=True)
# # df_hk.info()

# # - 整理回款表
# df_hk['身份证'] = df_hk['身份证'].str.upper()
# df_hk['发放时间'] = pd.to_datetime(df_hk['预计本次发放时间'])
# del df_hk['预计本次发放时间']

# df_hk.to_excel('res.xlsx')
# print('output_ok!')

# ----------------------------------------------------------

# import numpy as np  # 导入numpy库
# import matplotlib.pyplot as plt  # 导入matplotlib库
# from sklearn.cluster import KMeans  # 导入sklearn聚类模块
# from sklearn import metrics  # 导入sklearn效果评估模块

# # 数据准备
# raw_data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter4\cluster.txt')  # 导入数据文件
# # print(raw_data[:3,:])

# X = raw_data[:, :-1]  # 分割要聚类的数据
# # print('\n',X.shape)

# y_true = raw_data[:, -1]
# # print('\n',y_true[:3])

# # 训练聚类模型
# n_clusters = 10  # 设置聚类数量
# model_kmeans = KMeans(n_clusters=n_clusters, random_state=0)  # 建立聚类模型对象
# model_kmeans.fit(X)  # 训练聚类模型
# y_pre = model_kmeans.predict(X)  # 预测聚类模型
# # print('y_pre:',y_pre)
# # print('type(y_pre):',type(y_pre))

# # 模型效果指标评估
# n_samples, n_features = X.shape  # 总样本量,总特征数
# # print('n_samples:',n_samples)
# # print('n_features:',n_features)

# inertias = model_kmeans.inertia_  # 样本距离最近的聚类中心的总和
# adjusted_rand_s = metrics.adjusted_rand_score(y_true, y_pre)  # 调整后的兰德指数
# mutual_info_s = metrics.mutual_info_score(y_true, y_pre)  # 互信息
# adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y_true, y_pre)  # 调整后的互信息
# homogeneity_s = metrics.homogeneity_score(y_true, y_pre)  # 同质化得分
# completeness_s = metrics.completeness_score(y_true, y_pre)  # 完整性得分
# v_measure_s = metrics.v_measure_score(y_true, y_pre)  # V-measure得分
# silhouette_s = metrics.silhouette_score(X, y_pre, metric='euclidean')  # 平均轮廓系数
# calinski_harabaz_s = metrics.calinski_harabaz_score(X, y_pre)  # Calinski和Harabaz得分

# print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
# print (70 * '-')  # 打印分隔线
# print ('ine\tARI\tMI\tAMI\thomo\tcomp\tv_m\tsilh\tc&h')  # 打印输出指标标题
# print ('%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%d' % (
# inertias, adjusted_rand_s, mutual_info_s, adjusted_mutual_info_s, homogeneity_s, completeness_s, v_measure_s,
# silhouette_s, calinski_harabaz_s))  # 打印输出指标值
# print (70 * '-')  # 打印分隔线
# print ('short name \t full name')  # 打印输出缩写和全名标题
# print ('ine \t inertias')
# print ('ARI \t adjusted_rand_s')
# print ('MI \t mutual_info_s')
# print ('AMI \t adjusted_mutual_info_s')
# print ('homo \t homogeneity_s')
# print ('comp \t completeness_s')
# print ('v_m \t v_measure_s')
# print ('silh \t silhouette_s')
# print ('c&h \t calinski_harabaz_s')

# # 模型效果可视化
# centers = model_kmeans.cluster_centers_  # 各类别中心
# # colors = ['#4EACC5', '#FF9C34', '#4E9A06']  # 设置不同类别的颜色
# plt.figure()  # 建立画布
# for i in range(n_clusters):  # 循环读类别
#     index_sets = np.where(y_pre == i)  # 找到相同类的索引集合
#     # print('index_sets:',index_sets)

#     cluster = X[index_sets]  # 将相同类的数据划分为一个聚类子集
#     plt.scatter(cluster[:, 0], cluster[:, 1], marker='.')  # 展示聚类子集内的样本点
#     plt.plot(centers[i][0], centers[i][1], 'o', markeredgecolor='k',
#              markersize=6)  # 展示各聚类子集的中心
# plt.show()  # 展示图像

# # 模型应用
# new_X = [1, 3.6]
# print('new_X:',new_X)
# print(np.array(new_X).reshape(1,-1).shape)
# cluster_label = model_kmeans.predict(np.array(new_X).reshape(1,-1))
# print ('cluster of new data point is: %d' % cluster_label)

# ----------------------------------------------------------

# 4.2 回归分析
# 导入库
# import numpy as np  # numpy库
# from sklearn.linear_model import BayesianRidge, LinearRegression, ElasticNet  # 批量导入要实现的回归算法
# from sklearn.svm import SVR  # SVM中的回归算法
# from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor  # 集成算法
# from sklearn.model_selection import cross_val_score  # 交叉检验
# from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score  # 批量导入指标算法
# import pandas as pd  # 导入pandas
# import matplotlib.pyplot as plt  # 导入图形展示库

# # 数据准备
# raw_data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter4\regression.txt')  # 读取数据文件
# X = raw_data[:, :-1]  # 分割自变量
# y = raw_data[:, -1]  # 分割因变量

# # 训练回归模型
# n_folds = 6  # 设置交叉检验的次数
# model_br = BayesianRidge()  # 建立贝叶斯岭回归模型对象
# model_lr = LinearRegression()  # 建立普通线性回归模型对象
# model_etc = ElasticNet()  # 建立弹性网络回归模型对象
# model_svr = SVR()  # 建立支持向量机回归模型对象
# model_gbr = GradientBoostingRegressor()  # 建立梯度增强回归模型对象
# model_names = ['BayesianRidge', 'LinearRegression', 'ElasticNet', 'SVR', 'GBR']  # 不同模型的名称列表
# model_dic = [model_br, model_lr, model_etc, model_svr, model_gbr]  # 不同回归模型对象的集合
# cv_score_list = []  # 交叉检验结果列表
# pre_y_list = []  # 各个回归模型预测的y值列表
# for model in model_dic:  # 读出每个回归模型对象
#     scores = cross_val_score(model, X, y, cv=n_folds)  # 将每个回归模型导入交叉检验模型中做训练检验
#     cv_score_list.append(scores)  # 将交叉检验结果存入结果列表
#     pre_y_list.append(model.fit(X, y).predict(X))  # 将回归训练中得到的预测y存入列表

# # 模型效果指标评估
# n_samples, n_features = X.shape  # 总样本量,总特征数
# model_metrics_name = [explained_variance_score, mean_absolute_error, mean_squared_error, r2_score]  # 回归评估指标对象集
# model_metrics_list = []  # 回归评估指标列表
# for i in range(5):  # 循环每个模型索引
#     tmp_list = []  # 每个内循环的临时结果列表
#     for m in model_metrics_name:  # 循环每个指标对象
#         tmp_score = m(y, pre_y_list[i])  # 计算每个回归指标结果
#         tmp_list.append(tmp_score)  # 将结果存入每个内循环的临时结果列表
#     model_metrics_list.append(tmp_list)  # 将结果存入回归评估指标列表
# df1 = pd.DataFrame(cv_score_list, index=model_names)  # 建立交叉检验的数据框
# df2 = pd.DataFrame(model_metrics_list, index=model_names, columns=['ev', 'mae', 'mse', 'r2'])  # 建立回归指标的数据框
# print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
# print (70 * '-')  # 打印分隔线
# print ('cross validation result:')  # 打印输出标题
# print (df1)  # 打印输出交叉检验的数据框
# print (70 * '-')  # 打印分隔线
# print ('regression metrics:')  # 打印输出标题
# print (df2)  # 打印输出回归指标的数据框
# print (70 * '-')  # 打印分隔线
# print ('short name \t full name')  # 打印输出缩写和全名标题
# print ('ev \t explained_variance')
# print ('mae \t mean_absolute_error')
# print ('mse \t mean_squared_error')
# print ('r2 \t r2')
# print (70 * '-')  # 打印分隔线

# # 模型效果可视化
# plt.figure()  # 创建画布
# plt.plot(np.arange(X.shape[0]), y, color='k', label='true y')  # 画出原始值的曲线
# color_list = ['r', 'b', 'g', 'y', 'c']  # 颜色列表
# linestyle_list = ['-', '.', 'o', 'v', '*']  # 样式列表
# for i, pre_y in enumerate(pre_y_list):  # 读出通过回归模型预测得到的索引及结果
#     plt.plot(np.arange(X.shape[0]), pre_y_list[i], color_list[i], label=model_names[i])  # 画出每条预测结果线
# plt.title('regression result comparison')  # 标题
# plt.legend(loc='upper right')  # 图例位置
# plt.ylabel('real and predicted value')  # y轴标题
# plt.show()  # 展示图像

# # 模型应用
# print ('regression prediction')
# new_point_set = [[1.05393, 0., 8.14, 0., 0.538, 5.935, 29.3, 4.4986, 4., 307., 21., 386.85, 6.58],
#                  [0.7842, 0., 8.14, 0., 0.538, 5.99, 81.7, 4.2579, 4., 307., 21., 386.75, 14.67],
#                  [0.80271, 0., 8.14, 0., 0.538, 5.456, 36.6, 3.7965, 4., 307., 21., 288.99, 11.69],
#                  [0.7258, 0., 8.14, 0., 0.538, 5.727, 69.5, 3.7965, 4., 307., 21., 390.95, 11.28]]  # 要预测的新数据集
# for i, new_point in enumerate(new_point_set):  # 循环读出每个要预测的数据点
#     new_pre_y = model_gbr.predict(np.array(new_point).reshape(1,-1))  # 使用GBR进行预测
#     print ('predict for new point %d is:  %.2f' % (i + 1, new_pre_y))  # 打印输出每个数据点的预测信息

# ----------------------------------------------------------

# 4.3 分类分析
# 导入库
# import numpy as np  # 导入numpy库
# from sklearn.model_selection import train_test_split  # 数据分区库
# from sklearn import tree  # 导入决策树库
# from sklearn.metrics import accuracy_score, auc, confusion_matrix, f1_score, precision_score, recall_score, \
#     roc_curve  # 导入指标库
# import prettytable  # 导入表格库
# import pydotplus  # 导入dot插件库
# import matplotlib.pyplot as plt  # 导入图形展示库

# # 数据准备
# raw_data = np.loadtxt(r'D:\OneDrive\python\python_code\python数据分析\chapter4\classification.csv', delimiter=',', skiprows=1, )  # 读取数据文件
# X = raw_data[:, :-1]  # 分割X
# y = raw_data[:, -1]  # 分割y
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)  # 将数据分为训练集和测试集

# # 训练分类模型
# model_tree = tree.DecisionTreeClassifier(random_state=0)  # 建立决策树模型对象
# model_tree.fit(X_train, y_train)  # 训练决策树模型
# pre_y = model_tree.predict(X_test)  # 使用测试集做模型效果检验

# # 输出模型概况
# n_samples, n_features = X.shape  # 总样本量,总特征数
# print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
# print (70 * '-')  # 打印分隔线

# # 混淆矩阵
# confusion_m = confusion_matrix(y_test, pre_y)  # 获得混淆矩阵
# confusion_matrix_table = prettytable.PrettyTable()  # 创建表格实例
# confusion_matrix_table.add_row(confusion_m[0, :])  # 增加第一行数据
# confusion_matrix_table.add_row(confusion_m[1, :])  # 增加第二行数据
# print ('confusion matrix')
# print (confusion_matrix_table)  # 打印输出混淆矩阵

# # 核心评估指标
# y_score = model_tree.predict_proba(X_test)  # 获得决策树的预测概率
# fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])  # ROC
# auc_s = auc(fpr, tpr)  # AUC
# accuracy_s = accuracy_score(y_test, pre_y)  # 准确率
# precision_s = precision_score(y_test, pre_y)  # 精确度
# recall_s = recall_score(y_test, pre_y)  # 召回率
# f1_s = f1_score(y_test, pre_y)  # F1得分
# core_metrics = prettytable.PrettyTable()  # 创建表格实例
# core_metrics.field_names = ['auc', 'accuracy', 'precision', 'recall', 'f1']  # 定义表格列名
# core_metrics.add_row([auc_s, accuracy_s, precision_s, recall_s, f1_s])  # 增加数据
# print ('core metrics')
# print (core_metrics)  # 打印输出核心评估指标

# # 模型效果可视化
# names_list = ['age', 'gender', 'income', 'rfm_score']  # 分类模型维度列表
# color_list = ['r', 'c', 'b', 'g']  # 颜色列表
# plt.figure()  # 创建画布
# # 子网格1：ROC曲线
# plt.subplot(1, 2, 1)  # 第一个子网格
# plt.plot(fpr, tpr, label='ROC')  # 画出ROC曲线
# plt.plot([0, 1], [0, 1], linestyle='--', color='k', label='random chance')  # 画出随机状态下的准确率线
# plt.title('ROC')  # 子网格标题
# plt.xlabel('false positive rate')  # X轴标题
# plt.ylabel('true positive rate')  # y轴标题
# plt.legend(loc=0)
# # 子网格2：指标重要性
# feature_importance = model_tree.feature_importances_  # 获得指标重要性
# plt.subplot(1, 2, 2)  # 第二个子网格
# plt.bar(np.arange(feature_importance.shape[0]), feature_importance, tick_label=names_list, color=color_list)  # 画出条形图
# plt.title('feature importance')  # 子网格标题
# plt.xlabel('features')  # x轴标题
# plt.ylabel('importance')  # y轴标题
# plt.suptitle('classification result')  # 图形总标题
# plt.show()  # 展示图形

# # 保存决策树规则图为PDF文件
# dot_data = tree.export_graphviz(model_tree, out_file=None, max_depth=5, feature_names=names_list, filled=True,
#                                 rounded=True)  # 将决策树规则生成dot对象
# graph = pydotplus.graph_from_dot_data(dot_data)  # 通过pydotplus将决策树规则解析为图形
# graph.write_pdf("tree.pdf")  # 将决策树规则保存为PDF文件

# # 模型应用
# X_new = [[40, 0, 55616, 0], [17, 0, 55568, 0], [55, 1, 55932, 1]]
# print ('classification prediction')
# for i, data in enumerate(X_new):
    # y_pre_new = model_tree.predict(np.array(data).reshape(1,-1))
    # print ('classification for %d record is: %d' % (i + 1, y_pre_new))

# ----------------------------------------------------------

# df = pd.DataFrame(np.arange(6).reshape(2,3),index = ['a','b'],columns = ['col1','col2','col3'])

# df = df.reindex(['a','new','b'])

# print(df)

# print('{:*^60}'.format('split_line'))

# print(df.isnull().any(axis=1))

# ----------------------------------------------------------

# import dash_core_components

# print(dash_core_components.__version__)

# ----------------------------------------------------------

# import time

# start = time.time()

# df = pd.DataFrame({'a':[4,2,1,2,3],
#                    'b':[5,3,3,1,4]})


# df['rank_dense'] = df['b'].rank(method='dense')
# df['rank_first'] = df['b'].rank(method='first')
# df['rank_min'] = df['b'].rank(method='min')
# df['rank_max'] = df['b'].rank(method='max')

# df['group_rank'] = df.groupby('a')['b'].rank(method='dense')

# print(df)

# n = 10
# i = 2
# while(n):
#     i = i+i
#     n -= 1

# print(i)

# end = time.time()
# print ('time :',end-start)

# ----------------------------------------------------------

# def main():
#     price_now = 8.05
#     cost = 900 * 24.546
#     y1 = []
#     y2 = []

#     for i in range(100,15000,10):
#         price = (cost + i * price_now) / (900 + i)
#         money = i * price_now
#         y1.append(money)
#         y2.append(price)
#         print('when invest {0:.0f} , the new price is {1:.2f} '.format(money,price))

#     df = pd.DataFrame({'money':y1,'price':y2})


#     plt.plot(df.money, df.price, '-r')

#     plt.show()  

# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------

# df = pd.DataFrame(np.arange(60).reshape(20,3),columns = ['col1','col2','col3'])
# # print(df,'\n')

# gp = df.groupby('col1',as_index=False)['col2'].count()

# print(gp)


# for i , j in df.iterrows():
#     print('i:',i)
#     print('j:',j,'\n')

# for x in df.iterrows():
#     print('x:',x)
#     print('type_x:',type(x),'\n')

# a = tuple(range(1000))
# b = list(range(1000))

# print(a.__sizeof__()) # 8024
# print(b.__sizeof__()) # 9088

# a    = (1,2)
# # b    = [1,2] 

# c = {a: 1}     # OK
# # c = {b: 1}     # Error

# print(c)

# num = input(":")
# if float(num) < 0:
#     raise ValueError("Negative!")


# try:
#     # num = 5 / 0
#     print(n)
# except:
#     print("An error occurred")
#     raise ValueError

# temp = 10
# assert (temp >= 0), "Colder than absolute zero!"

# file = open("newfile.txt", "w")
# file.write("This has been written to a file")
# file.close()

# file = open("newfile.txt", "r")
# print(file.read())
# file.close()

# try:
#    f = open("newfile.txt")
#    print(f.read())
# finally:
#    f.close()

# print (print(1))


# nums = [55, 44, 33, 22, 11]

# if all([i > 5 for i in nums]):
#    print("All larger than 5")

# if any([i % 2 == 0 for i in nums]):
#    print("At least one is even")

# def counts(text,char):
#     count = 0
#     for i in text:
#         if i == char:
#             count += 1
    
#     return count

# with open('newfile.txt') as f:
#     text = f.read()

# # print(counts(text,'o'))

# for char in "abcdefghijklmnopqrstuvwxyz":
#   perc = 100 * counts(text, char) / len(text)
#   print("{0} - {1}%".format(char, round(perc, 2)))

# print((lambda x: x**2 + 5*x + 4) (4))

# def numbers(x):
#   for i in range(x):
#     if i % 2 == 0:
#       yield i

# print(list(numbers(11)))

# def decor(func):
#   def wrap():
#     print("============")
#     func()
#     print("============")
#   return wrap

# @decor
# def print_text():
#   print("Hello world!")

# print_text()

# # decorated = decor(print_text)
# # decorated()

# print(@decor)



# f = now
# f()

# def log(func):
#     def wrapper():
#         print ('call %s():' % func.__name__)
#         func()
#     return wrapper

# @log
# def now():
#     print ('2013-12-25')

# now()

# def j(x):
#     if x > 0:
#         return j(x) * j(x-1)
    
# j(5)

# def factorial(x):
#   if x == 1:
#     return 1
#   else: 
#     return x * factorial(x-1)
    
# print(factorial(5))

# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else: 
#     return fib(x-1) + fib(x-2)
# print(fib(4))

# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}

# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)

# from itertools import takewhile
# nums = [2, 4, 6, 7, 9, 8]
# a = takewhile(lambda x: x%2==0, nums)
# print(list(a))
# print(list(filter(lambda x: x%2==0, nums)))

# from itertools import product, permutations

# letters = ("A", "B")
# print(list(product(letters, range(2))))
# print(list(permutations(letters))) 

# class Dog:
#   def __init__(self, name, color):
#       self.name = name
#       self.color = color

#   def bark(self):
#       print(self.color)
#       print("Woof!")

# fido = Dog("Fido", "brown")
# print(fido.name)
# fido.bark()

# class Animal: 
#   def __init__(self, name, color):
#     self.name = name
#     self.color = color

# class Cat(Animal):
#   def purr(self):
#     print("Purr...")
        
# class Dog(Animal):
#   def bark(self):
#     print("Woof!")

# fido = Dog("Fido", "brown")
# print(fido.color)
# fido.bark()

# class A:
#   def method(self):
#     print("A method")
    
# class B(A):
#   def another_method(self):
#     print("B method")
    
# class C(B):
#   def third_method(self):
#     print("C method")
    
# c = C()
# c.method()
# c.another_method()
# c.third_method()

# class A:
#   def spam(self):
#     print(1)

# class B(A):
#   def spam(self):
#     print(2)
#     A().spam()
            
# B().spam()

# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def ad(self, other):
#     return Vector2D(self.x + other.x, self.y + other.y)

# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = Vector2D.ad(first + second)
# print(result.x)
# print(result.y)

# class SpecialString:
#   def __init__(self, cont):
#     self.cont = cont

#   def __add__(self, other):
#     line = "=" * len(other.cont)
#     return "\n".join([self.cont, line, other.cont])

# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam + hello)

# class SpecialString:
#   def __init__(self, cont):
#     self.cont = cont

#   def __gt__(self, other):
#     for index in range(len(other.cont)+1):
#       result = other.cont[:index] + ">" + self.cont
#       result += ">" + other.cont[index:]
#       print(result)

# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam > eggs

# import random

# class VagueList:
#   def __init__(self, cont):
#     self.cont = cont

#   def __getitem__(self, index):
#     return self.cont[index + random.randint(-1, 1)]

#   def __len__(self):
#     return random.randint(0, len(self.cont)*2)

# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])

# class Queue:
#   def __init__(self, contents):
#     self._hiddenlist = list(contents)

#   def push(self, value):
#     self._hiddenlist.insert(0, value)
   
#   def pop(self):
#     return self._hiddenlist.pop(-1)

#   def __repr__(self):
#     return "Queue({})".format(self._hiddenlist)

# queue = Queue([1, 2, 3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)

# class Spam:
#   __egg = 7
#   def print_egg(self):
#     print(self.__egg)

# s = Spam()
# s.print_egg()
# print(s._Spam__egg)
# print(s.__egg)

# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   def calculate_area(self):
#     return self.width * self.height

#   @classmethod
#   def new_square(cls, side_length):
#     return cls(side_length, side_length)

# square = Rectangle.new_square(5)
# print(square.calculate_area())

# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings

#   @staticmethod
#   def validate_topping(topping):
#     if topping == "pineapple":
#       raise ValueError("No pineapples!")
#     else:
#       return True

# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients) 

# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings

#   @staticmethod
#   def validate_topping(topping):
#     if topping == "pineapple":
#       raise ValueError("No pineapples!")
#       print('bug')
#     else:
#       return True

# ingredients = ["cheese", "onions", "spam","pineapple"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients) 

# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings
#     self._pineapple_allowed = False

#   @property
#   def pineapple_allowed(self):
#     return self._pineapple_allowed

#   @pineapple_allowed.setter
#   def pineapple_allowed(self, value):
#     if value:
#       password = input("Enter the password: ")
#       if password == "Sw0rdf1sh!":
#         self._pineapple_allowed = value
#       else:
#         raise ValueError("Alert! Intruder!")

# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)

# def get_input():
#   command = input(": ").split()
#   verb_word = command[0]
#   if verb_word in verb_dict:
#     verb = verb_dict[verb_word]
#   else:
#     print("Unknown verb {}". format(verb_word))
#     return

#   if len(command) >= 2:
#     noun_word = command[1]
#     print (verb(noun_word))
#   else:
#     print(verb("nothing"))

# def say(noun):
#   return 'You said "{}"'.format(noun)

# verb_dict = {
#   "say": say,
# }

# while True:
#   get_input()

# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     func()

# def foo():
#     print('i am foo')

# use_logging(foo)

# data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack'],
#         'Age':[25,26,25,23,30,29,23],
#         'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]
#         }

# df = pd.DataFrame(data)

# print(df)

# print('='*10)
# print(df['Age'].value_counts())

# print('='*10)
# print(df['Age'].value_counts(normalize=True))

# %%timeit print('''
# 今天在向数据库里面导入数据时，发现cvs文件竟然有180M，
# 用sqlserver自带的导入工具导了十几分钟，大概导入了百分之二，
# 而且会出现很多数据类型不匹配（还不知道什么原因，后面把所有类型的长度都加长了），
# 于是放弃了sqlserver自带的导入工具。
# ''')

# import timeit

# num = 1
# s = timeit.timeit('"-".join(str(n) for n in range(100))', number=num)
# print('time:{:.10f} s'.format(s / num) )

# n = 5
# with open(r'C:\Users\Xiaoji\Desktop\NisLog.txt') as f:
#     for line in f:
#         if n:
#             print(line.split('f'))
#             print('='*50)
#             n -= 1

# import pandas as pd

# reader = pd.read_csv(r'D:\VDownload\NYC Yellow Taxi data\green_tripdata_2013-08_2.csv', iterator=True)

# loop = True
# chunkSize = 10000
# chunks = []
# while loop:
#     try:
#         chunk = reader.get_chunk(chunkSize)
#         chunks.append(chunk)
#     except StopIteration:
#         loop = False
#         print ("Iteration is stopped.")
# df = pd.concat(chunks, ignore_index=True)

# m = re.findall(r"r[ua]n", "run ran ren")
# print(type(m))

# import datetime
# now = datetime.datetime.now()
# print("Current date and time : \n{}".format(now.strftime("%Y-%m-%d %H:%M:%S")))

# import math
# r = float(input("radius:"))
# Area = math.pi * (r ** 2)

# print('Area={}'.format(Area))

# x = '3, 5, 7, 23'
# l = x.split(',')
# t = tuple(l)

# print(l)
# print(t)

# n = 5
# n2 = n*10 + n
# n3 = n2*10 + n

# print(n3)

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

# l = [100,1000,2000]
# n = int(input("number"))

# if n in l:
# 	print('in')

mser = pd.Series(np.random.rand(6),index = [['white','white','blue','blue','red','red'],['up','down','up','down','up','down']])

print(mser.unstack())