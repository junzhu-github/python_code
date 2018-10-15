# coding: utf-8

# - 导入库
import os
import time
import numpy as np
import pandas as pd

print('begin_to_work!\n')
os.chdir(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据\派券')

start = time.time()

# - 导入待派券名单
with pd.ExcelFile(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据\派券\10月派券.xlsx') as xlsx:
    df_jd_bj = pd.read_excel(xlsx,'经典本金')
    df_jd_lx = pd.read_excel(xlsx,'经典利息')
    df_cg = pd.read_excel(xlsx,'存管回款')
    df_quan = pd.read_excel(xlsx,'券')

# - 导入已派券名单
df_rcd = pd.read_excel(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据\派券\已派券记录.xlsx')

print('import_ok!')

import_time = time.time()
print('import_time:{} s\n'.format(import_time-start))

# - 合并回款表
df_hk = df_jd_bj.append([df_jd_lx,df_cg], ignore_index=True,sort=True)

# - 整理回款表
df_hk['发放时间'] = pd.to_datetime(df_hk['预计本次发放时间'])
del df_hk['预计本次发放时间']

print('clean_ok!')

clean_time = time.time()
print('clean_time:{} s\n'.format(clean_time-import_time))

dtnow = pd.to_datetime('today')
day_of_week = dtnow.day_name()
hour_of_day = int(dtnow.hour)
print('Today is ',day_of_week)

if (day_of_week == 'Monday') & (hour_of_day < 12):
	print('---1 is choosed!---\n')
	timediff = pd.Timedelta(0,unit='d')
	dt_ff = dtnow + timediff
	dt_ff = dt_ff.strftime('%Y-%m-%d')
	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]
elif day_of_week == 'Friday':
	print('---2 is choosed!---\n')
	timediff = pd.Timedelta(-1,unit='d')
	dt_ff_1 = dtnow + timediff
	dt_ff_1 = dt_ff_1.strftime('%Y-%m-%d')
	timediff = pd.Timedelta(0,unit='d')
	dt_ff_2 = dtnow + timediff
	dt_ff_2 = dt_ff_2.strftime('%Y-%m-%d')
	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff_1) | (df_hk['发放时间'] == dt_ff_2)]
	dt_ff = '周末'
else:
	print('---3 is choosed!---\n')
	timediff = pd.Timedelta(1,unit='d')
	dt_ff = dtnow + timediff
	dt_ff = dt_ff.strftime('%Y-%m-%d')
	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]

# 周一回款
# dtnow = pd.to_datetime('today')
# timediff = pd.Timedelta(0,unit='d')
# dt_ff = dtnow + timediff
# dt_ff = dt_ff.strftime('%Y-%m-%d')
# df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]

# 周二-周四回款
# dtnow = pd.to_datetime('today')
# timediff = pd.Timedelta(1,unit='d')
# dt_ff = dtnow + timediff
# dt_ff = dt_ff.strftime('%Y-%m-%d')
# df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]

# 周五版筛选回款
# dtnow = pd.to_datetime('today')
# # ---
# timediff = pd.Timedelta(-1,unit='d')
# dt_ff_1 = dtnow + timediff
# dt_ff_1 = dt_ff_1.strftime('%Y-%m-%d')
# # ---
# timediff = pd.Timedelta(0,unit='d')
# dt_ff_2 = dtnow + timediff
# dt_ff_2 = dt_ff_2.strftime('%Y-%m-%d')
# df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff_1) | (df_hk['发放时间'] == dt_ff_2)]
# dt_ff = '周末'

#归类
class_pai = dict({'6月标':'派券2',
                  '12月标':'派券2',
                  360:'派券2',
                  180:'派券2',
                  90:'派券1',
                  30:'派券1'})

df_hk_today = df_hk_today.copy()
df_hk_today['分类'] = df_hk_today.loc[:,'投资期限'].map(class_pai)


# - 合并计算，排除当日回款金额小于1000元
#排除总金额<1000
gp_hk = df_hk_today.groupby('会员名',as_index=False)['本次发放金额'].sum()
l1000 = gp_hk[gp_hk['本次发放金额'] >= 1000]['会员名']
# l1000
df_hk_today_res_1 = df_hk_today[df_hk_today['会员名'].isin(l1000)]

# - 排除有2张券以上的人
df_quan['mark'] = 1
gp_quan = df_quan.groupby('会员名',as_index=False)['mark'].sum()
q2 = gp_quan[gp_quan['mark'] > 1]['会员名']
df_hk_today_res_2 = df_hk_today_res_1[~df_hk_today_res_1['会员名'].isin(q2)]

# - 排除已经派了3次的人
df_rcd['mark'] = 1
gp_rcd = df_rcd.groupby('会员名',as_index=False)['mark'].sum()
p3 = gp_rcd[gp_rcd['mark'] > 2]
df_hk_today_res_3 = df_hk_today_res_2[~df_hk_today_res_2['会员名'].isin(p3['会员名'])]

print('filter_ok!')

filter_time = time.time()
print('filter_time:{} s\n'.format(filter_time-clean_time))

# - 确定要派哪类券
gp_class = df_hk_today_res_3.groupby(['会员名','真实姓名','分类'])['本次发放金额'].sum().unstack()
gp_class.fillna(0,inplace=True)

if len(gp_class.columns) == 1:
	gp_class['派券分类'] = gp_class.columns[0]
else:
	gp_class['派券分类'] = np.where(gp_class['派券1'] > gp_class['派券2'],'派券1','派券2')

print('class_ok!')

class_time = time.time()
print('class_time:{} s\n'.format(class_time-filter_time))

# - 查找用户名等信息
res_temp = gp_class.copy()
res_temp = res_temp.reset_index()
res = res_temp.loc[:,['会员名','真实姓名','派券分类']]

# - 导出到表格
name = str(dt_ff) + '派券名单' + '.xlsx'
res.to_excel(name)

# - 记录已派券名单
df_x = df_rcd['会员名'].append(res.reset_index()['会员名'])
df_record = df_x.to_frame()

# df_record.head()
df_record.to_excel('已派券记录.xlsx',index=False)

print('write_ok!')

write_time = time.time()
print('write_time::{} s\n'.format(write_time-class_time))

print('ALL IS DONE!,TOTAL COST TIME:{} s\n'.format(write_time-start))
