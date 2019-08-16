# coding: utf-8

# 导入库
import os
import time

import numpy as np
import pandas as pd

print('\n派券系统启动!\n')
os.chdir(r'C:\百度云同步盘\小鸡理财\每日数据\派券')

start = time.time()

# 导入待派券名单
with pd.ExcelFile(r'C:\百度云同步盘\小鸡理财\每日数据\派券\8月派券.xlsx') as xlsx:
    df_cg = pd.read_excel(xlsx,'存管回款')
    df_quan = pd.read_excel(xlsx,'券')
    df_quaned = pd.read_excel(xlsx,'已派券')
    df_quan_used = pd.read_excel(xlsx,'券使用')

# 合并回款表
df_hk = df_cg.copy()

# 整理回款表
df_hk['发放时间'] = pd.to_datetime(df_hk['预计本次发放时间'])
del df_hk['预计本次发放时间']

dtnow = pd.to_datetime('today')
day_of_week = dtnow.day_name()
dt_hour = pd.datetime.now().hour
print('Today is ',day_of_week)

if day_of_week == 'Friday':
	print('---happy 周末 !---\n')

	timediff = pd.Timedelta(1,unit='d')
	dt_ff_1 = dtnow + timediff
	dt_ff_1 = dt_ff_1.strftime('%Y.%m.%d')
    
    # 周末天数，默认 2 天
	weekend_num = 2
	timediff = pd.Timedelta(weekend_num,unit='d')
	dt_ff_2 = dtnow + timediff
	dt_ff_2 = dt_ff_2.strftime('%Y.%m.%d')

	df_hk_today = df_hk[(df_hk['发放时间'] >= dt_ff_1) & (df_hk['发放时间'] <= dt_ff_2)]

	dt_ff = str(dt_ff_1) + '-' + str(dt_ff_2)
elif day_of_week == 'Monday' and dt_hour < 12:
	print('---上班干活!---\n')
	timediff = pd.Timedelta(0,unit='d')
	dt_ff = dtnow + timediff
	dt_ff = dt_ff.strftime('%Y.%m.%d')

	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]
else:
	print('---平时 is choosed!---\n')
	timediff = pd.Timedelta(1,unit='d')
	dt_ff = dtnow + timediff
	dt_ff = dt_ff.strftime('%Y.%m.%d')
	df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]


# 判断回款表是否正确
if df_hk_today.shape[0] == 0:
    # print(df_hk_today.head())
    print('回款表有错误！')
    exit()
else:
    pass


# 归类
class_pai = {360:'派券2',
            180:'派券2',
            90:'派券1',
            30:'派券1'}
df_hk_today = df_hk_today.copy()
df_hk_today['分类'] = df_hk_today.loc[:,'投资期限'].map(class_pai)

# 记录回款人数和金额
hk_pp = df_hk_today['会员名'].nunique()
hk_money = round(df_hk_today['本次发放金额'].sum() / 10000)


# 合并计算，排除当日回款金额小于 0 元
# 排除总金额 < 0
gp_hk = df_hk_today.groupby('会员名',as_index=False)['本次发放金额'].sum()
l500 = gp_hk[gp_hk['本次发放金额'] >= 0]['会员名']
# l500
df_hk_today_res_1 = df_hk_today[df_hk_today['会员名'].isin(l500)]
# 记录回款金额小于500元的人数
pp_500 = gp_hk[gp_hk['本次发放金额'] < 0]['会员名']
pp_500_num = len(pp_500)


# 排除有 3 张券以上的人
df_quan['mark'] = 1
df_quan_1 = df_quan[~(df_quan['大类'] == '现金券')]	# 排除现金券
gp_quan = df_quan_1.groupby('会员名',as_index=False)['mark'].sum()
q3 = gp_quan[gp_quan['mark'] >= 3]['会员名']
df_hk_today_res_2 = df_hk_today_res_1[~(df_hk_today_res_1['会员名'].isin(q3))]
# 记录拥有 3 张券以上的人数
df_q3 = df_hk_today[df_hk_today['会员名'].isin(q3)]
df_q3_num = df_q3['会员名'].nunique()


# 排除已经派了 4 次的人
df_quaned_select = df_quaned.loc[df_quaned['券别名'].isin(['清凉一夏（1）','清凉一夏（3）']),:]
gp_quaned = df_quaned_select.groupby('会员名',as_index=False)['ID'].count()
p4 = gp_quaned[gp_quaned['ID'] >= 4]
df_hk_today_res_3 = df_hk_today_res_2[~(df_hk_today_res_2['会员名'].isin(p4['会员名']))]
# 记录已经发放 4 次券包的人数
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
p_num_13 = res.loc[res['派券分类']=='派券1','会员名'].nunique()
p_num_612 = res.loc[res['派券分类']=='派券2','会员名'].nunique()
p_num = res['会员名'].nunique()

# 导出到表格
name = str(dt_ff) + '派券名单' + '.xlsx'
res.to_excel(name)

print('名单导出完成!')

write_time = time.time()

print('本次派券运行: {:.2f} s\n'.format(write_time-start))


print('''
TO 财务部：

附件是 {} 派券名单!
	'''.format(dt_ff))
print('{} 回款信息:共发放 {:.0f} 人，合计发放金额 {:.0f} 万元。'.format(dt_ff,hk_pp,hk_money))

# print('其中发放金额小于500元 {} 人，当日拥有3张券及以上的 {} 人，当月已发放3次券包的 {} 人。\n\n{} 需派 券包1: {} 人，券包2: {} 人，合计 {} 人！'.format(
#         pp_500_num,df_q3_num,df_p4_num,dt_ff,p_num_13,p_num_612,p_num))

print('其中当日拥有3张券及以上的 {} 人，当月已发放4次券包的 {} 人。\n\n{} 需派 券包1: {} 人，券包2: {} 人，合计 {} 人！'.format(
        df_q3_num,df_p4_num,dt_ff,p_num_13,p_num_612,p_num))

# print('\n派券名单已提交系统，请审核！')



# 券使用统计

## 券表格整理
def table_clean(df):
    # 冻结→已使用
    select_name = ['清凉一夏（1）','清凉一夏（2）','清凉一夏（3）','清凉一夏（4）']
    df = df[df['券别名'].isin(select_name)].copy()
    df['使用情况'] = df['使用状态'].replace('投标冻结','已使用')

    # 汇总
    gp_use_rate = df.groupby(by=['利息率','使用情况']).agg({'会员名':np.size,'冻结的匹配金额':np.sum}).unstack().fillna(0)
    gp_use_rate[0,'合计发放(张)'] = gp_use_rate['会员名'].sum(axis=1)
    gp_use_rate[0,'使用率%'] = round(gp_use_rate[('会员名','已使用')] / gp_use_rate[(0,'合计发放(张)')] * 100,2)
    gp_use_rate[0,'投资金额'] = round(gp_use_rate[('冻结的匹配金额','已使用')],0)
    gp_use_rate[0,'单券投资金额'] = round(gp_use_rate[('冻结的匹配金额','已使用')] / gp_use_rate[('会员名','已使用')],2)

    # 删除多余列
    gp_use_rate.drop(columns=('冻结的匹配金额'),inplace=True)

    # 去除多级列名称
    gp_use_rate.columns = gp_use_rate.columns.droplevel()

    # 重做行名称
    gp_use_rate.reset_index(inplace=True)

    return gp_use_rate


## 将表格导出为图片
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, title=None,**kwargs):
    
    import matplotlib.pyplot as plt
    import six
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    # 生成表格
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    # 隔行添加背景色
    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    
    ax.set_title(title,fontsize=18)
    ax.set_axis_off()

    return ax

## 设定手动开关
switch = 0

if day_of_week == 'Friday' and switch:

    # 本月发券使用统计
    df_month_quan_used = df_quan_used[df_quan_used['生效时间'] >= dtnow.strftime('%Y-%m-01')]

    # 累计发券使用统计
    df_all_quan_used = df_quan_used

    gp_month_quan_used = table_clean(df_month_quan_used)
    gp_all_quan_used =  table_clean(df_all_quan_used)

    size = (np.array(gp_month_quan_used.shape[::-1]) + np.array([0, 1])) * np.array([3.0, 0.625*2])
    fig, (ax1, ax2) = plt.subplots(2,1,figsize=size)

    render_mpl_table(gp_month_quan_used, ax=ax1, header_columns=0, col_width=2.0, title='本月发券使用统计')
    render_mpl_table(gp_all_quan_used, ax=ax2, header_columns=0, col_width=2.0, title='累计发券使用统计')

    plt.show()
