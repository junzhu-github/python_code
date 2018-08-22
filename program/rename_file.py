# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:59:23 2018

@author: ying
"""

#导入os库
import os

#设置要修改的目录
#！必须保证目录内只有要修改的文件，不能含有文件夹
dir_path = 'G:\wangwangduilidagong\汪汪队立大功 第四季'

#修改工作目录
os.chdir(dir_path)

#进入循环
for i in os.listdir('.'):
    #分离，提取要修改成的文件名
    s = i.split(' ',3)[3]
    
    #重命名文件
    os.rename(i,s)

    #成功打印
    print ("重命名成功。")