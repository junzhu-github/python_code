'''
根据全部下载文件的url和已经存在的文件，找出未下载文件的url
'''

import os
import re

def run_main():
    # 已经下载的文件名称
    file_name = os.listdir(r'D:\VDownload\NYC Yellow Taxi data')

    # 全部文件的下载url 
    with open(r'C:\Users\Xiaoji\Desktop\1024.txt') as f:
        all_url = f.readlines()


    l = []  # 用来存放未下载的url

    # 遍历全部url，找出未下载部分
    for i in all_url:
        match = re.search(r'(/)([fgy](.*))',i)
        if match:
            if match.group(2) not in file_name:
                l.append(i)

    # 写入到文件
    with open(r'C:\Users\Xiaoji\Desktop\url.txt','w') as w:
        for j in l:
            w.write(j)

if __name__ == '__main__':
    run_main()