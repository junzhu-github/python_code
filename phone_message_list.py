# coding: utf-8

# 导入库
import pandas as pd

# 导入表格
df = pd.read_excel(r'C:\百度云同步盘\小鸡理财\短信发送记录\短信名单.xlsx')

# 计算列数
n = df.shape[1]

# 合并数据
res = pd.DataFrame()
for i in range(int(n/2)):
    temp = df.iloc[:,[i*2,i*2+1]]
    temp.columns = ['用户名', '手机号']
    res = res.append(temp)

# 去重
res.drop_duplicates('用户名',inplace=True)

# 去空值
res.dropna(how = 'all',inplace=True)

# 计算人数
m = res.shape[0]
print('一共有  {}  人'.format(m))

# 导出名单
res.to_excel(r'C:\百度云同步盘\小鸡理财\短信发送记录\短信名单result.xlsx',index=False)