#!/usr/bin/env python
# coding=utf-8
'''
@Date: 2019-04-25 10:45:51
@Author: YING
@LastEditTime: 2019-11-14 11:14:40
'''
# -*- coding: utf-8 -*- 

# @author: ying

import os

'''获取文件夹下包含子文件夹的所有文件类型和数量'''
def file_type_num(path):
    dir_num = 0
    zi = {}

    for root, dirs, files in os.walk(path):
    #    print('root: {}'.format(root))
    #    print('dirs: {}'.format(dirs))
    #    print('files: {}'.format(files))
    #    print('-'*50)
        
        dir_num += len(dirs)
        for i in files:
            print(os.path.getsize(i))
            k = os.path.splitext(i)[1]
            if k in zi:
                zi[k] += 1
            else:
                zi[k] = 1

    for key,value in zi.items():
        print('该文件夹下共有类型为【%s】的文件 %s 个' % (key,value))
    print('该文件夹下共有类型为【文件夹】的文件 %s 个' % (dir_num))


'''获取文件夹下包含子文件夹的所有文件路径'''
def list_file_walk(path):
    file_dict = {}
    # file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            
            # file_list.append(file_path)
            file_dict[file_path] = round(file_size / 1024 / 1024,2)  # 文件单位：MB
            # file_dict[file_path] = '$1234'
    
    return file_dict


file_path = r'E:\OneDrive - xbsf.cursotamandare.g12.br\我的资源\book\kindle人打包'

file_type_num(file_path)

# d = list_file_walk(file_path)
# print(d)

# with open('y.txt','w', encoding="utf-8") as f:
#     for k,v in d.items():
#         f.write(k + '   '+ str(v) + 'MB' + '\n')
print('~~~end~~~')