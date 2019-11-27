#!/usr/bin/env python
# coding=utf-8
'''
@Date: 2019-11-26 17:41:28
@Author: YING
@LastEditTime: 2019-11-27 15:36:35
'''
import os
import time
import numpy as np
import pandas as pd


# 买币条件：
def buy_btc(n,price):
    df_btc.loc[n,'out_money'] = 1000
    df_btc.loc[n,'cum_out_money'] = df_btc.loc[n-1,'cum_out_money'] + 1000
    df_btc.loc[n,'in_amount'] = 1000 / price
    df_btc.loc[n,'cum_in_amount'] = df_btc.loc[n,'in_amount'] + df_btc.loc[n-1,'cum_in_amount']
    df_btc.loc[n,'out_amount'] = 0
    df_btc.loc[n,'cum_out_amount'] = df_btc.loc[n-1,'cum_out_amount']
    df_btc.loc[n,'in_money'] = 0
    df_btc.loc[n,'cum_in_money'] = df_btc.loc[n-1,'cum_in_money']
    df_btc.loc[n,'own_amount'] = df_btc.loc[n,'cum_in_amount'] - df_btc.loc[n,'cum_out_amount']
    df_btc.loc[n,'cost'] = (df_btc.loc[n,'cum_out_money'] - df_btc.loc[n,'cum_in_money']) / df_btc.loc[n,'own_amount']
    df_btc.loc[n,'cost_change_percent'] = (df_btc.loc[n,'cost'] / df_btc.loc[n-1,'cost'] -1) * 100
    df_btc.loc[n,'btc_value'] = price * df_btc.loc[n,'own_amount']
    df_btc.loc[n,'own_value'] = df_btc.loc[n,'btc_value'] + df_btc.loc[n,'cum_in_money']
    df_btc.loc[n,'value_gap'] = df_btc.loc[n,'own_value'] - df_btc.loc[n,'cum_out_money']
    df_btc.loc[n,'value_gap_percent'] = (df_btc.loc[n,'value_gap'] / df_btc.loc[n,'cum_out_money']) * 100

# 卖币条件：
def sale_btc(n,price,sale_btc_amount):
    df_btc.loc[n,'out_money'] = 0
    df_btc.loc[n,'cum_out_money'] = df_btc.loc[n-1,'cum_out_money']
    df_btc.loc[n,'in_amount'] = 0
    df_btc.loc[n,'cum_in_amount'] = df_btc.loc[n-1,'cum_in_amount']
    df_btc.loc[n,'out_amount'] = df_btc.loc[n-1,'own_amount'] * sale_btc_amount
    df_btc.loc[n,'cum_out_amount'] = df_btc.loc[n,'out_amount'] + df_btc.loc[n-1,'cum_out_amount']
    df_btc.loc[n,'in_money'] = df_btc.loc[n,'out_amount'] * price
    df_btc.loc[n,'cum_in_money'] = df_btc.loc[n,'in_money'] + df_btc.loc[n-1,'cum_in_money']
    df_btc.loc[n,'own_amount'] = df_btc.loc[n,'cum_in_amount'] - df_btc.loc[n,'cum_out_amount']
    df_btc.loc[n,'cost'] = (df_btc.loc[n,'cum_out_money'] - df_btc.loc[n,'cum_in_money']) / df_btc.loc[n,'own_amount']
    df_btc.loc[n,'cost_change_percent'] = (df_btc.loc[n,'cost'] / df_btc.loc[n-1,'cost'] -1) * 100
    df_btc.loc[n,'btc_value'] = price * df_btc.loc[n,'own_amount']
    df_btc.loc[n,'own_value'] = df_btc.loc[n,'btc_value'] + df_btc.loc[n,'cum_in_money']
    df_btc.loc[n,'value_gap'] = df_btc.loc[n,'own_value'] - df_btc.loc[n,'cum_out_money']
    df_btc.loc[n,'value_gap_percent'] = (df_btc.loc[n,'value_gap'] / df_btc.loc[n,'cum_out_money']) * 100

# 未达成买卖条件：
def no_action(n,price):
    df_btc.loc[n,'out_money'] = 0
    df_btc.loc[n,'cum_out_money'] = df_btc.loc[n-1,'cum_out_money']
    df_btc.loc[n,'in_amount'] = 0
    df_btc.loc[n,'cum_in_amount'] = df_btc.loc[n-1,'cum_in_amount']
    df_btc.loc[n,'out_amount'] = 0
    df_btc.loc[n,'cum_out_amount'] = df_btc.loc[n-1,'cum_out_amount']
    df_btc.loc[n,'in_money'] = 0
    df_btc.loc[n,'cum_in_money'] = df_btc.loc[n-1,'cum_in_money']
    df_btc.loc[n,'own_amount'] = df_btc.loc[n-1,'own_amount']
    df_btc.loc[n,'cost'] = df_btc.loc[n-1,'cost']
    df_btc.loc[n,'cost_change_percent'] = 0
    df_btc.loc[n,'btc_value'] = price * df_btc.loc[n,'own_amount']
    df_btc.loc[n,'own_value'] = df_btc.loc[n,'btc_value'] + df_btc.loc[n,'cum_in_money']
    df_btc.loc[n,'value_gap'] = df_btc.loc[n,'own_value'] - df_btc.loc[n,'cum_out_money']
    df_btc.loc[n,'value_gap_percent'] = (df_btc.loc[n,'value_gap'] / df_btc.loc[n,'cum_out_money']) * 100

# 条件判断
def btc_calculator(df_btc,below_percent_buy,above_price_percent,sale_btc_amount):
    
    for i in range(1,df_btc.shape[0]):
        price = df_btc.loc[i,'Close']
        if df_btc.loc[i-1,'cost'] * below_percent_buy - price >=0:
            buy_btc(i,price)
        elif price - df_btc.loc[i-1,'cost'] * above_price_percent >= 0:
            sale_btc(i,price,sale_btc_amount)
        else:
            no_action(i,price)
        
        if df_btc.loc[i,'cost'] <= 0 or df_btc.loc[i,'own_amount'] == 0:
            break        
    
    # print(df_btc[df_btc.out_amount > 0].head())
    df_res = df_btc.dropna(subset=['out_money'])
    xlsx_name = 'btc_' + str(below_percent_buy) + '_' + str(above_price_percent) + '_' + str(sale_btc_amount) + '.xlsx'
    df_res.to_excel(xlsx_name)

    # 结束日
    end_day = df_res.loc[df_res.index[-1],'Date']
    # 运行时长
    during_days = df_res.shape[0]
    # 最终投入金额  
    max_out_money = df_res['cum_out_money'].max()
    # 最大资产价值
    max_own_value = df_res['own_value'].max()
    # 最大资产价值的日期
    max_own_value_day = df_res.iloc[df_res['own_value'].idxmax(),0]
    # 最终资产价值
    last_own_value = df_res.loc[df_res.index[-1],'own_value']
    # 最大回撤
    max_recall_percent = df_res['value_gap_percent'].min()
    # 最大收益率
    max_earn_percent = df_res['value_gap_percent'].max()
    # 最大收益率日期
    max_earn_percent_day = df_res.iloc[df_res['value_gap_percent'].idxmax(),0]

    return [below_percent_buy,above_price_percent,sale_btc_amount,end_day,during_days,max_out_money,max_own_value,max_own_value_day,last_own_value,max_recall_percent,max_earn_percent,max_earn_percent_day]

# 切换工作目录
os.chdir(r'C:\Users\Dragon\OneDrive\invest\btc')

# 导入数据
df_btc_0 = pd.read_excel('btc_price.xlsx')

# 初始买入
df_btc_0.loc[0,'out_money'] = 1000
df_btc_0.loc[0,'cum_out_money'] = 1000
df_btc_0.loc[0,'in_amount'] = 1000 / 10931.4
df_btc_0.loc[0,'cum_in_amount'] = 1000 / 10931.4
df_btc_0.loc[0,'out_amount'] = 0
df_btc_0.loc[0,'cum_out_amount'] = 0
df_btc_0.loc[0,'in_money'] = 0
df_btc_0.loc[0,'cum_in_money'] = 0
df_btc_0.loc[0,'own_amount'] = 1000 / 10931.4
df_btc_0.loc[0,'cost'] = 10931.4
df_btc_0.loc[0,'cost_change_percent'] = np.nan
df_btc_0.loc[0,'btc_value'] = 1000
df_btc_0.loc[0,'own_value'] = 1000
df_btc_0.loc[0,'value_gap'] = 0
df_btc_0.loc[0,'value_gap_percent'] = np.nan

btc_list = []
res_list = []

n = 0
start_total = time.time()

# 循环计算
above_price_percent = 1.5
sale_btc_amount = 0.5
for below_percent_buy in [round(x * 0.1,2) for x in range(3, 10)]:
    for above_price_percent in [round(x * 0.1+1,2) for x in range(1, 21)]:
        for sale_btc_amount in [round(x * 0.1,2) for x in range(1, 11)]:
            
            start_loop = time.time()
            
            df_btc = df_btc_0.copy()
            # print(df_btc[~df_btc['out_money'].isnull()].shape)

            res_list = btc_calculator(df_btc,below_percent_buy,above_price_percent,sale_btc_amount)
            btc_list.append(res_list)

            n += 1
            end_loop = time.time()
            print('已计算{} 个条件：低于成本价买入：{}，高于成本价卖出：{}，卖出比例：{}，本次条件测试耗时 {:.2f} s'.format(n,below_percent_buy,above_price_percent,sale_btc_amount,end_loop-start_loop))


# below_percent_buy = 0.8
# above_price_percent = 1.5
# sale_btc_amount = 0.5
# df_btc = df_btc_0
# btc_calculator(df_btc,below_percent_buy,above_price_percent,sale_btc_amount)
# print(df_res)
# stop()

# 设置列字段
columns_name = ['低于成本价买入','高于成本价卖出','卖出比例','结束日','运行时长','最终投入金额','最大资产价值','最大资产价值的日期','最终资产价值','最大回撤','最大收益率','最大收益率日期']

# 生成结果数据帧
df = pd.DataFrame(btc_list,columns = columns_name)

# 导出表格
df.to_excel('btc_results.xlsx')

end_total = time.time()
print('全部数据已测试完成，总共用时 {:.2f} s。'.format(end_total - start_total))
