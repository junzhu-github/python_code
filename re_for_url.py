'''
根据全部下载文件的url和已经存在的文件，找出未下载文件的url
'''

import os
import re

# def run_main():
    # 写入到文件

with open(r'D:\OneDrive\python\python_code\newfile.txt','r',encoding='utf-8-sig') as f:
    content = f.read()

m = re.findall(r"http.*/", content)

with open('result.txt','w') as res:
    for i in m:
        res.writelines(i)
        res.write('\n')


# if __name__ == '__main__':
#     run_main()