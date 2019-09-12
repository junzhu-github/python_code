#!/usr/bin/env python
# coding=utf-8
'''
@Date: 2019-01-04 10:02:36
@Author: YING
@LastEditTime: 2019-09-04 17:51:41
'''
# coding: utf-8

# 导入库
import os
import smtplib
import time
import webbrowser
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

import numpy as np
import pandas as pd
import xlwings as xw

# 倒数计时器
def count_down(n,s='离程序关闭还有'):
    while n+1:
        print('\r{}：{:>2d}s'.format(s,n),end='')
        time.sleep(1)
        n -= 1

# 下载券表格
def download_data(url):
    webbrowser.open(url)

# 获得最新表格
def newest_xls():
    file_dir = r'C:\Users\Dragon\Downloads'
    file_dict = {}
    lists = os.listdir(file_dir) #先获取文件夹内的所有文件
    for i in lists: # 遍历所有文件
        ctime = os.stat(os.path.join(file_dir, i)).st_ctime
        file_dict[ctime] = i # 添加创建时间和文件名到字典
    max_ctime = max(file_dict.keys()) # 取值最大的时间
    print('\n当前目录最新文件为：',file_dict[max_ctime])

    return file_dict[max_ctime]

# 处理表格
def handle_xls(new_xls):
    app = xw.App(visible=False, add_book=False)
    xls = app.books.open(new_xls)
    sheet = xls.sheets[0]
    dataframe = sheet.range('A1').options(pd.DataFrame, expand='table').value
    xls.close()
    app.quit()   
    return dataframe

# 券名单生成
def coupon_list(dt_today,day_of_week,dt_hour,df_quan_not_use,df_quan_use):
    os.chdir(r'C:\百度云同步盘\小鸡理财\每日数据\派券')

    # 导入待派券名单
    with pd.ExcelFile(r'C:\百度云同步盘\小鸡理财\每日数据\派券\9月派券.xlsx') as xlsx:
        df_cg = pd.read_excel(xlsx,'存管回款')
        # df_quan_not_use = pd.read_excel(xlsx,'券')
        # df_quan_use = pd.read_excel(xlsx,'已派券')
        # df_quan_used = pd.read_excel(xlsx,'券使用')

    # 合并回款表
    df_hk = df_cg.copy()

    # 整理回款表
    df_hk['发放时间'] = pd.to_datetime(df_hk['预计本次发放时间'])
    del df_hk['预计本次发放时间']

    if day_of_week == 'Friday':
        print('\n---happy 周末 !---\n')

        timediff = pd.Timedelta(1,unit='d')
        dt_ff_1 = dt_today + timediff
        dt_ff_1 = dt_ff_1.strftime('%Y.%m.%d')
        
        # 周末天数，默认 2 天
        weekend_num = 2
        timediff = pd.Timedelta(weekend_num,unit='d')
        dt_ff_2 = dt_today + timediff
        dt_ff_2 = dt_ff_2.strftime('%Y.%m.%d')

        df_hk_today = df_hk[(df_hk['发放时间'] >= dt_ff_1) & (df_hk['发放时间'] <= dt_ff_2)]

        dt_ff = str(dt_ff_1) + '-' + str(dt_ff_2)
    elif day_of_week == 'Monday' and dt_hour < 12:
        print('\n---上班干活!---\n')
        timediff = pd.Timedelta(0,unit='d')
        dt_ff = dt_today + timediff
        dt_ff = dt_ff.strftime('%Y.%m.%d')

        df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]
    else:
        print('\n---平时 is choosed!---\n')
        timediff = pd.Timedelta(1,unit='d')
        dt_ff = dt_today + timediff
        dt_ff = dt_ff.strftime('%Y.%m.%d')
        df_hk_today = df_hk[(df_hk['发放时间'] == dt_ff)]


    # 判断回款表是否正确
    if df_hk_today.shape[0] == 0:
        # print(df_hk_today.head())
        print('回款表有错误！')
        exit()


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
    df_quan_not_use['mark'] = 1
    df_quan_1 = df_quan_not_use[~(df_quan_not_use['大类'] == '现金券')]	# 排除现金券
    gp_quan = df_quan_1.groupby('会员名',as_index=False)['mark'].sum()
    q3 = gp_quan[gp_quan['mark'] >= 3]['会员名']
    df_hk_today_res_2 = df_hk_today_res_1[~(df_hk_today_res_1['会员名'].isin(q3))]
    # 记录拥有 3 张券以上的人数
    df_q3 = df_hk_today[df_hk_today['会员名'].isin(q3)]
    df_q3_num = df_q3['会员名'].nunique()


    # 排除已经派了 4 次的人
    df_quaned_select = df_quan_use.loc[df_quan_use['券别名'].isin(['秋风送礼福利（1）','秋风送礼福利（3）']),:]
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

    # print('名单整理完成! 开始导出EXCEL...')

    # 查找用户名等信息
    res_temp = gp_class.copy()
    res_temp = res_temp.reset_index()
    res = res_temp.loc[:,['会员名','真实姓名','派券分类']]

    # 记录本次派券人数
    p_num_13 = res.loc[res['派券分类']=='派券1','会员名'].nunique()
    p_num_612 = res.loc[res['派券分类']=='派券2','会员名'].nunique()
    p_num = res['会员名'].nunique()

    # 导出到表格
    file_name = str(dt_ff) + '派券名单' + '.xlsx'
    res.to_excel(file_name)

    # print('EXCEL名单整理完成!')

    # print('\nTO 财务部：')
    # print('附件是 {} 派券名单!\n'.format(dt_ff))
    print('\n{} 回款信息:共发放 {:.0f} 人，合计发放金额 {:.0f} 万元。'.format(dt_ff,hk_pp,hk_money))

    # print('其中发放金额小于500元 {} 人，当日拥有3张券及以上的 {} 人，当月已发放3次券包的 {} 人。\n\n{} 需派 券包1: {} 人，券包2: {} 人，合计 {} 人！'.format(
    #         pp_500_num,df_q3_num,df_p4_num,dt_ff,p_num_13,p_num_612,p_num))

    print('其中当日拥有3张券及以上的 {} 人，当月已发放4次券包的 {} 人。\n{} 需派 券包1: {} 人，券包2: {} 人，合计 {} 人！'.format(
            df_q3_num,df_p4_num,dt_ff,p_num_13,p_num_612,p_num))
   
    string = '\nTO 财务部：\n附件是 {} 派券名单!\n{} 回款信息:共发放 {:.0f} 人，合计发放金额 {:.0f} 万元。\n其中当日拥有3张券及以上的 {} 人，当月已发放4次券包的 {} 人。\n\n{} 需派 券包1: {} 人，券包2: {} 人，合计 {} 人！'.format(dt_ff,dt_ff,hk_pp,hk_money,df_q3_num,df_p4_num,dt_ff,p_num_13,p_num_612,p_num)
    
    return file_name,string

# 券表格整理
def table_clean(df):
    # 冻结→已使用
    select_name = ['秋风送礼福利（1）','秋风送礼福利（2）','秋风送礼福利（3）','秋风送礼福利（4）']
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

# 将表格导出为图片
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

# 券使用统计
def coupon_statics():
    ## 设定手动开关
    switch = 0

    if day_of_week == 'Friday' and switch:

        # 本月发券使用统计
        df_month_quan_used = df_quan_used[df_quan_used['生效时间'] >= dt_today.strftime('%Y-%m-01')]

        # 累计发券使用统计
        df_all_quan_used = df_quan_used

        gp_month_quan_used = table_clean(df_month_quan_used)
        gp_all_quan_used =  table_clean(df_all_quan_used)

        size = (np.array(gp_month_quan_used.shape[::-1]) + np.array([0, 1])) * np.array([3.0, 0.625*2])
        fig, (ax1, ax2) = plt.subplots(2,1,figsize=size)

        render_mpl_table(gp_month_quan_used, ax=ax1, header_columns=0, col_width=2.0, title='本月发券使用统计')
        render_mpl_table(gp_all_quan_used, ax=ax2, header_columns=0, col_width=2.0, title='累计发券使用统计')

        plt.show()

# 发送邮件
def send_mail(file_name,string,mail_title = '回款派券'):
    ## 发件人和收件人信息
    smtp_server = 'smtp.mxhichina.com'  # 服务器
    sender = 'yingchao@xiaojilicai.cn'  # 发件人邮箱, 多人逗号分开
    password = 'fuck.123'
    receiver = 'geyani@xiaojilicai.cn,liuqiaoyan@xiaojilicai.cn'    # 收件人邮箱, 多人逗号分开
    cc='xujingcheng@xiaojilicai.cn,chenlijuan@xiaojilicai.cn'  # 抄送邮箱, 多人逗号分开
       
    ## 邮件的正文内容
    mail_content = string

    msg = MIMEMultipart() 
    msg.add_header('From',sender) 
    msg.add_header('To',receiver) 
    msg.add_header('Cc',cc)
    # msg.add_header('BCc',bcc) 
    msg.add_header('Subject',mail_title) 
    msg.attach(MIMEText(mail_content,'plain','utf-8')) 
    ##所有收信人信息
    receiver_list = ["liuqiaoyan@xiaojilicai.cn","geyani@xiaojilicai.cn"] ## 收件人邮箱, 多人逗号分开
    cc_list = ["xujingcheng@xiaojilicai.cn","chenlijuan@xiaojilicai.cn"]  # #抄送邮箱, 多人逗号分开

    toaddrs = receiver_list + cc_list  

    ## 添加附件
    with open(file_name, 'rb') as f:
        # 设置附件的MIME和文件名
        mime = MIMEBase('application','vnd.ms-excel')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=file_name)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(0)
    server.login(sender, password)
    server.sendmail(sender, toaddrs, msg.as_string())
    
    return server.quit()

def main():

    dt_today = pd.to_datetime('today')
    dt_today_day = pd.to_datetime('today').strftime('%Y-%m-%d')
    day_of_week = pd.to_datetime('today').day_name()
    dt_hour = pd.datetime.now().hour
    print('\nToday is {} {}'.format(dt_today_day,day_of_week))

    # 每月1号
    dt_month_01 = pd.to_datetime('today').strftime('%Y-%m-01')

    # 手动，截至2019-12-31
    handle = ['2019-09-12','2019-09-27','2019-09-29','2019-09-30','2019-10-11','2019-10-12']

    # 不用派券
    holiday = ['2019-09-13','2019-10-01','2019-10-02','2019-10-03','2019-10-04','2019-10-07'] 
    
    ## 日期判断
    if dt_today_day == dt_month_01:
        print('---跟新回款名单---')
        count_down(30,'离开始派券还有')
    
    if dt_today_day in handle:
        print('需要手工派券！')
        count_down(10000)
    elif dt_today_day in holiday or day_of_week in ['Saturday','Sunday']:
        print('今天是周末or节假日，不用派券！')
        count_down(100)
        exit()

    
    print('\n派券系统启动!')
    os.chdir(r'C:\Users\Dragon\Downloads')
    start = time.time()

    quan_not_use = 'https://cg.xiaojilicai.com/admin/coupon/publishcoupon?username=&realname=&cellphone=&company_name=&coupon_alias=&use_status=1&refer_id=&pack_name=&bill_id=&start_time=&end_time=&start_time2=&end_time2=&export=1&async=0&__hash__=e776bcc8348b125590c7d83c83cb054d_c884f04a16d4ae6d1fee5a9407ca9481'
    quan_use = 'https://cg.xiaojilicai.com/admin/coupon/publishcoupon?username=&realname=&cellphone=&company_name=&coupon_alias=%E7%A7%8B%E9%A3%8E%E9%80%81%E7%A4%BC%E7%A6%8F%E5%88%A9&use_status=&refer_id=&pack_name=&bill_id=&start_time=2019-09-01&end_time=&start_time2=&end_time2=&export=1&async=0&__hash__=e776bcc8348b125590c7d83c83cb054d_cb2b4970047067183088f7fd69988ce8'
    download_url = [quan_not_use,quan_use]
    xls_name = ['quan_not_use','quan_use']
    
    origin_file = newest_xls()
    count = 0
    
    for i,j in zip(xls_name,download_url):
        download_data(j)    # 下载
        count_down(30,s='下载等待')
        new_xls = newest_xls()  # 捕获下载文件
        
        n = 2
        while new_xls == origin_file:
            count_down(30,s='下载继续等待')
            new_xls = newest_xls()
            n -= 1

            if n == 0:
                print('下载文件错误，请手动检查')
                count_down(60)
                exit()
               
            
        new_df = handle_xls(new_xls)    # 转换下载文件
        globals()['df_'+str(i)] = new_df # 批量生成变量名
        # print ('df_'+str(i))

        count += 1
        print('第 {} 个表格已经完成。'.format(count))
    
        origin_file = new_xls

    coupon_list_name,coupon_string = coupon_list(dt_today,day_of_week,dt_hour,df_quan_not_use,df_quan_use)   
    
    end_time = time.time()

    print('\n派券表格已生成，本次运行时间: {:.2f} s\n'.format(end_time-start))
    count_down(60,'60s后发送邮件')
    

    # x = input('Press y to send mail...')
    # if str(x) == 'y':

    send_res,_ = send_mail(coupon_list_name,coupon_string)
    if send_res == 221:
        print('\n邮件发送成功！')
    else:
        print('\n邮件发送失败，需手动处理！')
    
    count_down(60)
    # print()    
    # input('Press any key to exit.')

main()
