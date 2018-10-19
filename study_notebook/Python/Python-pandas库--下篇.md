## 11、pandas的分组操作
```
'''示例数组'''
df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils',],
         'Rank': [1, 2, 2,],
         'Year': [2014,2015,2014],
         'Points':[876,789,863]})
--->   Points  Rank    Team  Year
    0     876     1  Riders  2014
    1     789     2  Riders  2015
    2     863     2  Devils  2014
```
```
'''按 指定列 分组'''
df.groupby('Team')      #返回的是地址
---><pandas.core.groupby.DataFrameGroupBy object at 0x000000000705FC18>
----------------------------------------------------------------------------------
'''打印 分组'''
df.groupby(['Team','Year']).groups      #可以指定多个列分组
--->{('Devils', 2014): Int64Index([2], dtype='int64'), ('Riders', 2014): Int64Index([0], dtype='int64'), ('Riders', 2015): Int64Index([1], dtype='int64')}
----------------------------------------------------------------------------------
'''美美地打印 分组'''
for name,group in df.groupby(['Team','Year']):      #类似字典
    print(name)
    print(group)
--->('Devils', 2014)
       Points  Rank    Team  Year
    2     863     2  Devils  2014
    ('Riders', 2014)
       Points  Rank    Team  Year
    0     876     1  Riders  2014
    ('Riders', 2015)
       Points  Rank    Team  Year
    1     789     2  Riders  2015
```
```
'''获得分组内 某个具体的组别'''
df.groupby('Team').get_group('Riders')
--->   Points  Rank    Team  Year
    0     876     1  Riders  2014
    1     789     2  Riders  2015
```
```
'''组内的统计函数，'''
#求组内平均数
grouped.mean()
--->             Points  Rank
    Team   Year              
    Devils 2014     863     2
    Riders 2014     876     1
           2015     789     2

#在分组结果中加入前缀
grouped.mean().add_prefix('mean_')
--->
        mean_Points  mean_Rank
Team                                     
Devils        863.0        2.0
Riders        832.5        1.5


#将上面的一维表转换成二维表
grouped.mean().unstack()
--->       Points        Rank     
    Year     2014   2015 2014 2015
    Team                          
    Devils  863.0    NaN  2.0  NaN
    Riders  876.0  789.0  1.0  2.0
-----------------------------------------------------------------------------------
#可以针对其他未分组列进行统计,如求Point列的平均值、和、个数
df.groupby('Team')['Points'].agg([np.mean,np.sum,np.size])
--->         mean   sum  size      #统计分数列的指标
    Team                     
    Devils  863.0   863     1
    Riders  832.5  1665     2
```
```
'''分组后的函数运用'''
apply函数

#定义函数top
def top(df,n = 3, column = 'Year'):
    return df.sort_values(by=column, ascending=False)[:n]

#在组内调用函数
df.groupby('Team').apply(top)
--->          Points  Rank    Team  Year
    Team                                
    Devils 2     863     2  Devils  2014      #对每个Team按Year排倒序，并返回前3行
    Riders 1     789     2  Riders  2015
           0     876     1  Riders  2014

#可以直接在apply内对调用的函数传递参数
df.groupby('Team').apply(top,n = 1,column = 'Rank')
--->          Points  Rank    Team  Year
    Team                                
    Devils 2     863     2  Devils  2014
    Riders 1     789     2  Riders  2015

--------------------------------------------------------------------------------------------------------

transform函数

score = lambda x: (x - x.mean()) / x.std()*10
df.groupby('Team').transform(score)      #运用自定义公式
--->     Points      Rank      Year
    0  7.071068 -7.071068 -7.071068
    1 -7.071068  7.071068  7.071068
    2       NaN       NaN       NaN

----------------------------------------------------------------------------------

filter函数

filter = df.groupby('Team').filter(lambda x: len(x) >= 2)      #过滤行数
--->   Points  Rank    Team  Year
    0     876     1  Riders  2014
    1     789     2  Riders  2015
```
*************************************************************************************
## 12、pandas的连接操作
```
'''两个数组的左右合并-merge函数'''

#示例数组1
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})

--->     Name  id subject_id
    0    Alex   1       sub1
    1     Amy   2       sub2
    2   Allen   3       sub4
    3   Alice   4       sub6
    4  Ayoung   5       sub5
========================================
    Name  id subject_id
    0  Billy   1       sub2
    1  Brian   2       sub4
    2   Bran   3       sub3
    3  Bryce   4       sub6
    4  Betty   5       sub5
```
```
#根据1个或多个条件列合并
rs = pd.merge(left,right,on=['id','subject_id'])      #合并条件=id&subject_id
--->   Name_x  id subject_id Name_y
    0   Alice   4       sub6  Bryce
    1  Ayoung   5       sub5  Betty
----------------------------------------------------------------------------------
#左/右连接
rs = pd.merge(left, right, on='subject_id', how='left')      #same as how = 'right'
--->   Name_x  id_x subject_id Name_y  id_y
    0    Alex     1       sub1    NaN   NaN
    1     Amy     2       sub2  Billy   1.0
    2   Allen     3       sub4  Brian   2.0
    3   Alice     4       sub6  Bryce   4.0
    4  Ayoung     5       sub5  Betty   5.0
----------------------------------------------------------------------------------
#merge默认内连接，通过how参数修改为外连接
rs = pd.merge(left, right, how='outer', on='subject_id')
--->   Name_x  id_x subject_id Name_y  id_y
    0    Alex   1.0       sub1    NaN   NaN
    1     Amy   2.0       sub2  Billy   1.0
    2   Allen   3.0       sub4  Brian   2.0
    3   Alice   4.0       sub6  Bryce   4.0
    4  Ayoung   5.0       sub5  Betty   5.0
    5     NaN   NaN       sub3   Bran   3.0
----------------------------------------------------------------------------------
#！内连接效果，同上区别
rs = pd.merge(left, right, on='subject_id')
--->   Name_x  id_x subject_id Name_y  id_y
    0     Amy     2       sub2  Billy     1
    1   Allen     3       sub4  Brian     2
    2   Alice     4       sub6  Bryce     4
    3  Ayoung     5       sub5  Betty     5
----------------------------------------------------------------------------------
#改变连接关键列的名称
left = left.rename(columns = {'id':'left_id'})
right = right.rename(columns = {'id':'left_id'})

#连接函数有变化
pd.merge(left,right,left_on = 'left_id',right_on = 'right_id')
--->略
```
```
'''两个数组的 “上下”/“左右” 合并-concat函数'''
#示例数组2
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[0,1,2])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['e','b','c','d'],index=[1,2,3])
--->     a    b    c    d
    0  0.0  0.0  0.0  0.0
    1  0.0  0.0  0.0  0.0
    2  0.0  0.0  0.0  0.0
========================================
--->     e    b    c    d
    1  1.0  1.0  1.0  1.0
    2  1.0  1.0  1.0  1.0
    3  1.0  1.0  1.0  1.0
----------------------------------------------------------------------------------
#1、默认上下合并,可修改 axis=1 为左右合并
#2、默认外连接，可修改 join='inner' 为内连接,内连接去除带NaN的列
#3、可通过 ignore_index=True 参数对行索引重新命名
rs = pd.concat([df1,df2])
--->     a    b    c    d    e
    0  0.0  0.0  0.0  0.0  NaN
    1  0.0  0.0  0.0  0.0  NaN
    2  0.0  0.0  0.0  0.0  NaN
    1  NaN  1.0  1.0  1.0  1.0
    2  NaN  1.0  1.0  1.0  1.0
    3  NaN  1.0  1.0  1.0  1.0
----------------------------------------------------------------------------------
'''dataframe和series合并'''
#创建系列s
s = pd.Series(np.random.randn(5))
--->
0   -0.280951
1   -2.324420
2   -0.605283
3    0.347614
4    1.091512
dtype: float64

#创建数据帧df
df = pd.DataFrame(np.arange(9).reshape(3,3),columns = ['col1','col2','col3'])
--->
   col1  col2  col3
0     0     1     2
1     3     4     5
2     6     7     8


#df和s延横轴合并
df_concat = pd.concat([df,s],axis = 1)
--->
   col1  col2  col3         0
0   0.0   1.0   2.0 -0.280951
1   3.0   4.0   5.0 -2.324420
2   6.0   7.0   8.0 -0.605283
3   NaN   NaN   NaN  0.347614
4   NaN   NaN   NaN  1.091512

#df和s延纵轴合并
df_concat = pd.concat([df,s],axis = 0)
--->
   col1  col2  col3         0
0   0.0   1.0   2.0       NaN
1   3.0   4.0   5.0       NaN
2   6.0   7.0   8.0       NaN
0   NaN   NaN   NaN -0.280951
1   NaN   NaN   NaN -2.324420
2   NaN   NaN   NaN -0.605283
3   NaN   NaN   NaN  0.347614
4   NaN   NaN   NaN  1.091512
```
```
'''两个数组的上下合并-append函数'''
#append只有纵向合并，没有横向合并
rs = df1.append([df1,df2],ignore_index=True)
--->     a    b    c    d    e
    0  0.0  0.0  0.0  0.0  NaN
    1  0.0  0.0  0.0  0.0  NaN
    2  0.0  0.0  0.0  0.0  NaN
    3  NaN  1.0  1.0  1.0  1.0
    4  NaN  1.0  1.0  1.0  1.0
    5  NaN  1.0  1.0  1.0  1.0
    6  0.0  0.0  0.0  0.0  NaN
    7  0.0  0.0  0.0  0.0  NaN
    8  0.0  0.0  0.0  0.0  NaN
----------------------------------------------------------------------------------
#也可以与Series系列合并，同concat合并区别！
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
rs = df1.append(s1,ignore_index=True)
--->     a    b    c    d
    0  0.0  0.0  0.0  0.0
    1  0.0  0.0  0.0  0.0
    2  0.0  0.0  0.0  0.0
    3  1.0  2.0  3.0  4.0
```
```
'''部分重合 的数据合并-combine_first'''
s1 = pd.Series(np.arange(5))
--->
0    0
1    1
2    2
3    3
4    4
dtype: int32
s2 = pd.Series(np.arange(2,7),index = [1,2,3,4,5])
--->
1    2
2    3
3    4
4    5
5    6
dtype: int32

#以s1的数值优先如果没有则用s2的数字补充
s1.combine_first(s2)
--->
0    0.0
1    1.0
2    2.0
3    3.0
4    4.0
5    6.0
dtype: float64
```
```
'''近似匹配'''
left = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c']})
--->
    a left_val
0   1        a
1   5        b
2  10        c

right = pd.DataFrame({'a': [1, 2, 3, 6, 7],'right_val': [1, 2, 3, 6, 7]})
--->
   a  right_val
0  1          1
1  2          2
2  3          3
3  6          6
4  7          7

#只有左连接，根据left的'a'列，在right的'a'列查找比其小且最接近的值，同excel的vlookup模糊查找
pd.merge_asof(left, right, on='a')  #可选参数direction : ‘backward’ (default),‘forward’, or ‘nearest’
--->
    a left_val  right_val
0   1        a          1
1   5        b          3
2  10        c          7
----------------------------------------------------------------------------------
>>> quotes
                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

>>> trades
                     time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.048   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100

#在相同'ticker'条件下查找time最接近的值
pd.merge_asof(trades, quotes,
...                       on='time',
...                       by='ticker',
...                       tolerance=pd.Timedelta('2ms'))
--->
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
```
*************************************************************************************
## 13、pandas的时间/日期操作
```
'''对时间操作'''
#获取当前时间
pd.datetime.now()  --->2018-04-17 18:28:29.033226

#创建一个时间戳
pd.Timestamp('2018-11-01')  --->2018-11-01 00:00:00      #1
pd.Timestamp(0,unit='s')  --->1970-01-01 00:00:00      #2

#改变时间显示格式
#原格式
dtnow = pd.to_datetime('today')  --->Timestamp('2018-08-07 00:00:00')
#修改后格式
dtnow.strftime('%y-%m-%d')  --->'18-08-07'

#把不同格式时间转换为一样的时间戳
#！同时将格式转换为datetime64[ns]
pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None]))
--->0   2009-07-31    
    1   2019-10-10
    2          NaT
    dtype: datetime64[ns]

#创建一个时间范围
#！通过修改 freq='H' 参数可按小时累加
pd.date_range("12:00", "13:59", freq="30min")
--->DatetimeIndex(['2018-04-17 12:00:00', '2018-04-17 12:30:00','2018-04-17 13:00:00', '2018-04-17 13:30:00'],dtype='datetime64[ns]', freq='30T')
```
```
'''对日期操作'''
#创建日期范围
#！通过修改 freq='M' 参数可按月或按年累加
pd.date_range('2011/11/03', periods=5)
--->DatetimeIndex(['2011-11-03', '2011-11-04', '2011-11-05', '2011-11-06','2011-11-07'],dtype='datetime64[ns]', freq='D')

#通过指定偏移量
sum_offset = pd.tseries.offsets.Week(2)      #偏移量为2周
pd.date_range('1/1/2018', periods=10, freq=sum_offset)
--->DatetimeIndex(['2018-01-08', '2018-01-22', '2018-02-05', '2018-02-19',
               '2018-03-05'],dtype='datetime64[ns]', freq='2W')

#！同上区别，创建<工作日>日期范围
pd.bdate_range('2011/11/03', periods=5)      #pd.bdate_range  /  没了11/5和11/6
--->DatetimeIndex(['2011-11-03', '2011-11-04', '2011-11-07', '2011-11-08','2011-11-09'],dtype='datetime64[ns]', freq='B')      

#给定开始和结束日期，创建一个日期范围
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
--->DatetimeIndex(['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04','2017-11-05'],dtype='datetime64[ns]', freq='D')
```
```
#示例日期
rng = pd.date_range('1/1/2018', periods=10, freq='W-SAT')      #日期以周为频率，从指定日期“1/1/2018”之后的第一个周六开始，见结果
ts = pd.Series(np.arange(10), index=rng)
--->2018-01-06    0
2018-01-13    1
2018-01-20    2
2018-01-27    3
2018-02-03    4
2018-02-10    5
2018-02-17    6
2018-02-24    7
2018-03-03    8
2018-03-10    9
Freq: W-SAT, dtype: int32

'''索引日期'''
#当日期列为行索引时,对日期进行索引
ts[ts.index[2]]      #等同于ts['2018/01/13']、ts['20180113']
--->2

#以2为步长进行索引
ts[::2]      #从前往后
--->2018-01-06    0
2018-01-20    2
2018-02-03    4
2018-02-17    6
2018-03-03    8
Freq: 2W-SAT, dtype: int32

#索引指定“年月”
ts['2018-2']
--->2018-02-03    4
2018-02-10    5
2018-02-17    6
2018-02-24    7
Freq: W-SAT, dtype: int32

#索引指定日期之后的
#！注意before、after
ts.truncate(before='2018-3-1')
--->2018-03-03    8
2018-03-10    9
Freq: W-SAT, dtype: int32

#同上相反，索引指定日期之前的
ts.truncate(after='2018-3-1')
--->2018-01-06    0
2018-01-13    1
2018-01-20    2
2018-01-27    3
2018-02-03    4
2018-02-10    5
2018-02-17    6
2018-02-24    7
Freq: W-SAT, dtype: int32
-----------------------------------------------------------------------------------------
'''移动数据'''
#日期索引不变，数据值往后移动
ts.shift(1)
--->2018-01-06    NaN      #第一个数值变为NaN
2018-01-13    0.0
2018-01-20    1.0
2018-01-27    2.0
2018-02-03    3.0
2018-02-10    4.0
2018-02-17    5.0
2018-02-24    6.0
2018-03-03    7.0
2018-03-10    8.0
Freq: W-SAT, dtype: float64

#日期索引不变，数据值往前移动
ts.shift(-1)
2018-01-06    1.0
2018-01-13    2.0
2018-01-20    3.0
2018-01-27    4.0
2018-02-03    5.0
2018-02-10    6.0
2018-02-17    7.0
2018-02-24    8.0
2018-03-03    9.0
2018-03-10    NaN      #最后一个数值变为NaN
Freq: W-SAT, dtype: float64
-----------------------------------------------------------------------------------------

#检查日期索引是否有重复
ts.index.is_unique
--->True      #True=无重复

#对日期索引进行分组
grouped = ts.groupby(level=0)      # level=0

```
```
'''时间差操作'''
#创建一个时间差
timediff = pd.Timedelta(6,unit='s')      #unit可以是'd','h','m','s'
timediff = pd.Timedelta(seconds = 6)      #写法2                                                        
--->0 days 00:00:06

#时间差的加减
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
--->           A      B
    0 2012-01-01 0 days
    1 2012-01-02 1 days
    2 2012-01-03 2 days

df['C']=df['A']+df['B']      #也可以作减法
--->           A      B          C
    0 2018-01-01 0 days 2018-01-01
    1 2018-01-02 1 days 2018-01-03
    2 2018-01-03 2 days 2018-01-05

# 计算时间间隔
x = pd.Series(pd.date_range('2013-1-1', periods=3, freq='D'))
--->
0   2013-01-01
1   2013-01-02
2   2013-01-03
dtype: datetime64[ns]

# 直接相减得到时间差格式
x-s
--->
0   366 days
1   366 days
2   366 days
dtype: timedelta64[ns]

# 以下得到时间差整数
(x-s).dt.days
--->
0    366
1    366
2    366
dtype: int64
```
```
'''时间数据重采样'''
'''降采样'''
#示例数组1，注意行索引和数据列都包含日期
df = pd.DataFrame({'date': pd.date_range('2015-01-01', freq='W',periods=5),'a': np.arange(5)},
    index=pd.MultiIndex.from_arrays([[1,2,3,4,5],pd.date_range('2015-01-01', freq='W',periods=5)],names=['v','d']))

--->              a       date
    v d                       
    1 2015-01-04  0 2015-01-04
    2 2015-01-11  1 2015-01-11
    3 2015-01-18  2 2015-01-18
    4 2015-01-25  3 2015-01-25
    5 2015-02-01  4 2015-02-01

#按date列的日期以<月>为单位求a列的和
df.resample('M', on='date').sum()
--->            a
    date         
    2015-01-31  6
    2015-02-28  4

#按索引d列的日期以<月>为单位求a列的和
#！同上区别
df.resample('M', level='d').sum()
--->            a
    d            
    2015-01-31  6
    2015-02-28  4
--------------------------------------------------------------------------------------
#示例数组2
df = pd.DataFrame({'a': [1]*100},
    index=pd.date_range('2018-01-01', periods = 100))
--->            a
    2018-01-01  1
    2018-01-02  1
    2018-01-03  1
    2018-01-04  1
    2018-01-05  1

#按5天采样，并计算5天中的开盘、收盘、最高、最低值
df.resample('5D').ohlc()
--->              a               
               open high low close
    2018-01-01    1    1   1     1
    2018-01-06    1    1   1     1
    ......
    2018-04-01    1    1   1     1
    2018-04-06    1    1   1     1

#按月份重采样，注意用的是groupby()
df.groupby(lambda x: x.month).sum()
--->    a
    1  31
    2  28
    3  31
    4  10
```
```
'''升采样'''
#示例数组，按周一为间隔单位
df = pd.DataFrame(np.random.randn(2, 3),
                 index=pd.date_range('20170101', periods=2, freq='W-MON'),
                 columns=['S1', 'S2', 'S3'])
--->                  S1        S2        S3
    2017-01-02 -1.204836  0.538345 -0.933471
    2017-01-09  2.307653 -0.112200  0.942536

# 直接升采样会产生空值
df.resample('D').asfreq()
--->                  S1        S2        S3
    2017-01-02 -1.204836  0.538345 -0.933471
    2017-01-03       NaN       NaN       NaN
    2017-01-04       NaN       NaN       NaN
    2017-01-05       NaN       NaN       NaN
    2017-01-06       NaN       NaN       NaN
    2017-01-07       NaN       NaN       NaN
    2017-01-08       NaN       NaN       NaN
    2017-01-09  2.307653 -0.112200  0.942536

#ffill用NaN的前一个值填充，bfill用NaN的后一个值填充，可以指定填充个数
df.resample('D').ffill(2)
--->                  S1        S2        S3
    2017-01-02 -1.204836  0.538345 -0.933471
    2017-01-03 -1.204836  0.538345 -0.933471
    2017-01-04 -1.204836  0.538345 -0.933471
    2017-01-05       NaN       NaN       NaN
    2017-01-06       NaN       NaN       NaN
    2017-01-07       NaN       NaN       NaN
    2017-01-08       NaN       NaN       NaN
    2017-01-09  2.307653 -0.112200  0.942536

#采用线性填充
df.resample('D').interpolate('linear')
--->                  S1        S2        S3
    2017-01-02 -1.204836  0.538345 -0.933471
    2017-01-03 -0.703052  0.445410 -0.665470
    2017-01-04 -0.201268  0.352475 -0.397469
    2017-01-05  0.300517  0.259540 -0.129468
    2017-01-06  0.802301  0.166605  0.138533
    2017-01-07  1.304085  0.073670  0.406534
    2017-01-08  1.805869 -0.019265  0.674535
    2017-01-09  2.307653 -0.112200  0.942536
```
![日期和时间处理](https://upload-images.jianshu.io/upload_images/4353065-567f0b137257697c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![频率freq的参数设置1](https://upload-images.jianshu.io/upload_images/4353065-f2836c834eda1739.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![频率freq的参数设置2](https://upload-images.jianshu.io/upload_images/4353065-6923bea0bc9f90cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
*************************************************************************************
## 14、pandas的IO操作
```
#原始数据
   S.No    Name  Age       City  Salary
0     1     Tom   28    Toronto   20000
1     2     Lee   32   HongKong    3000
2     3  Steven   43   Bay Area    8300
3     4     Ram   38  Hyderabad    3900

'''csv文件'''
#读取
df = pd.read_csv('01.csv')

#指定索引列
df=pd.read_csv("01.csv",index_col=['S.No'])
--->        Name  Age       City  Salary
    S.No                                
    1        Tom   28    Toronto   20000
    2        Lee   32   HongKong    3000
    3     Steven   43   Bay Area    8300
    4        Ram   38  Hyderabad    3900

#修改指定列的数据类型
df=pd.read_csv("01.csv",index_col=['S.No'],dtype = {'Salary':np.float64})
df2.dtypes
--->Name      object
    Age        int64
    City      object
    Salary     float64      #由导入默认的int64 ---> float64
    dtype: object

#重新标注并取代默认导入的列名称
df=pd.read_csv("01.csv",names=['a','b','c','d','e'],header=0)
--->   a       b   c          d      e      #列名称变了，如果没有参数 header=0，保留原列名称行
    0  1     Tom  28    Toronto  20000
    1  2     Lee  32   HongKong   3000
    2  3  Steven  43   Bay Area   8300
    3  4     Ram  38  Hyderabad   3900

#跳过指定行数
df=pd.read_csv("01.csv", skiprows=2)
--->   2     Lee  32   HongKong  3000      #！列名称
    0  3  Steven  43   Bay Area  8300
    1  4     Ram  38  Hyderabad  3900
```
```
'''excel文件'''
#读取
with pd.ExcelFile('01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'Sheet1')
    df2 = pd.read_excel(xlsx,'Sheet2')

#查看表格统计信息
df1.info()
---><class 'pandas.core.frame.DataFrame'>
    RangeIndex: 233614 entries, 0 to 233613
    Data columns (total 3 columns):
    用户名     233614 non-null object
    真实姓名    141860 non-null object
    注册时间    233614 non-null object
    dtypes: object(3)
    memory usage: 14.3+ MB
    None

#写入
df.to_excel('001.xlsx')      #参数 index = False 可以不输出行索引
```
![IO文件类型](https://upload-images.jianshu.io/upload_images/4353065-05ae226d53de30d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
*************************************************************************************
## 15、pandas的可视化操作
```
'''示例数据组1'''
df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'))

#折线图
df.plot()

#条形图
df.plot.bar()

#堆积条形图
df.plot.bar()

#水平条形图
df.plot.barh()

#水平堆积条形图
df.plot.barh(stacked=True)
```
```
'''示例数据组2'''
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

#直方图，按列分图
df.plot.hist(bins=50)      #列合并在一张图，参数bins表示宽度
df.hist(bins=20)      #几列就几张图

#箱形图
df.plot.box()

#散点图
df.plot.scatter(x='a', y='b')      #x，y代表横纵坐标轴

#饼图
df.plot.pie(subplots=True)
```
*************************************************************************************
## 16、Pandas的类SQL用法
```
'''Pandas的类SQL用法'''
#示例数组
total_bill tip sex smoker day time size
59 48.27 6.73 Male No Sat Dinner 4
125 29.80 4.20 Female No Thur Lunch 6
141 34.30 6.70 Male No Thur Lunch 6
142 41.19 5.00 Male No Thur Lunch 5
143 27.05 5.00 Female No Thur Lunch 6
155 29.85 5.14 Female No Sun Dinner 5
156 48.17 5.00 Male No Sun Dinner 6
170 50.81 10.00 Male Yes Sat Dinner 3
182 45.35 3.50 Male Yes Sun Dinner 3
185 20.69 5.00 Male No Sun Dinner 5
187 30.46 2.00 Male Yes Sun Dinner 5
212 48.33 9.00 Male No Sat Dinner 4
216 28.15 3.00 Male Yes Sat Dinner 5

#SELECT用法
tips[['total_bill', 'tip', 'smoker', 'time']].head(5)      #查询某几列，.head(n)返回前n行  
--->   total_bill   tip smoker    time
    0       16.99  1.01     No  Dinner
    1       10.34  1.66     No  Dinner
    2       21.01  3.50     No  Dinner
    3       23.68  3.31     No  Dinner
    4       24.59  3.61     No  Dinner

-----------------------------------------------------------------------------------------

#WHERE用法
tips[tips['time'] == 'Dinner'].head(5)      #附加查询条件
--->   total_bill   tip     sex smoker  day    time  size
    0       16.99  1.01  Female     No  Sun  Dinner     2
    1       10.34  1.66    Male     No  Sun  Dinner     3
    2       21.01  3.50    Male     No  Sun  Dinner     3
    3       23.68  3.31    Male     No  Sun  Dinner     2
    4       24.59  3.61  Female     No  Sun  Dinner     4

-----------------------------------------------------------------------------------------

#GroupBy用法
tips.groupby('sex').size()      #计算性别人数      
--->sex
    Female    2
    Male      3
    dtype: int64

tips.groupby('sex')['total_bill'].count()      #计算total_bill列下的性别人数
--->sex
    Female 2
    Male 3
    Name: total_bill, dtype: int64

tips.groupby('day').agg({'tip': np.mean, 'day': np.size})      #求均值
--->    tip day
day
Fri 2.734737 19
Sat 2.993103 87

tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})
--->tip
            size mean
smoker day
No    Fri 4.0 2.812500
        Sat 45.0 3.102889
Yes    Fri 15.0 2.714000
        Sat 42.0 2.875476

```
*************************************************************************************
## 17、pandas的透视表操作
```
#示例数组
df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','MN','ON'],
                        'City' : ['Toronto','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
                        'Sales' : [13,6,16,8,4,3,1]})
--->        City Province  Sales
    0    Toronto       ON     13
    1   Montreal       QC      6
    2  Vancouver       BC     16
    3    Calgary       AL      8
    4   Edmonton       AL      4
    5   Winnipeg       MN      3
    6    Windsor       ON      1
```
```
#创建透视表
table = pd.pivot_table(df,values=['City'],index=['Province'],columns=['City'],aggfunc=np.size)

--->           Sales                                                     
    City     Calgary Edmonton Montreal Toronto Vancouver Windsor Winnipeg
    Province                                                             
    AL           1.0      1.0      NaN     NaN       NaN     NaN      NaN
    BC           NaN      NaN      NaN     NaN       1.0     NaN      NaN
    MN           NaN      NaN      NaN     NaN       NaN     NaN      1.0
    ON           NaN      NaN      NaN     1.0       NaN     1.0      NaN
    QC           NaN      NaN      1.0     NaN       NaN     NaN      NaN
```
```
#把二维透视表转成一维，同上区别
table.stack('City')

--->                    Sales
    Province City            
    AL       Calgary      1.0
             Edmonton     1.0
    BC       Vancouver    1.0
    MN       Winnipeg     1.0
    ON       Toronto      1.0
             Windsor      1.0
    QC       Montreal     1.0
```
*************************************************************************************
## 18、其他
```
#判断单个值是否存在
s = pd.Series(range(5))
print (s==4)
--->0    False
    1    False
    2    False
    3    False
    4     True
    dtype: bool

-------------------------------------------------------------------------

#判断多个值是否存在
s = pd.Series(list('abc'))
x = s.isin(['a', 'c', 'e'])      #返回的是系列的bool值
print (x)      
--->0     True
    1    False
    2     True
    dtype: bool
```
*************************************************************************************

> # [Pandas常用命令对照清单](http://www.cnblogs.com/everfight/p/pandas_data_sheet.html)
