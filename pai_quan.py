# coding: utf-8

# 导入库
import os
import time

import numpy as np
import pandas as pd

print('派券系统启动!')
os.chdir(r'C:\百度云同步盘\小鸡理财\每日数据\派券')

start = time.time()

# 导入待派券名单
with pd.ExcelFile(r'C:\百度云同步盘\小鸡理财\每日数据\派券\1月派券.xlsx') as xlsx:
    df_jd_bj = pd.read_excel(xlsx,'经典本金')
    df_jd_lx = pd.read_excel(xlsx,'经典利息')
    df_cg = pd.read_excel(xlsx,'存管回款')
    df_quan = pd.read_excel(xlsx,'券')
    df_quaned = pd.read_excel(xlsx,'已派券')

# 合并回款表
df_hk = df_jd_bj.append([df_jd_lx,df_cg], ignore_index=True,sort=True)

# 整理回款表
df_hk['发放时间'] = pd.to_datetime(df_hk['预计本次发放时间'])
del df_hk['预计本次发放时间']

dtnow = pd.to_datetime('today')
day_of_week = dtnow.day_name()
print('Today is ',day_of_week)

if day_of_week == 'Friday':
	print('---happy 周末 !---\n')

	timediff = pd.Timedelta(1,unit='d')
	dt_ff_1 = dtnow + timediff
	dt_ff_1 = dt_ff_1.strftime('%Y.%m.%d')

	timediff = pd.Timedelta(2,unit='d')
	dt_ff_2 = dtnow + timediff
	dt_ff_2 = dt_ff_2.strftime('%Y.%m.%d')

	timediff = pd.Timedelta(3,unit='d')
	dt_ff_3 = dtnow + timediff
	dt_ff_3 = dt_ff_3.strftime('%Y.%m.%d')

	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff_1) | (df_hk['发放时间'] == dt_ff_2) | (df_hk['发放时间'] == dt_ff_3)]

	dt_ff = str(dt_ff_1) + '-' + str(dt_ff_3)
else:
	print('---平时 is choosed!---\n')
	timediff = pd.Timedelta(1,unit='d')
	dt_ff = dtnow + timediff
	dt_ff = dt_ff.strftime('%Y.%m.%d')
	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]

# 归类
class_pai = dict({'6月标':'派券2',
                  '12月标':'派券2',
                  360:'派券2',
                  180:'派券2',
                  90:'派券1',
                  30:'派券1'})
df_hk_today = df_hk_today.copy()
df_hk_today['分类'] = df_hk_today.loc[:,'投资期限'].map(class_pai)

# 记录回款人数和金额
hk_pp = df_hk_today['会员名'].nunique()
hk_money = round(df_hk_today['本次发放金额'].sum() / 10000)

# 合并计算，排除当日回款金额小于500元
# 排除总金额<0
gp_hk = df_hk_today.groupby('会员名',as_index=False)['本次发放金额'].sum()
l500 = gp_hk[gp_hk['本次发放金额'] >= 0]['会员名']
# l500
df_hk_today_res_1 = df_hk_today[df_hk_today['会员名'].isin(l500)]
# 记录回款金额小于500元的人数
pp_500 = gp_hk[gp_hk['本次发放金额'] < 0]['会员名']
pp_500_num = len(pp_500)


# 排除有3张券以上的人
df_quan['mark'] = 1
df_quan_1 = df_quan[~(df_quan['大类'] == '现金券')]	# 排除现金券
gp_quan = df_quan_1.groupby('会员名',as_index=False)['mark'].sum()
q3 = gp_quan[gp_quan['mark'] >= 3]['会员名']
df_hk_today_res_2 = df_hk_today_res_1[~(df_hk_today_res_1['会员名'].isin(q3))]
# 记录拥有3张券以上的人数
df_q3 = df_hk_today[df_hk_today['会员名'].isin(q3)]
df_q3_num = df_q3['会员名'].nunique()



# 排除已经派了5次的人
df_quaned_select = df_quaned.loc[df_quaned['券别名'].isin(['小鸡暖冬福利（1）','小鸡暖冬福利（3）']),:]
gp_quaned = df_quaned_select.groupby('会员名',as_index=False)['ID'].count()
p4 = gp_quaned[gp_quaned['ID'] >= 5]
df_hk_today_res_3 = df_hk_today_res_2[~(df_hk_today_res_2['会员名'].isin(p4['会员名']))]
# 记录已经发放5次券包的人数
df_p4 = df_hk_today[df_hk_today['会员名'].isin(p4['会员名'])]
df_p4_num = df_p4['会员名'].nunique()


# 确定要派哪类券
gp_class = df_hk_today_res_3.groupby(['会员名','真实姓名','分类'])['本次发放金额'].sum().unstack()
gp_class.fillna(0,inplace=True)
if len(gp_class.columns) == 1:
	gp_class['派券分类'] = gp_class.columns[0]
else:
	gp_class['派券分类'] = np.where(gp_class['派券2'] == 0,'派券1','派券2')

print('名单整理完成! 开始导出EXCEL...')

# 查找用户名等信息
res_temp = gp_class.copy()
res_temp = res_temp.reset_index()
res = res_temp.loc[:,['会员名','真实姓名','派券分类']]
# 记录本次派券人数
p_num = res['会员名'].nunique()

# 导出到表格
name = str(dt_ff) + '派券名单' + '.xlsx'
res.to_excel(name)

# 记录已派券名单
# df_x = df_rcd['会员名'].append(res.reset_index()['会员名'])
# df_record = df_x.to_frame()
# df_record.head()
# df_record.to_excel('已派券记录.xlsx',index=False)

print('名单导出完成!')

write_time = time.time()

print('本次派券运行: {:.2f} s\n'.format(write_time-start))


print('''
TO 财务部：

附件是 {} 派券名单!
	'''.format(dt_ff))
print('{} 回款信息:共回款 {:.0f} 人，合计回款金额 {:.0f} 万元。'.format(dt_ff,hk_pp,hk_money))

print('其中拥有3张券以上的 {} 人，已经发放5次券包的 {} 人。\n\n{} 需派券 {} 人！'.format(
        df_q3_num,df_p4_num,dt_ff,p_num))

# print('其中回款金额小于0元 {} 人，拥有3张券以上的 {} 人，已经发放5次券包的 {} 人。\n\n{} 需派券 {} 人！'.format(
#         pp_500_num,df_q3_num,df_p4_num,dt_ff,p_num))
