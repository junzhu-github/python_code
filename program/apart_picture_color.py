#!/usr/bin/env python
# coding=utf-8
'''
@Date: 2019-08-19 16:03:47
@Author: YING
@LastEditTime: 2019-10-18 10:58:31
'''
import os
import time

import cv2
import numpy as np


def get_pic_matrix(pic_name):
    # print(cv2.imread(pic_name))
    return cv2.imread(pic_name)
    
def calu_max_gap(pic_matrix):
    pic_gap = []
        
    try:
        pic_matrix.shape
    except:
        # print("\n{} is not a jpg!".format(pic_matrix))
        return 'bug'
    else:
        for i in range(pic_matrix.shape[0]):
            for j in range(pic_matrix.shape[1]):
                gap = max(pic_matrix[i,j,:]) - min(pic_matrix[i,j,:])
                pic_gap.append(gap)
        return pic_gap
       
def move_pic(pic_name,moved_path):
    if not os.path.exists(moved_path):
        os.mkdir(moved_path)

    # source = os.path.join(path,pic_name)
    destination = os.path.join(moved_path,pic_name)
    os.rename(pic_name, destination)

def main():
    start_time = time.time()
    path = r'F:\迅雷下载\chuquan'
    move_to_path = r'F:\迅雷下载\black and white'
    not_pic_path = r'F:\迅雷下载\not a pic'
    normal_pic = r'F:\迅雷下载\normal_pic'

    os.chdir(path)
    print('程序已启动！')
    print('工作目录已更改为：',os.getcwd())
   
    pic_list = os.listdir('.')

    total_pic_num = len(pic_list)
    count_pct = 0
    is_bp_pic = 0
    not_pic = 0

    print('本次需处理 {} 张图片\n'.format(total_pic_num))
    
    for p in pic_list:
        pic_matrix = get_pic_matrix(p)
        pic_gap = calu_max_gap(pic_matrix)
        
        count_pct += 1
        print('\r已分析 {} 张，\
            已用时 {:.2f} s,\
            进度: {:.4%}'.format(count_pct,(time.time()-start_time),(count_pct / total_pic_num)),end='')
        
        if pic_gap == 'bug':
            not_pic +=1
            move_pic(p,not_pic_path)   
        elif max(pic_gap) < 50:   # 满足条件判断为黑白图片
            # print(p,'属于黑白图片！')
            is_bp_pic += 1
            
            # print('\n\r已找到 {} 张图片'.format(is_bp_pic),end='')
            move_pic(p,move_to_path)
        else:
            move_pic(p,normal_pic)
            
    # if is_bp_pic == 0:
    #     print('未找到黑白图片！'.format(is_bp_pic))
    
    print('\n\n本次处理 {} 张图片,\
        其中非图片 {} 张,\
        共发现黑白图片 {} 张。'.format(total_pic_num,not_pic,is_bp_pic))
    print('程序运行结束！')

main()
