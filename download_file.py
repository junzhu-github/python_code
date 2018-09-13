# import requests


# # 通过requests库下载文件
# url = 'https://web.umeng.com/main.php?c=flow&a=detail&ajax=module=report&siteid=1254745261&st=2018-09-12&et=2018-09-12&visitorFrom=pv&pageType=30&currentPage=1&visitorType=&visitorAgent=&visitorAct=&location=&refererType=&ip=&referer=&keyword=&hour=24&page=&cnzz_eid=&downloadType=csv'
# # url = 'https://cg.xiaojilicai.com/admin/member/index?user_type=0&uname=&cellphone=&realname=&fp_name=&company_name=&market_source=&fp_source=&source=&lx=&bj=&money=&is_old_user=0&start_time=2018-09-01&end_time=2018-09-11&start_time2=&end_time2=&start_time3=&end_time3=&start_time4=&end_time4=&export=1&__hash__=c837606798566198e600d91531403f9c_fa8be16a05777b204d67ff6754eb37d6'
# r = requests.get(url)


# print(r.content)

# with open("my.csv", "wb") as code:
#     code.write(r.content)

import urllib 

print ("downloading with urllib" )
url = 'http://www.pythontab.com/test/demo.zip'  
print ("downloading with urllib")
urllib.urlretrieve(url, "demo.zip")
