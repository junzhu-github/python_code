# coding: utf-8

# 导入库
import pandas as pd

# 导入表格
df = pd.read_excel(r'C:\百度云同步盘\小鸡理财\短信发送记录\短信名单.xlsx')

# 短信黑名单
black_list = [13175198841,13588059774]

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

# 重建索引
res.reset_index(drop=True,inplace=True)

# 去除黑名单
for i in black_list:
    for j in res['手机号']:
        if i == j: 
            print('\n{} 击中黑名单！'.format(i))
            res.drop(res[res['手机号'] == j].index,inplace=True)

# 计算人数
m = res.shape[0]
print('\n 一共有  {}  人\n'.format(m))

# 导出名单
res.to_excel(r'C:\百度云同步盘\小鸡理财\短信发送记录\短信名单result.xlsx',index=False)