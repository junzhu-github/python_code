# -*- coding: utf-8 -*-

'''
study from here.

'''

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
def hannoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else: 
        hannoi(n-1,x,z,y)
        print(x,'-->',z)
        hannoi(n-1,y,x,z)

num = int(input('number:  '))

hannoi(num,'x','y','z')
'''
#---------------------------------------------------------------
'''
dict1 = {'李宁':'一切皆有可能','耐克':'just do it','阿迪达斯':'impossible is nothing'}

dict2 = dict((('f',70),('i',105),('s',115),('h',104),('c',67)))

dict3 = dict(小甲鱼='让编程改变世界',哈哈='呵呵哈哈哈')

dict4 = dict(one='1',two='2',three='3')

dict5 = dict('1'='one','2'='two')

dict1.fromkeys((1,2,3),('good','better','best'))
'''
#---------------------------------------------------------------
'''
list1 = [0,1,2,3,4,5,5,3,1]

for i in list1:
    for j in list1.remove(i):
        if i == j:
'''
#---------------------------------------------------------------           
'''
f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")

boy = []
girl = []
num = 1

for i in f:
    if i[:3] == '小甲鱼':
        boy.append(i.split('：')[1])
    
    if i[:3] == '小客服':
        girl.append(i.split('：')[1])


    if i[:3] == '===':
        boy_file = "boy_" + str(num) + ".txt"
        girl_file = "girl_" + str(num) + ".txt"
        
        b = open(boy_file,"w")
        b.writelines(boy)
        b.close()
        print("boy_file saved")
        
        g = open(girl_file,"w")
        g.writelines(girl)
        g.close()
        print("girl_file saved")
      
        boy = []
        girl = []
        num += 1


boy_file = "boy_" + str(num) + ".txt"
girl_file = "girl_" + str(num) + ".txt"
        
b = open(boy_file,"w")
b.writelines(boy)
b.close()
print("last boy_file saved")

g = open(girl_file,"w")
g.writelines(girl)
g.close()
print("last girl_file saved")
  
print('byebye!')
'''
#--------------------------------------------------------------- 
'''
f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
l = [f.read().split()]

boy = []
girl = []
num = 1
boy_file = "boy_{0}.txt".format(num)
girl_file = "girl_{0}.txt".format(num)


for i in range(len(l[0])):
    list1 = l[0][i]
#    print(list1)
#    print('-'*50)
    
    if list1[:3] == '小甲鱼':
        boy.append(list1.split('：')[1])
    
    if list1[:3] == '小客服':
        girl.append(list1.split('：')[1])


    if list1[:3] == '===':
        b = open(boy_file,"w")
        b.write("\n".join(boy))
        b.close()
        print("boy_file saved")
        
        g = open(girl_file,"w")
        g.write("\n".join(girl))
        g.close()
        print("girl_file saved")
      
        boy = []
        girl = []
        list1 = []
        num += 1
        boy_file = "boy_{0}.txt".format(num)
        girl_file = "girl_{0}.txt".format(num)


b = open(boy_file,"w")
b.write("\n".join(boy))
b.close()
print("last boy_file saved")

g = open(girl_file,"w")
g.write("\n".join(girl))
g.close()
print("last girl_file saved")

print('byebye!')
'''
#--------------------------------------------------------------- 
'''
f = open('123456789.txt','w')

l = ['1','2','3']

f.writelines(l)

f.close()
'''
#--------------------------------------------------------------- 
'''
def save_file(boy,girl,num):
    boy_file = "boy_" + str(num) + ".txt"
    girl_file = "girl_" + str(num) + ".txt"
    
    b = open(boy_file,"w")
    b.writelines(boy)
    b.close()
    print("boy_file saved")
    
    g = open(girl_file,"w")
    g.writelines(girl)
    g.close()
    print("girl_file saved")
 
def split_file(file_name):
    f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
    
    boy = []
    girl = []
    num = 1
    
    for i in f:
        if i[:3] == '小甲鱼':
            boy.append(i.split('：')[1])   
        if i[:3] == '小客服':
            girl.append(i.split('：')[1]
        if i[:3] == '===':
            save_file(boy,girl,num)
            
            boy = []
            girl =[]
            num += 1
    
    save_file(boy,girl,num)
    f.close()  
    print('byebye!')


split_file('111.txt')
'''
#--------------------------------------------------------------- 
'''
import pickle

first_list = [1,2,'a','b',['一','二']]

f = open('my_list.pkl','wb')
pickle.dump(first_list,f)
f.close()

j = open('my_list.pkl','rb')
second_list = pickle.load(j)
print(second_list)
'''
#--------------------------------------------------------------- 
'''
class Person:
    def hell(self):
        print('father is running...')


class Other:
    def hello(self):
        print('other is running')

    
class Child(Person):
    def hello(self):
        super().hell()
        print('child is running...')

a = Person()
a.hell()
'''
#---------------------------------------------------------------
'''
class B:
    def pb(self):
        print('nozuonodie')

B.pb(B)
c = B()
c.pb()
print(c.__dict__)
'''
#---------------------------------------------------------------
'''
class A(str):
    def __new__(cls,string):
        string = string.upper()
        print('-'*20,string)
        return str.__new__(cls,string)

a1 = A('abc')
print(a1)
'''
#---------------------------------------------------------------
'''
class C:
    def __init__(self):
        print(self)
        print('__init__ is running')
    def __del__(self):
        print('__del__ is running')

c1 = C()

c2 = C()
'''
#---------------------------------------------------------------  
'''
class New_int(int):
    def __add__(self,other):
        print(self)
        print('*'*50)
        print(other)
        return int.__sub__(self,other)

a = New_int(1)
print('-'*50)
b = New_int(3)
print('-'*50)
print(a+b)
'''
#---------------------------------------------------------------  
'''
class Try_int(int):
    def __add__(self,other):
        print(type(self))
        print('*'*50)
        print(type(other))
        return int(self) + int(other)

a = Try_int(1)
print('-'*50)
b = Try_int(3)
print('-'*50)
print(a+b)
'''
#---------------------------------------------------------------  
'''
class Try_int(int):   
    def __add__(self,other):
        return Try_int.__add__(self,other)


a=Try_int(5)
b=Try_int(10)

print(a+b)
'''
#--------------------------------------------------------------- 
'''
class A(int):
    def __add__(self,other):
        print('A is running')
        return int(self) + int(other)
    
a1 = A(5)
print(a1)
print('-'*5)
a2 = A(10)
print(a2)
print('-'*10)
print(a1+a2)
'''
#--------------------------------------------------------------- 
'''
class Rec:
    def __init__(self,width = 0,heig = 0):
        self.width = width
        print(self.width,'-')
        self.heig = heig
        print(self.heig)
       
    def __setattr__(self,name,value):
        print('__setattr__')
        if name == "square":
            print(value)
            self.width = value
            self.name = value
        else:
            print("else")
            #self.name = value
            super().__setattr__(name,value)
            
    def getArea(self):
        return self.width * self.heig
        
a = Rec(4,5)
print('-'*50)
a.square = 10
print(a.getArea())
'''
#--------------------------------------------------------------- 
'''
string = 'hello|world'
it =iter(string)
print(it)
for i in it:
    print(next(it))
'''
#--------------------------------------------------------------- 
'''
class Fib(object):
    def __init__(self,n = 100):
        print('0'*20)
        self.a = 0
        self.b = 1
        self.n = n
        print('-'*50)
        
    def __iter__(self):
        print('1'*20)
        return self
            
    print('/'*50)
    
    def __next__(self):
        print('2'*20)
        self.a,self.b = self.b,self.a+self.b
        if self.a > self.n:
            print('3'*20)
            raise StopIteration
        print('4'*20)
        return self.a
    
fib = Fib(3)
print(next(fib))
print(next(fib))
print(next(fib))

'''
#--------------------------------------------------------------- 
'''
import numpy as np 
a = np.array([[1,2],[4,5]])
b = np.arange(4).reshape(2,2)  

print('a:\n',a)
print('b:\n',b)


print('-'*50)
print(a*b)

c_dot = np.dot(a,b)
print('-'*50)
print(c_dot)

print('-'*50)
print(np.sum(a,axis = 1))

print('-'*50)
print(a.reshape(1,4))

print('-'*50)
print(type(a))
'''
#--------------------------------------------------------------- 
'''
f1 = open('01.mp3','rb')

c = f1.readlines(
print(c)

f2 = open('01.txt','wb')

f2.write(c)

f2.close()
'''
#--------------------------------------------------------------- 
'''
with open('out.txt','r') as f:
    for each_line in f.readlines():
        print(each_line,'|')
    
f.close()
'''
#--------------------------------------------------------------- 
'''
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns = ['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns = ['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns = ['A','B','C','D'])
df4 = pd.DataFrame(np.ones((3,4))*3,columns = ['E','B','C','D'])


print(df1)
print(df2)
print(df3)
print(df4)
print('1-1'*50)

res1 = pd.concat([df1,df2,df3,df4])

print(res1)
print('2-2'*50)

res2 = pd.concat([df1,df2,df3,df4],ignore_index = True)

print(res2)
print('3-3'*50)

res3 = pd.concat([df1,df2,df3,df4],join = 'inner',ignore_index = True)

print(res3)
print('4-4'*50)

res4  = pd.merge(df3,df4,on = 'B',how = 'outer',suffixes = ('_df3','_df4'),indicator = True)

print(res4)
print('5-5'*50)
'''
#--------------------------------------------------------------- 
'''
import os

dir_num = 0
zi = {}

for root, dirs, files in os.walk(r'D:\OneDrive\python\book'):
#    print(root)
#    print(dirs)
#    print(files)
#    print('-'*50)
    dir_num += len(dirs)
    for i in files:
        k = os.path.splitext(i)[1]
        if k in zi:
            zi[k] += 1
        else:
            zi[k] = 1

for key,value in zi.items():
    print('该文件夹下共有类型为【%s】的文件 %s 个' % (key,value))
print('该文件夹下共有类型为【文件夹】的文件 %s 个' % (dir_num))
'''
#--------------------------------------------------------------- 
'''
import numpy as np

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 
print(x)
print('='*50)

y = np.random.rand(4,3)
print(y)
print('='*50)

print(y[x>5])
print('='*50)

print(y[(x>5) & (x%2==0)] )
print('='*50)

print(y[(x>5) | (x%2==0)] )
print('='*50)

print(np.extract(x>5,y))
print('='*50)
'''
#--------------------------------------------------------------- 
'''
b = [11,12,13,14,15]

for i,j in enumerate(b):
    print(i,':',j)
'''
#--------------------------------------------------------------- 
'''
import csv

# 数据集路径
data_path = r'D:\wait_for_study\小象学院-python数据分析\第一周\codes\01\object\survey.csv'


def run_main():
    """
        主函数
    """
    male_set = {'male', 'm'}  # “男性”可能的取值
    female_set = {'female', 'f'}  # “女性”可能的取值

    # 构造统计结果的数据结构 result_dict
    # 其中每个元素是键值对，“键”是国家名称，“值”是列表结构，
    # 列表的第一个数为该国家女性统计数据，第二个数为该国家男性统计数据
    # 如 {'United States': [20, 50], 'Canada': [30, 40]}
    # 思考：这里的“值”为什么用列表(list)而不用元组(tuple)
    result_dict = {}

    with open(data_path, 'r', newline='') as csvfile:
        # 加载数据
        rows = csv.reader(csvfile)
        for i, row in enumerate(rows):
            print(i,':',row)
#            input('press enter to continue...')

            if i == 0:
                # 跳过第一行表头数据
                continue

            if i != 0:
                print('正在处理第{}行数据...'.format(i))
            # 性别数据
            gender_val = row[2]
            country_val = row[3]

            # 去掉可能存在的空格
            gender_val = gender_val.replace(' ', '')
            # 转换为小写
            gender_val = gender_val.lower()

            # 判断“国家”是否已经存在
            if country_val not in result_dict:
                # 如果不存在，初始化数据
                result_dict[country_val] = [0, 0]

            # 判断性别
            if gender_val in female_set:
                # 女性
                result_dict[country_val][0] += 1
            elif gender_val in male_set:
                # 男性
                result_dict[country_val][1] += 1
            else:
                # 噪声数据，不做处理
                pass

    # 将结果写入文件
    with open('gender_country.csv', 'w', newline='', encoding='utf-16') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        # 写入表头
        csvwriter.writerow(['国家', '男性', '女性'])

        # 写入统计结果
        for k, v in list(result_dict.items()):
            csvwriter.writerow([k, v[0], v[1]])

if __name__ == '__main__':
    run_main()
'''
#--------------------------------------------------------------- 
'''
import math
import random

class Sample(object):
    """
        样本点类
    """
    def __init__(self, coords):
        self.coords = coords    # 样本点包含的坐标
        self.n_dim = len(coords)    # 样本点维度

    def __repr__(self):
        """
            输出对象信息
        """
        return str(self.coords)


def gen_random_sample(n_dim, lower, upper):
    """
        生成随机样本
    """
    sample = Sample([random.uniform(lower, upper) for _ in range(n_dim)])
    return sample

samples = [gen_random_sample(2, 0, 200) for _ in range(1000)]

print(len(samples))
'''
#--------------------------------------------------------------- 
'''
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
'''
#--------------------------------------------------------------- 
'''
df = pd.DataFrame(np.random.randn(1000,4),
                  index = range(1000),
                  columns = list('ABCD'))
df = df.cumsum()
#print(df)
#df.plot()
ax = df.plot.scatter(x ='A',y='B',color = 'lightblue')
df.plot.scatter(x ='C',y='D',color = 'yellow',ax = ax)
plt.show()
'''
#--------------------------------------------------------------- 
'''
x = np.linspace(-3,3,50)
y1 = x*2+1
y2 = x**3

#plt.figure()
#plt.plot(x,y1)


plt.figure(num = 3,figsize = (15,12))
l1, = plt.plot(x,y1,label = 'L1')
l2, = plt.plot(x,y2,linewidth = 5.0,linestyle = '--',label = 'L2')

#plt.legend(handles = [l1,l2],labels = ['aaa','bbb'],loc = 'best')
plt.legend()


#plt.xlim(-4,4)
#plt.ylim(0,30)

plt.xlabel('i am x')
plt.ylabel('i am y')

x0 = 2
y0 = x0*2+1
plt.scatter(x0,y0,s=50,color='b')
#plt.plot([x0,x0],[y0,0],'k--',lw=2.5)


plt.annotate(r'$2 * %s +1 = %s$' %(x0,y0),
             xy=(x0,y0),
             xycoords='data',
             xytext=(+30,-30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
             )

plt.text(-2.7,3,
         r'$this\ is\ some\ text$',
         fontdict={'size':16,'color':'r'})

#plt.xticks(np.linspace(-4,4,10))
#plt.yticks([0,5,10,15,20,25,30],
#           ['a','b','c','d','e','f','g'])

#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#
#ax.spines['bottom'].set_position(('data',0))
#ax.spines['left'].set_position(('data',0))


plt.show()
'''
#--------------------------------------------------------------- 
'''
n = 1024
X = np.random.randn(n)
Y = np.random.randn(n)
T = np.arctan2(Y,X) #for color value

plt.scatter(X,Y,
            c=T,
            alpha = 0.5)

plt.xlime((-2,2))
plt.ylime((-2,2))

plt.xticks(())
plt.yticks(())


plt.show()
'''
#--------------------------------------------------------------- 
'''
x = np.random.randn(5)
y = np.random.randn(5)

plt.figure()

plt.subplot(211)
plt.plot(x,y)

plt.subplot(234)
plt.plot(y,x)

plt.subplot(235)
plt.plot(x,x)

plt.subplot(236)
plt.plot(y,y)
'''
#--------------------------------------------------------------- 
'''
#需要展现的数据
data = np.arange(100, 201)

#设定x，y轴的最大、最小值
plt.axis([0,100,50,300])

#另一种设定x，y轴的最大、最小值的方式
#plt.xlim(0,100)
#plt.ylim(50,300)

#设定x，y轴标记号
plt.xticks(np.linspace(0,100,5,endpoint=True),['$zero$','$one$','one','two','three'])
plt.yticks(np.linspace(50,300,5,endpoint=True))



 #设定图表标题
plt.title('Easy as 1, 2, 3')

#设定x，y轴标签的字体，颜色
plt.xlabel('x numbers',fontsize=14, color='red')      
plt.ylabel('y numbers',fontsize=14, color='red')

#在图表内增加公式
plt.text(20, 250, r'$\mu=100,\ \sigma=15,\bigcap $')

#设置背景网格线
plt.grid(True)

#设置打印线段的颜色、线宽、线型
fig,ax = plt.subplots(1,1,figsize=(8,4))
print(fig)
print(ax)


plt.show()
'''
#--------------------------------------------------------------- 
'''
os.chdir(r'D:\JunZhu\My Downloads\code_data\code_data\data')

df = pd.read_csv('stock_data_sample.csv',encoding = 'gbk')

print(df.head())
print('='*50)

print(df.info())
print('='*50)

data = df[df['交易日期'] > pd.to_datetime('20160101')]
print(data.head())
print('='*50)
'''
#--------------------------------------------------------------- 
'''
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

df['three'] = np.where(df['one'] >= df ['two'],'one','two')

print(df)
'''
#--------------------------------------------------------------- 

dtnow = pd.to_datetime('today')


timediff = pd.Timedelta(1,unit='d')
dt_ff = dtnow + timediff

df = dt_ff.strftime('%Y-%m-%d')
print(df)

































































