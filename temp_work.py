# -*- coding: utf-8 -*-


"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------
'''
#stuff = {'name':'zad','age':39,'height':6*12+2}
#print(stuff['name'])


#!/usr/bin/python3 

dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))  #how to use .get
print ("Sex 值为 : %s" %  dict.get('Sex'))


#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7}

print ("Value : %s" %dict.items())
'''
'''
def add(a,b):
    sum = a+b
    print(sum)
    
add(5,4)    
add(5,5)    
'''
'''
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
    
print(convert_number("a"))
'''
'''
import os
 
try:
     os._exit(0)
except:
     print ('die.')
'''
'''
i = 5
print(i)
i = i+1
print(i)

s = this is a mutli-line string.\
this is the second line.

print(s)
'''
'''
number=23
guess=int(input('Enter an integer : '))
if guess==number:
    print ('Congratulations, you guessed it.') # New block starts here
    print ("(but you do not win any prizes!)") # New block ends here
elif guess<number:
    print ('No, it is a little higher than that') # Another block
# You can do whatever you want in a block ...
else:
    print ('No, it is a little lower than that')
# you must have guess > number to reach here
print ('Done')
# This last statement is always executed, after the if statement is executed
'''
'''
import sys
print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('*'*10)
print("\n\nThe pythonpath is ",sys.path,'\n')
'''
'''
# 'ab' is short for 'a'ddress'b'ook
ab = { 'Swaroop' :'swaroopch@byteofpython.info',
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer' : 'spammer@hotmail.com'
      }

print(len(ab),'-'*10)
print("Swaroop's address is %s" %ab['Swaroop'])

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']
print('\nThere are %d contacts in the address-book\n' %len(ab))

for name,address in ab.items():
    print('Contact %s at %s' % (name, address))

if 'Guido' in ab: # OR ab.has_key('Guido')
    print("\nGuido's address is %s" % ab['Guido'])
'''
'''
shoplist = ['apple', 'mango', 'carrot', 'banana']

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
'''
'''
# Slicing on a string
name = 'swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
'''
'''
print('Simple Assignment')   
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print('\nCopy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del shoplist[0] # remove first item
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different
'''
'''
name = 'Swaroop'   # This is a string object
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
'''
'''
import os
print(os.getcwd())   
print(os.system('1'))

os.chdir('C:\FDownload')
print(os.getcwd())

os.chdir('../dowloads')
print(os.getcwd())

os.mkdir('a')
print(os.listdir())
print(os.getcwd())

os.makedirs('b/c/d')
print(os.listdir())
print(os.getcwd())

os.remove('a/1.txt')
os.removedirs('d')

print(os.name)
for i in os.listdir():
    print(i)
    
print('-'*100)

os.rename('新建文本文档.txt','123.txt')

for i in os.listdir():
    print(i)
'''
'''
import os 
def robocopy(source, target, thread=8):
    os.system( "robocopy %s %s /MT:%d /E"% (source.replace( "/", ""), target.replace( "/", ""), thread))
    
robocopy( "D:/source_test", "D:/copy_test")
'''
'''
#获取时间函数
import time
print
(time.strftime('%Y%m%d%H%M%S'))
'''
'''
import os

a = os.getcwd()
print(a)
print(os.listdir('.'))
print('-'*50)

b = os.chdir('D:\\222')
print(os.getcwd())

os.makedirs('D:\\222\\home\\monthly\\daily')

print(os.listdir())
print('-'*50)
'''

'''
print(a)
print('-'*50)
b = os.listdir('.')
print(b)
print(os.path.getmtime(a))
'''
'''
try:
    x = input('--->')
    print(int(x))
    if x < 10:
        raise("invalid x")
except ValueError as x:
    print(f"{x} is not a number")
except("invalid"):
    print(f"{x} is invalid")
else:
    print(f"number is {x}")
'''
'''
list = ['a','b','c']
print(f'before:{list}')

list.append('d')
print(f'after append:{list}')

add = ['e','f']
list.extend(add)
print(f'after extend:{list}')

list.insert(0,'0')
print(f'after insert:{list}')
'''


'''
list = ['a','b','c','e','f']
print(f'before:{list}')

pop1 = list.pop()
print(f'pop1:{pop1}')
print(f'after pop1:{list}')

pop2 = list.pop(0)
print(f'pop2:{pop2}')
print(f'after pop2:{list}')

remove = list.remove('b')
print(remove)
print(f'after remove:{list}')

del list[0]
print(f'after del:{list}')

del list
print(f'after del:{list}')
'''
'''
list = ['a','b','b','c','e','f']
print(list.count('b'))

print(list)
'''
'''
import xlrd

data= xlrd.open_workbook("C:\\Users\\ye\\xlrd\\nan.xlsx")
print(data.nsheets)

for s in data.sheets():
    print('Sheet:',s.name)
    print("行数：",s.nrows)
    print("列数：",s.ncols)
    for row in range(s.nrows):
        print('the row is:',row)
        values = []
        for col in range(s.ncols):
            print("row:",row," col:",col)
            print(s.cell(row,col))
            print("---",s.cell(row,col).value)
#            values.append(s.cell(row,col).value)
#        print(values)  
'''
'''
import xlrd

book = xlrd.open_workbook("D:\\小鸡理财\\OneDrive\\python\\xlrd\\learn_xlrd.xlsx")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))

list = []

for i in range(book.nsheets):
    print("-----{0}-----".format(i))
    sh = book.sheet_by_index(i)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    for rx in range(sh.nrows):
        list.append(sh.row(rx))
        print(sh.row(rx))
    print(r"++++++++++")
    
for n in list:
    print(n)
'''   
'''
from xlrd import open_workbook

wb = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls')

for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(','.join(values))
    print()
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook
book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls')

print("0 book.nsheets is {0}".format(book.nsheets))

for sheet_index in range(book.nsheets):
    print("1",book.sheet_by_index(sheet_index))
    print("2",book.sheet_names())

for sheet_name in book.sheet_names():
    print("3",book.sheet_by_name(sheet_name))

for sheet in book.sheets():
    print("4",sheet)
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook,cellname

book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
sheet = book.sheet_by_index(0)
    
print("1 sheet.name:{}".format(sheet.name))
print("2 sheet.nrows:{}".format(sheet.nrows))
print("3 sheet.ncols:{}".format(sheet.ncols))
print("-"*20)

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print('cellname:',cellname(row_index,col_index))        
        print('cellvalue:',sheet.cell(row_index,col_index).value)
        print("-"*10)
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook,XL_CELL_TEXT

book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
sheet = book.sheet_by_index(1)

cell = sheet.cell(0,0)

print('1 cell:',cell)
print('2 cell value:',cell.value)
print('3 cell type:',cell.ctype)
print(cell.ctype == XL_CELL_TEXT)

for i in range(sheet.ncols):
    print(sheet.cell_type(1,i))
    print(sheet.cell_value(1,i))
    print('-'*10)
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook
book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\odd.xls')
sheet0 = book.sheet_by_index(0)
sheet1 = book.sheet_by_index(1)
print(sheet0.row(0))
print(sheet0.row_values(0))
print(sheet0.col(0))
print(sheet0.col_values(0))

print()
print(sheet0.row_slice(0,1))
print(sheet0.row_slice(0,1,2))
print(sheet0.row_values(0,1))
print(sheet0.row_values(0,1,2))
print(sheet0.row_types(0,1))
print(sheet0.row_types(0,1,2))
print()
print(sheet1.col_slice(0,1))
print(sheet0.col_slice(0,1,2))
print(sheet1.col_values(0,1))
print(sheet0.col_values(0,1,2))
print(sheet1.col_types(0,1))
print(sheet0.col_types(0,1,2))
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import cellname, cellnameabs, colname
print(cellname(0,0),cellname(10,10),cellname(100,100))
print(cellnameabs(3,1),cellnameabs(41,59),cellnameabs(265,358))
print(colname(0),colname(10),colname(100))
'''
#------------------------------------------------------------------------------------------------
'''
from datetime import date,datetime,time
from xlrd import open_workbook,xldate_as_tuple

book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
sheet = book.sheets()[0]

date_value = xldate_as_tuple(sheet.cell(3,2).value,book.datemode)
print(sheet.cell(3,2).value)
print(date_value)
print(datetime(*date_value),'|',date(*date_value[:3]))
print('-'*30)

datetime_value = xldate_as_tuple(sheet.cell(3,3).value,book.datemode)
print(sheet.cell(3,3).value)
print(datetime_value)
print(datetime(*datetime_value),'|',date(*date_value[:3]))
print('-'*30)

time_value = xldate_as_tuple(sheet.cell(3,4).value,book.datemode)
print(sheet.cell(3,4).value)
print(time(*time_value[3:]))

#print(datetime(*time_value))
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook,error_text_from_code
book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
sheet = book.sheet_by_index(0)

print(error_text_from_code[sheet.cell(5,2).value])
print(error_text_from_code[sheet.cell(5,3).value])
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook,empty_cell

print('-',empty_cell.value,'-')


book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls')
sheet = book.sheet_by_index(0)
empty = sheet.cell(6,2)
blank = sheet.cell(7,2)
print(empty is blank, empty is empty_cell, blank is empty_cell)

book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls',formatting_info=True)
sheet = book.sheet_by_index(0)
empty = sheet.cell(6,2)
blank = sheet.cell(7,2)
print(empty.ctype,repr(empty.value))
print(blank.ctype,repr(blank.value))
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook

def cell_contents(sheet,row_x):
    result = []
    for col_x in range(2,sheet.ncols):
        cell = sheet.cell(row_x,col_x)
        result.append((cell.ctype,cell,cell.value))
    return result

sheet = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls').sheet_by_index(0)


print('XL_CELL_TEXT',cell_contents(sheet,1))
print('XL_CELL_NUMBER',cell_contents(sheet,2))
print('XL_CELL_DATE',cell_contents(sheet,3))
print('XL_CELL_BOOLEAN',cell_contents(sheet,4))
print('XL_CELL_ERROR',cell_contents(sheet,5))
print('XL_CELL_BLANK',cell_contents(sheet,6))
print('XL_CELL_EMPTY',cell_contents(sheet,7))
print()


sheet = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\types.xls',formatting_info=True).sheet_by_index(0)

print('XL_CELL_TEXT',cell_contents(sheet,1))
print('XL_CELL_NUMBER',cell_contents(sheet,2))
print('XL_CELL_DATE',cell_contents(sheet,3))
print('XL_CELL_BOOLEAN',cell_contents(sheet,4))
print('XL_CELL_ERROR',cell_contents(sheet,5))
print('XL_CELL_BLANK',cell_contents(sheet,6))
print('XL_CELL_EMPTY',cell_contents(sheet,7))
'''
#------------------------------------------------------------------------------------------------
'''
from xlrd import open_workbook

book = open_workbook('C:\\Users\\ye\\Downloads\\tutorial-master\\students\\xlrd\\simple.xls',on_demand=True)
for name in book.sheet_names():
    if name.endswith('2'):
        sheet = book.sheet_by_name(name)
        print(sheet.cell_value(0,0))
        book.unload_sheet(name)
        print(sheet.cell_value(0,0))
'''
#------------------------------------------------------------------------------------------------
'''
from tempfile import TemporaryFile
from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
book.add_sheet('Sheet 2')

sheet1.write(0,0,'A1')
sheet1.write(0,1,'B1')
row1 = sheet1.row(1)
row1.write(0,'A2')
row1.write(1,'B2')
sheet1.col(0).width = 10000

sheet2 = book.get_sheet(1)
sheet2.row(0).write(0,'Sheet 2 A1')
sheet2.row(0).write(1,'Sheet 2 B1')
sheet2.flush_row_data()
sheet2.write(1,0,'Sheet 2 A3')
sheet2.col(0).width = 5000
sheet2.col(0).hidden = True

book.save('simple.xls')
book.save(TemporaryFile())
'''
#------------------------------------------------------------------------------------------------
'''
def test(*params,exp):
    print('参数的长度是:',len(params))
    print('第二个参数是：',params[1])
    
test(1,'工作簿',3.14,50,88,exp=60)
'''
#------------------------------------------------------------------------------------------------
'''
def fun1():
    print('fun1 is working...')
    def fun2():
        print('fun2 is working......')
    fun2()
        
fun1()
'''
#------------------------------------------------------------------------------------------------
'''
def funx(x):
    def funy(y):
        return x*y
    return funy

i = funx(5)(8)
print(i)


def funx(x):
    print(x)
    def funy(y):
        return x*y
    funy
    

u = funx(5)
print(u)
'''
#------------------------------------------------------------------------------------------------
'''
def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()

i = fun1()
print(i)
'''
#------------------------------------------------------------------------------------------------
'''
def ds(x):
    return 3*x+10

print(ds(10) )

a = lambda x : 3*x+10
print(a(10))
'''
#------------------------------------------------------------------------------------------------
'''
def odd(x):
    return x % 2

temp = range(10)

show = map(odd,temp)

list(show)
'''
#------------------------------------------------------------------------------------------------
'''
def square(x):
    return x ** 2

temp = range(10)

show = map(square,temp)

list(show)
'''
#------------------------------------------------------------------------------------------------
'''
def cheng(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
        
    return result
        

num = int(input("输入一个数字:"))


print(num,"的阶乘是:",cheng(num))


def cheng(x):
    if x == 1:
        return 1
    else:
        return x * cheng(x-1)
    
num = int(input("输入一个数字:"))


print(num,"的阶乘是:",cheng(num))
'''
#------------------------------------------------------------------------------------------------
'''
result = [1,1]

a , b = 1 , 1

for i in range(10):
    a , b = b , a+b
    result.append(b)
    
print(result)
'''
#------------------------------------------------------------------------------------------------
'''
def hannoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hannoi(n-1,x,z,y)
        print(x,'-->',z)
        hannoi(n-1,y,x,z)
        
num = int(input('please enter a number:'))

hannoi(num,'X','Y','Z')
'''
#------------------------------------------------------------------------------------------------
'''
from xlwt import Workbook

book = Workbook()

sheet1 = book.add_sheet('sheet 1',cell_overwrite_ok=True)
sheet1.write(0,0,'original')
sheet = book.get_sheet(0)
sheet.write(0,0,'new')

#sheet2 = book.add_sheet('sheet 2')
#sheet2.write(0,0,'original')
#sheet2.write(0,0,'new')

book.save('1.xls')
'''
#------------------------------------------------------------------------------------------------
'''
from datetime import date,time,datetime
from decimal import Decimal
from xlwt import Workbook,Style

wb = Workbook()

ws = wb.add_sheet('Type examples')

ws.row(0).write(0,u'\xa3')
ws.row(0).write(1,'Text')

ws.row(1).write(0,3.1415)
ws.row(1).write(1,15)
ws.row(1).write(2,265)
ws.row(1).write(3,Decimal('3.65'))

ws.row(2).set_cell_number(0,3.1415)
ws.row(2).set_cell_number(1,15)
ws.row(2).set_cell_number(2,265)
ws.row(2).set_cell_number(3,Decimal('3.65'))


ws.row(3).write(0,date(2009,3,18))
ws.row(3).write(1,datetime(2009,3,18,17,0,1))
ws.row(3).write(2,time(17,1))
ws.row(4).set_cell_date(0,date(2009,3,18))
ws.row(4).set_cell_date(1,datetime(2009,3,18,17,0,1))
ws.row(4).set_cell_date(2,time(17,1))


ws.row(5).write(0,False)
ws.row(5).write(1,True)
ws.row(6).set_cell_boolean(0,False)
ws.row(6).set_cell_boolean(1,True)

ws.row(7).set_cell_error(0,0x17)
ws.row(7).set_cell_error(1,'#NULL!')

ws.row(8).write(
    0,'',Style.easyxf('pattern: pattern solid, fore_colour green;'))
ws.row(8).write(
    1,None,Style.easyxf('pattern: pattern solid, fore_colour blue;'))
ws.row(9).set_cell_blank(
    0,Style.easyxf('pattern: pattern solid, fore_colour yellow;'))

ws.row(10).set_cell_mulblanks(
    5,10,Style.easyxf('pattern: pattern solid, fore_colour red;')
    )

wb.save('types.xls')
'''
#------------------------------------------------------------------------------------------------
'''
from xlwt.Utils import rowcol_to_cell
from xlwt import Workbook, easyxf


book = Workbook()
sheet = book.add_sheet('A Date')

sheet.write(1,1,rowcol_to_cell(1,1))

book.save('1111111.xls')
'''
#------------------------------------------------------------------------------------------------
'''
dict1 = {'李宁':'一切皆有可能','耐克':'just do it','阿迪达斯':'impossible is nothing'}

dict2 = dict((('f',70),('i',105),('s',115),('h',104),('c',67)))

dict3 = dict(one='1',two='2',three='3')
'''
#------------------------------------------------------------------------------------------------
'''
def gd(n):
    list1 = []
    string = str(n)
#    length = len(string)
    for each in string:
        list1.append(each)
        
    return list1

a = gd(123456)
print(a)
'''
#------------------------------------------------------------------------------------------------
'''
import xlwt
from datetime import datetime
 
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='yyyy/m/d h:mm;@')
 
wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sheet')
 
ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, 1234.56,style1)
ws.write(1, 2, datetime.now(),style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
 
wb.save('example.xls')
'''
#------------------------------------------------------------------------------------------------
'''
import xlrd
#import xlwt
from xlutils.copy import copy

copy_wb = xlrd.open_workbook("2.xls",formatting_info=True)
copy_ws = copy_wb.sheets()[0]

list1 = []

for i in range(copy_ws.nrows):
    list1.append(copy_ws.row_values(i)) 
    

to_wb = xlrd.open_workbook("1.xls",formatting_info=True)
to_ws = to_wb.sheet_by_index(0)

new_wb = copy(to_wb)
new_ws = new_wb.get_sheet(0)

row_num = to_ws.nrows
   
for j in range(len(list1)):
    for k in range(len(list1[j])):
        new_ws.write(row_num,k,list1[j][k])
    row_num += 1
        
new_wb.save("11.xls")
print("SAVE SUCCESS!!!")
'''
#------------------------------------------------------------------------------------------------
'''
import xlwt
import xlrd
from xlutils.copy import copy


wb = xlwt.Workbook()
ws = wb.add_sheet('destination')
ws.write(0, 0, "Header")
ws.write(0, 1, "CatalogNumber")
ws.write(0, 2, "PartNumber")
wb.save('destination.xls')



oldWb = xlrd.open_workbook('1.xls', formatting_info=True)
print(oldWb)             #<xlrd.book.Book object at 0x000000000315C940>

newWb = copy(oldWb)
print(newWb)                #<xlwt.Workbook.Workbook object at 0x000000000315F470>

newWs = newWb.get_sheet(0)
newWs.write(1, 0, "value1")
newWs.write(1, 1, "value2")
newWs.write(1, 2, "value3")
print("write new values ok")

newWb.save('1.xls');
print("save with same name ok")
'''
#------------------------------------------------------------------------------------------------
'''
f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")
l = [f.read().split()]

boy = []
girl = []
num = 1
boy_file = "boy_{0}.txt".format(num)
girl_file = "girl_{0}.txt".format(num)


for i in range(len(l[0])):
    list1 = l[0][i]
#    print(list1)
#    print('-'*50)
    
    if list1[:3] == '小甲鱼':
        boy.append(list1.split('：')[1])
    
    if list1[:3] == '小客服':
        girl.append(list1.split('：')[1])


    if list1[:3] == '===':
        b = open(boy_file,"w")
        b.write("\n".join(boy))
        b.close()
        print("boy_file saved")
        
        g = open(girl_file,"w")
        g.write("\n".join(girl))
        g.close()
        print("girl_file saved")
      
        boy = []
        girl = []
        list1 = []
        num += 1
        boy_file = "boy_{0}.txt".format(num)
        girl_file = "girl_{0}.txt".format(num)


b = open(boy_file,"w")
b.write("\n".join(boy))
b.close()
print("last boy_file saved")

g = open(girl_file,"w")
g.write("\n".join(girl))
g.close()
print("last girl_file saved")

print('byebye!')
'''
#------------------------------------------------------------------------------------------------
'''
f = open("D:\\小鸡理财\\OneDrive\\python\\111.txt")

boy = []
girl = []
num = 1

for i in f:
    if i[:3] == '小甲鱼':
        boy.append(i.split('：')[1])
    
    if i[:3] == '小客服':
        girl.append(i.split('：')[1])


    if i[:3] == '===':
        boy_file = "boy_" + str(num) + ".txt"
        girl_file = "girl_" + str(num) + ".txt"
        
        b = open(boy_file,"w")
        b.writelines(boy)
        b.close()
        print("boy_file saved")
        
        g = open(girl_file,"w")
        g.writelines(girl)
        g.close()
        print("girl_file saved")
      
        boy = []
        girl = []
        num += 1


boy_file = "boy_" + str(num) + ".txt"
girl_file = "girl_" + str(num) + ".txt"
        
b = open(boy_file,"w")
b.writelines(boy)
b.close()
print("last boy_file saved")

g = open(girl_file,"w")
g.writelines(girl)
g.close()
print("last girl_file saved")
  
print('byebye!')
'''
#------------------------------------------------------------------------------------------------
'''
try:
    1/0
except ZeroDivisionError as reason:
    print('you are wrong because ' + str(reason))
except OSError:
    print('操作系统错误')
finally:
    raise ZeroDivisionError('除数为零的异常') x is {self.p.x},
'''
#------------------------------------------------------------------------------------------------
'''
class Person():
    def __init__(self):
        pass      
    def printx(self,x):
        print('father\'x is: ',x)
        
        
class Child():
    def __init__(self,x,y):
        self.x = Person().printx(x)
        self.y = y
        
    def printy(self):
        print(f'y is {self.y}')


a1 = Child(10,5)
print('-'*50)
a1.printy()
'''
#------------------------------------------------------------------------------------------------
'''
class Person():
    def __init__(self):
        print('__init__')      
    def printx(self,x):
        print('father\'x is: ',x)
        
p1 = Person()
p1.printx(5)
'''
#------------------------------------------------------------------------------------------------
'''
class CC():
    def setXY(self,x,y):
        self.x = x
        self.y = y
        print(self.x,self.y)

c1 = CC()
c1.setXY(11,99)

del CC
c1.setXY(11,99)
c2 = CC
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
x = np.empty((3,2,1), dtype =  np.int)  
print(x)
print(x.ndim)
'''
#------------------------------------------------------------------------------------------------
'''
# 从列表中获得迭代器  
import numpy as np 
list = range(5) 
it = iter(list)  
# 使用迭代器创建 ndarray 
x = np.fromiter([0, 1, 2, 3, 4], dtype =  float)  
print(x)

import numpy as np
l = list(range(5))


x = np.fromiter(l,dtype = float)
print(x)
'''
#------------------------------------------------------------------------------------------------
'''
class A(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)

a1 = A('abc')
print(a1)
'''
#------------------------------------------------------------------------------------------------
'''
class A:
    def __new__(cls):
        return 1
    def __init__(self):
        print('__init__ is running...')

class B(A):
    def __new__(cls,b):
        b = b*10
        return A.__new__(cls)


a1 = A()
print(a1)


b1 = B(1)
print(b1)
'''
#------------------------------------------------------------------------------------------------
'''
class Word(str):
    def __eq__(self,other):
        return len(self) == len(other)
    
a1 = Word('a')
b1 = Word('b')

print(a1==b1)
'''
#------------------------------------------------------------------------------------------------
'''
class Word(str):
    ''单词类，按照单词长度来定义比较行为''

    def __new__(cls, word):
        # 注意，我们只能使用 __new__ ，因为str是不可变类型
        # 所以我们必须提前初始化它（在实例创建时）
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]
            # Word现在包含第一个空格前的所有字母
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) < len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)


a1 = Word('abc')
a2 = Word('abcd')

print(a1 > a2)
print(len('abc') < len('abcd'))
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print('我们的数组是：'  )
print(x )
print('\n') 
rows = np.array([[3,3],[0,1],[1,1]]) 
cols = np.array([[0,2],[1,1],[0,0]]) 
y = x[rows,cols]  
print([rows,cols])
print('这个数组的每个角处的元素是：'  )
print( y)
'''
#------------------------------------------------------------------------------------------------
'''
class Person():
    def printx(self,x):
        print('father\'x is: ',x)


         
class Child(Person):
    def __init__(self,x,y):
        self.y = y
    def printy(self):
        Person.printx(x)      #！与上面的区别
        print(f'y is {self.y}')

a1 = Child(10,5)      #--->  father'x is:  10
a1.printy()      #--->  y is 5
'''
#------------------------------------------------------------------------------------------------
'''
y = int(input('give a year:'))

if (y%4==0 and y%100 != 0) or ( y%400 == 0):
    print('闰年')
else:
    print('no')
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print(  '我们的数组是：' ) 
print( x )
print(  '\n'  )


# 切片
z = x[1:4,1:3]  
print(  '切片之后，我们的数组变为：' ) 
print( z )
print(  '\n'  )
# 对列使用高级索引 
y = x[1:4,[1,2]] 
print(  '对列使用高级索引来切片：' ) 
print( y)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 

print(x[x>5])
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  

print(  '第一个数组：' ) 
print( a )
print(  '\n' ) 
print(  '第二个数组：')  
print( b )
print(  '\n'  )
print(  '第一个数组加第二个数组：' )
print(b-a)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
a = np.arange(0,60,5) 
a = a.reshape(4,3)  
print(  '原始数组是：' ) 
print( a )
print(  '\n'  )
print(  '修改后的数组是：')  
for x in np.nditer(a):  
    print(x,end = ',')
print()
for y in np.nditer(a, flags =  ['external_loop'], order ='F'):
    print(y)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print(  '原始数组是：')  
print( a )
print(  '\n'  )
print(  '修改后的数组是：')  
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):  
    print( x,)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
a = np.arange(0,60,5).reshape(4,3)

b = np.array([1,  2,  3])  

print(  '修改后的数组是：' ) 
for x,y in np.nditer([a,b]):  
    print  (x,':',y,end='||')
'''
#------------------------------------------------------------------------------------------------
'''
X = np.reshape(np.arange(24), (2, 3, 4))
print(X)

print('-'*50)

print(X[:,:,0])
print(X.shape)
'''
#------------------------------------------------------------------------------------------------
'''
for x in range(1,101):
    m = lambda x: x if x % 2 == 1 else ','
    print(m(x),end = '')



#m = lambda i: i if i % 2 == 1 else continue
'''
#------------------------------------------------------------------------------------------------
'''
x = 7
i = 1
flag = 0
	
while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
        i += 1
    
if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
'''
#------------------------------------------------------------------------------------------------
'''
z = 0
list1 = []

for x in range(4):
    for y in range(4):
        if (x + y) >=2:
            z = 8-(x+y)
            list1.append((x,y,z))
            
print(list1)
'''
#------------------------------------------------------------------------------------------------
'''
print('red\tyellow\tblue')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)
'''
#------------------------------------------------------------------------------------------------
'''
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)
'''
#------------------------------------------------------------------------------------------------
'''
# 创建了三维的 ndarray
import numpy as np
a = np.arange(8).reshape(2,2,2)

print( '原数组：')
print( a)
print( '\n')
# 将轴 2 滚动到轴 0(宽度到深度)



print( '调用 rollaxis 函数：')
print( np.swapaxes(a,2,0))
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])  

# 对 y 广播 x
b = np.broadcast(x,y)  
# 它拥有 iterator 属性，基于自身组件的迭代器元组

print( '对 y 广播 x：')
r,c = b.iters
print( r.next(), c.next())
print( r.next(), c.next())
print ('\n'  )
# shape 属性返回广播对象的形状


print( '广播对象的形状：')
print( b.shape)
print( '\n'  )
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x,y)
c = np.empty(b.shape)

print( '手动使用 broadcast 将 x 与 y 相加：')
print (c.shape)
print( '\n'  )
c.flat = [u + v for (u,v) in b]

print( '调用 flat 函数：')
print( c)
print ('\n'  )
# 获得了和 NumPy 内建的广播支持相同的结果

print( 'x 与 y 的和：')
print( x + y)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np  
x = np.arange(9).reshape(1,3,3)

print( '数组 x：')
print( x)
print( '\n'  )
y = np.squeeze(x)

print( '数组 y：')
print( y)
print( '\n'  )

print( '数组 x 和 y 的形状：')
print( x.shape, y.shape)
'''
#------------------------------------------------------------------------------------------------
'''
list1 = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

#member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

add = [88,90,85,90,88]

member = []

for i in range(len(list1)):
    member.append(list1[i])
    member.append(add[i])
    
for j in member:
    print(j)
'''
#------------------------------------------------------------------------------------------------
'''
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2
'''
#------------------------------------------------------------------------------------------------
'''
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list1)

list2 = []
for x in range(10):
    for y in range(10):
        if x%2==0 and y%2!=0:
            list2.append((x, y))
print(list2)            
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])

print( '第一个数组：')
print( a)
print( '\n' ) 

print( '未传递 Axis 参数。 在插入之前输入数组会被展开。')
print( np.insert(a,3,[11,12]))
print( '\n'  )
print( '传递了 Axis 参数。 会广播值数组来配输入数组。')

print( '沿轴 0 广播：')
print( np.insert(a,1,[11],axis = 0))
print( '\n' ) 

print( '沿轴 1 广播：')
print( np.insert(a,1,11,axis = 1))
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
a = np.arange(8)

print( '第一个数组：')
print( a)
print( '\n'  )

print( '将数组分为三个大小相等的子数组：')
b = np.split(a,4)
print( b)
print( '\n' ) 

print( '将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print( b)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
a = np.array([[1,2],[3,4]])

print( '第一个数组：')
print( a)
print( '\n'  )

print( '未传递 Axis 参数。 在插入之前输入数组会被展开。')
print( np.insert(a,3,[11,12]))
print( '\n'  )
print( '传递了 Axis 参数。 会广播值数组来配输入数组。')

print( '沿轴 0 广播：')
print( np.insert(a,1,[11],axis = 0))
print( '\n'  )

print( '沿轴 1 广播：')
print( np.insert(a,1,11,axis = 1))
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
a = np.array([5,2,6,2,7,5,6,8,2,9])

print( '第一个数组：')
print( a)
print( '\n'  )

print( '第一个数组的去重值：')
u = np.unique(a)
print( u)
print( '\n'  )

print( '去重数组的索引数组：')
u,indices = np.unique(a, return_index = True)
print( indices)
print( '\n'  )

print( '我们可以看到每个和原数组下标对应的数值：')
print (a)
print( '\n'  )

print( '去重数组的下标：')
u,indices = np.unique(a,return_inverse = True)
print( u)
print ('\n')

print( '下标为：')
print( indices)
print( '\n'  )

print( '使用下标重构原数组：')
print( u[indices])
print( '\n'  )

print( '返回去重元素的重复数量：')
u,indices = np.unique(a,return_counts = True)
print( u)
print( indices)
'''
#------------------------------------------------------------------------------------------------
'''
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0) :
    passwd = input("您输入的密码为空（或空格），请重新输入：")

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0

# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break
    
# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break    

# 打印结果
while 1 :
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1 :
        print("低")
    elif flag_len == 2 or flag_con == 2 :
        print("中")
    else :
        print("高")
        print("请继续保持")
        break

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位'")
    break
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print(  '我们的数组是：' ) 
print( a )
print(  '\n'  )
print ( '调用 amin() 函数：'  )
print( np.ptp(a)  )
print(  '\n'  )
print(  '再次调用 amin() 函数：'  )
print( np.ptp(a,axis = 0)  )
print( np.ptp(a,axis = 1)  )
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y = x**2+5
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,'m') 
plt.show()
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
import matplotlib.pyplot as plt 

# 计算正弦和余弦曲线上的点的 x 和 y 坐标 
x = np.arange(0,  3  * np.pi,  0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  

# 建立 subplot 网格，高为 2，宽为 1  

# 激活第一个 subplot
plt.subplot(2,  1,  1)  
# 绘制第一个图像 
plt.plot(x, y_sin) 
plt.title('Sine')  

# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2) 
# 绘制第二个图像
plt.plot(x, y_cos) 
plt.title('Cosine')  

# 展示图像
plt.show()
'''
#------------------------------------------------------------------------------------------------
'''
from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 

plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 
a = np.array([1,2,3,4,5]) 
np.save('outfile',a)
b = np.load('outfile.npy')
print(b)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np 

a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt')  
print(b)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)

df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
#print(df)

#print(df.head())
#print("--------------" * 10)

#print('*'*50)
#print(range(len(df)))
#print(df.tail(0))
#print('*'*50)

for i in range(len(df)):
    print(df.tail(i+1))
    print('-'*10)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[0:2,0:2])
print('-'*50)
print(df)
'''
#------------------------------------------------------------------------------------------------
'''
def gcd(x,y):
    if x % y == 0:
        return y
    else:
        while (x % y):
            x , y = y , x % y
        return y

a = gcd(147,7)
print(a)
'''
#------------------------------------------------------------------------------------------------
'''
def bin1(x):
    m = '1'
    if x == 0:
        return 0
    while (x // 2 != 0):
        m += str(x % 2)
        x = x // 2
        
    return m


a1 = bin1(0)
print(a1,'B')
'''
#------------------------------------------------------------------------------------------------
'''
def Dec2Bin(dec):
    temp = []
    result = ''
    
    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())
    
    return result

print(Dec2Bin(62))
#------------------------------------------------
def bin1(x):
    m = ''
#    if x == 0:
#        return 0
    while x:
        m += str(x % 2)
        x = x // 2
        
    return m

print(bin1(62))

'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(10),index = ['a','b','c','d','e','f','g','h','i','j'])

print(s)
print('-'*10)

print(s.axes)
print('-'*10)

print(s.empty)
print('-'*10)

print(s.ndim)
print('-'*10)

print(s.values)
print('-'*10)

print(s.head(2))
print('-'*10)

print(s.tail(2))
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
import pandas as pd

data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack'],
        'Age':[25,26,25,23,30,29,23],
        'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]
        }

df = pd.DataFrame(data)

print(df[1])
print('-'*10)

print(df.T)
print('-'*10)

print(df)
print('-'*10)

print(df.axes)
print('-'*10)

print(df.dtypes)
print('-'*10)

print(df.empty)
print('-'*10)

print(df.ndim)
print('-'*10)

print(df.shape)
print('-'*10)

print(df.size)
print('-'*10)

print(df.values)
print('-'*10)

print(df.head(2))
print('-'*10)

print(df.tail(2))
print('-'*10)
'''
#------------------------------------------------------------------------------------------------
'''
def Hui(x):
    for i in range(len(x)):
        if x[i] == x[(len(x)-1)-i]:
            continue
        else:
            return 'not huiwenlian'
    return 'huiwenlian111'


str1 =input('give a string:')
print(Hui(str1))
'''
#------------------------------------------------------------------------------------------------
'''
zimu = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shuzi = '0123456789'
kongge = ' '

z = 0
s = 0
k = 0
q = 0

s1 = input('pass a string:')

for i in s1:
    if i in zimu:
        z +=1
    elif i in shuzi:
        s +=1
    elif i in kongge:
        k +=1  
    else:
        q += 1

print(f'zimu {z} , shuzi {s} , kongge {k} , qita {q} .')
'''
#------------------------------------------------------------------------------------------------
'''
car = 'Hi'

def fun1():
    global var
    var = 'Baby'
    return fun2(var)

def fun2(var):
    var += 'i love you'
    fun3(var)
    return var

def fun3(var):
    var = 'xiaojiy'
    
print(fun1())
print('-'*50)

def fun(var):
    var = 1314
    print(var)

var = 520
fun(var)

print(var)
'''
#------------------------------------------------------------------------------------------------
'''
def Hui(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return 'HuiWen'
    else:
        return 'NotHuiWen'
    
print(Hui('上海自来水来自海上'))
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1,7).reshape(3,2),
   index = pd.date_range('1/1/2019', periods=3),
   columns = ['A', 'B'])

print(df)

print('-'*10)

print (df.expanding(min_periods=2).mean())
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]
         }
df = pd.DataFrame(ipl_data)

print (df)

print (df.groupby('Year'))
print('-'*10)

print (df.groupby('Year').groups)
print('-'*10)

print (df.groupby(['Year','Team']).groups)
print('-'*10)

grouped = df.groupby('Year')

for name,group in grouped:
    print (name)
    print (group)
print('-'*10)

print (grouped.get_group(2014))
print('-'*10)

agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print (agg)
print('-'*20)

filter = df.groupby('Team').filter(lambda x: len(x) >= 3)
print (filter)
print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
def Fun1():
    x = 5
    def Fun2():
        nonlocal x
        x *= 5
        return x
    return Fun2

a = Fun1()

print(a)
print(a)
print(a)

print('-'*50)

print(a())
print(a())
print(a())
'''
#------------------------------------------------------------------------------------------------
'''
def funout():
    def funin():
        print('bingo!')
    return funin

funout()()   
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.read_csv("temp.csv")

print("type of df",type(df))
value=df.values
print("type of value:",type(value))
print("shape of value:",value.shape)
print(df)
print('-'*50)

df2 = pd.read_csv("temp.csv")
print(df2.ix[:,1:3])
'''
#------------------------------------------------------------------------------------------------
'''
def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x,y-1)

power(3,2)
'''
#------------------------------------------------------------------------------------------------
'''
#求最大公约数的递归函数 
def gcd1(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)
'''
#------------------------------------------------------------------------------------------------
'''
#十进制转二进制的递归函数
def bin2(x):
    m = ''

    if x//2 <2:
        return m + str(x % 2) 
    else:
        return m + str(bin(x // 2))
'''
#------------------------------------------------------------------------------------------------
'''
def get_digits(n):
    l = []
    if n < 10:
        return [n]
    else:
        return [n%10]+get_digits(n//10)
'''
#------------------------------------------------------------------------------------------------
'''
def sui(n):
    if n == 1:
        return 10
    else:
        return sui(n-1)+2
sui(5)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(15).reshape(5,3),index = [0,2,4,1,3],columns=['col2','col1','col3'])

print(df)
print('-'*50)
    
sorted_df=df.sort_values(by='col1',ascending=False)
print(sorted_df)
'''
#------------------------------------------------------------------------------------------------
'''
print('
      |--- 欢迎进入通讯录程序 ---|
      |--- 1：查询联系人资料 ---|
      |--- 2：插入新的联系人 ---|
      |--- 3：删除已有联系人 ---|
      |--- 4：退出通讯录程序 ---|
      ')

txl = {}

def one():
    name = input('请输入联系人姓名：')
    if name in txl:
        print(name,':',txl.get(name))
        give_code()
    else:
        print('查无此人')
        give_code()

def two():
    name = input('请输入联系人姓名：')
    if name in txl:
        print('输入的姓名在通讯录中已存在 --->>  ',name,':',txl.get(name)) 
        change = input('是否修改用户资料（YES/NO）：')
        if change == 'YES':
            number = input('请输入用户联系电话：')
            txl[name] = number
            print('修改成功！')
            give_code()
        else:
            give_code()         
    else:
        number = input('请输入用户联系电话：')
        txl[name] = number
        print('插入成功！') 
        give_code()
        
def three():
    name = input('请输入联系人姓名：')
    if name in txl:
        print('确认删除这条记录吗？ --->>  ',name,':',txl.get(name)) 
        change = input('确认（YES/NO）：')
        if change == 'YES':
            del txl[name]
            print('删除成功！')
            give_code()
        else:
            print('取消删除！')
            give_code()
    else:
        print('查无此人') 
        give_code()

def four():
    print('|--- 感谢使用通讯录程序 ---|')


def give_code():  
    code = input('请输入相关的指令代码：')
    if code == '1':
        one()
    elif code == '2':
        two()
    elif code == '3':
        three()
    elif code == '4':
        four()
    else:
        print('指令输入错误!!!')


give_code()
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t', 'Alber@t'])

print(s)
print('-'*50)

print (s.str.cat(sep=' <=> '))
print('-'*50)

print (s.str.get_dummies())
print('-'*50)

print (s.str.contains(' '))
print('-'*50)

print (s.str.replace('@','$'))
print('-'*50)

print (s.str.repeat(2))
print('-'*50)

print (s.str.count('m'))
print('-'*50)

print (s.str.findall('i'))
print('-'*50)

print (s.str.swapcase())
print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
import numpy as np
import pandas as pd

data = {'Name':['Tom','James','Ricky'],
        'Age':[25,26,25],
        'Rating':[4.23,3.24,3.98]
        }

df = pd.DataFrame(data)

print(df)
print('-'*50)

print (df['Age'].pct_change())      #想应用到行上，那么可使用axis = 1参数
print('-'*50)

print (df['Age'].corr(df['Rating']))
print('-'*50)

print (df.corr())
print('-'*50)

print (df['Age'].rank(method = 'min'))
print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(15).reshape(5,3),index = ['a','b','c','d','e'],columns = ['col1','col2','col3'])

print(df)
print('-'*50)

#print (df.rolling(window=3,min_periods=2).mean())
print('-'*50)

#print (df.rolling(window=3).mean())
print('-'*50)

#print (df.expanding(min_periods=3).mean())
print('-'*50)

#print (df['col1'].mean())
print('-'*50)

#print (df.ewm(com=1).mean())
#print('-'*50)

#print (df.ewm(com=10).mean())
#print('-'*50)

r = df.rolling(window=3,min_periods=1)

print (r[['col1','col2']].aggregate([np.sum,np.mean]))
print('-'*50)

print (r.aggregate({'col1' : np.sum,'col2' : np.mean}))
print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(6).reshape(2,3),index = ['a','b'],columns = ['col1','col2','col3'])

df = df.reindex(['a','new','b'])

print(df)
print('-'*50)

print(df.isnull())
print('-'*50)

#print (df.notnull())
#print('-'*50)

print (df.fillna(0))
print('-'*50)

print (df.fillna(method='pad'))
print('-'*50)

print (df.fillna(method='backfill'))
print('-'*50)

print (df.dropna())
print('-'*50)

print (df.replace({3:333,5:555}))
print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'Team': ['Riders', 'Riders', 'Devils',],
         'Rank': [1, 2, 2,],
         'Year': [2014,2015,2014],
         'Points':[876,789,863]})

print(df)
print('-'*50)

print (df.groupby('Team'))
print('-'*50)

print (df.groupby(['Team','Year']).groups)
print('-'*50)

for name,group in df.groupby(['Team','Year']):
    print(name)
    print(group)
print('-'*50)

print (df.groupby('Team').get_group('Riders'))
print('-'*50)

print (df.groupby('Team')['Points'].agg([np.mean,np.sum,np.size]))
print('-'*50)
#
print (df.groupby('Team').agg(np.size))
print('-'*50)

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))
print('-'*50)

filter = df.groupby('Team').filter(lambda x:  len(x) >= 2)
print (filter)
'''
#------------------------------------------------------------------------------------------------
'''
str1 = input('>>>')

list1 = str1.split('\n')

print('-'*50)
print(list1)
print('-'*50)

#for i in list1:
#    print (i)
#    print('-'*50)
'''
#------------------------------------------------------------------------------------------------
'''
file_name = input('请输入文件名：')

f = open(file_name + '.txt','w')
list1 = []

content = input('请输入内容【单独输入“:w”保存退出】：')
new = content[:-2]  

f.write(new)

f.close()
'''
#------------------------------------------------------------------------------------------------
'''
str1 = input('请输入2个文件名，用“,”分隔：')

f1,f2 = str1.split(',')[0],str1.split(',')[1]

c1 = open(f1+'.txt','r')
c2 = open(f2+'.txt','r')
xu = 0
count = 0
l = []

len1 = len(c1.readlines())
c1.seek(0,0)

for i in range(len1):
    xu += 1 
    if c1.readline() == c2.readline():
        continue
    else:
        count += 1
        l.append(xu)
        
print('两个文件共有【',count,'】处不同：')
for i in l:
    print('第',i,'行不一样')
'''
#------------------------------------------------------------------------------------------------   
'''
file_name = input('请输入要打开的文件：')
#D:\\小鸡理财\\OneDrive\\python\\01.txt
row = int(input('请输入要显示的文件行数：'))

print('文件 ',file_name,' 的前',row,'行的内容如下：')

f= open(file_name)

for i in range(row):
    print(f.readline())

f.close()
'''
#------------------------------------------------------------------------------------------------  
'''
file_name = input('请输入要打开的文件：')
#D:\\小鸡理财\\OneDrive\\python\\01.txt
f= open(file_name)

row = input('请输入要显示的文件行数：').split(':')

def p1():
    print('文件 ',file_name,' 的第',row[0],'行到第',row[1],'行的内容如下：')
    gap = int(row[1])-int(row[0])
    for i in range(int(row[0])-1):
        f.readline()
    for j in range(gap):
        print(f.readline())
        
def p2():
    print('文件 ',file_name,' 开始到第',row[1],'行的内容如下：')
    for i in range(int(row[1])):
        print(f.readline())
   
def p3():
    print('文件 ',file_name,' 第',row[0],'行到结尾的内容如下：')
    for i in range(int(row[0])-1):
        f.readline()
    for j in range(20):
        print(f.readline())    


if row[0] == '':
    p2()
elif row[1] == '':
    p3()
else:
    p1()
'''
#------------------------------------------------------------------------------------------------ 
'''
file_name = input('请输入要打开的文件：')
#D:\\小鸡理财\\OneDrive\\python\\01.txt
f= open(file_name)
str_all = f.read()

str_old = input('请输入要替换的单词或字符：')
str_new = input('请输入新的单词或字符：')

c = str_all.count(str_old)

print('文件 ',file_name,' 中共有',c,'个【',str_old,'】\n'\
      '确定要把所有的替换为',str_new,'吗？\n'\
      )
choose = input('[YES/NO]:')

if choose == 'yes':
    str_all_new = str_all.replace(str_old,str_new)
    print(str_all_new)    
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd

left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print("========================================")
print (right)
print('-'*50)

#rs = pd.merge(left,right,on='id')
#print(rs)
print('-'*50)

#rs = pd.merge(left,right,on=['id','subject_id'])
#print(rs)
print('-'*50)

#rs = pd.merge(left, right, on='subject_id', how='left')         #same as how = 'right'
#print (rs)
print('-'*50)

rs = pd.merge(left, right, how='outer', on='subject_id')
print (rs)
print('-'*50)

rs = pd.merge(left, right, on='subject_id', how='inner')
print (rs)
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[0,1,2])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['e','b','c','d'],index=[1,2,3])
#df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

print (df1)
print("========================================")
print (df2)
print("========================================")
#print (df3)
#print('-'*50)

#rs = pd.concat([df1,df2])
#print(rs)
print('-'*50)


#rs = pd.concat([df1,df2],ignore_index=True,join='inner')
#print(rs)
print('-'*50)

#rs = pd.concat([df1,df2],axis=1)
#print(rs)
print('-'*50)

#rs = pd.concat([df1,df2],axis=1,join_axes = [df1.index])
#print(rs)
print('-'*50)

rs = df1.append([df2,df1],ignore_index=True)
print(rs)
print('-'*50)

s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
rs = df1.append(s1,ignore_index=True)
print(rs)
print('-'*50)

rs = pd.merge()
'''
#------------------------------------------------------------------------------------------------ 
'''
import os

dir_num = 0
zi = {}

for root, dirs, files in os.walk(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据'):
#    print(root)
#    print(dirs)
#    print(files)
#    print('-'*50)
    dir_num += len(dirs)
    for i in files:
        k = os.path.splitext(i)[1]
        if k in zi:
            zi[k] += 1
        else:
            zi[k] = 1

for key,value in zi.items():
    print('该文件夹下共有类型为【%s】的文件 %s 个' % (key,value))
print('该文件夹下共有类型为【文件夹】的文件 %s 个' % (dir_num))
'''
#------------------------------------------------------------------------------------------------ 
'''
import os

for root,dirs,files in os.walk(r'D:\小鸡理财\百度云同步盘\小鸡理财\每日数据'):
    os.chdir(root)
    
    for i in files:
        size = os.path.getsize(i)
        print('%s [ %s Bytes]' %(i,size))
'''
#------------------------------------------------------------------------------------------------ 
'''
import os

file_add = input('请输入待查找的初始目录：')
video = ['.mp4','.rmve','.avi']
video_list = []

for root,dirs,files in os.walk(file_add):
    for i in files:
        k = os.path.splitext(i)[1]
        if k in video:
            add = root + '\\' + i
            video_list.append(add)

#print(video_list)

f = open('video_list.txt','w')
for j in video_list:
    f.write(j)
    f.write('\n')
#f.writelines(video_list)
f.close()

#D:\VDownload
'''
#------------------------------------------------------------------------------------------------ 
'''
import os

all_files = os.listdir(os.curdir)
type_dict = dict()

print(all_files)
'''
#------------------------------------------------------------------------------------------------ 
'''
def futou(n):
    if n == 1:
        return 14000*1.2
    else:
        return futou(n-1)*1.2


a = int(input('enter years: '))

money = 0
 
for i in range(a):
    money += futou(i+1)

print(money)
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd
import numpy as np

df = pd.read_csv('01.csv')

print(df)
print('-'*50)

df1=pd.read_csv("01.csv",index_col=['S.No'])
print (df1)
print(df1.dtypes)
print('-'*50)

df2=pd.read_csv("01.csv",index_col=['S.No'],dtype = {'Salary':np.float64})
print (df2)
print(df2.dtypes)
print('-'*50)

df3=pd.read_csv("01.csv",names=['a','b','c','d','e'],header=0)
print (df3)
print('-'*50)

df4=pd.read_csv("01.csv", skiprows=2)
print (df4)
'''
#------------------------------------------------------------------------------------------------ 
'''
try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i,j)
except KeyboardInterrupt:
    print('out!')
    print('6')
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd
import numpy as np

#df = pd.DataFrame(np.random.rand(10,4),columns=list('ABCD'))
#print(df)

#df.plot()

#df.plot.bar()

#df.plot.bar(stacked=True)


#df.plot.barh()

#df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

#df.plot.hist(bins=50)
#df.hist(bins=20)
#df.plot.box()
#df.plot.area()
#df.plot.scatter(x='a', y='b')

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
df.plot.pie()
'''
#------------------------------------------------------------------------------------------------ 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
# -*- coding: utf-8 -*-

import pandas as pd

with pd.ExcelFile('01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'Sheet1')
    df2 = pd.read_excel(xlsx,'Sheet2')
    
print(df1.info())

df3 = pd.merge(df1,df2,how = 'left',on = '身份证')
df3.to_excel('用户画像数据_合并2.xlsx')

    
#----------------------
#df1 = pd.read_csv(r'D:\小鸡理财\OneDrive\01.csv',sep = '\\n',engine='python',encoding = 'utf-8')
#df2 = pd.read_csv(r'D:\小鸡理财\OneDrive\02.csv',sep = '\\n',engine='python',encoding = 'utf-8')

#df1.rename(columns={'身份证' : 'c1'},inplace = True)
#df2.rename(columns={'身份证' : 'c1'},inplace = True)            

#print(len(df1))

#df1['a'] = pd.Series(np.arange(len(df1)))
#df2['b'] = pd.Series(np.arange(len(df2)))

#df3 = pd.merge(df1,df2,how = 'left',on = '身份证')
#print(df3)
#df3.to_excel('000.xlsx')
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'total_bill':np.random.randint(10,size = 5),
                    'sex':np.random.choice(np.array(['male','female']),5),
                    'id':pd.Series(np.arange(5))
                    })
                    

print(df)
print('='*50)

#print(df.info())

print(df.tips[['id','sex']])
'''
#------------------------------------------------------------------------------------------------ 
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)
#print(data.shape)
#print('='*50)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#print(fig)
#print('='*50)
#print(axs)
#print('='*50)


axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()1投资标的
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd

with pd.ExcelFile('01.xlsx') as xlsx:
#    df1 = pd.read_excel(xlsx,'经典注册用户')
#    df2 = pd.read_excel(xlsx,'经典投资记录')
    df3 = pd.read_excel(xlsx,'存管注册用户')
    df4 = pd.read_excel(xlsx,'存管投资记录')
    
#print(df1.info())
print('---------------------------read_ok---------------------------')


#df5 = pd.merge(df1,df2,how = 'left',left_on = '用户名',right_on = '投资用户')
df5 = pd.merge(df3,df4,how = 'left',left_on = '手机号码',right_on = '手机号')
#df7 = pd.merge(df6,df4,how = 'left',left_on = '用户名',right_on = '投资用户')
print('---------------------------merge_ok---------------------------')

with pd.ExcelWriter('001.xlsx') as writer:
    df5.to_excel(writer,sheet_name = 'jingdian',index = False)
#    df7.to_excel(writer,sheet_name = 'cunguan',index = False)
    
#df7.to_excel('001.xlsx')
print('---------------------------write_ok---------------------------')
'''
#------------------------------------------------------------------------------------------------ 
'''
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 6, 9], '-r')

plt.plot([1, 2, 3], [2, 4, 9], ':g') 

plt.show()
'''
#------------------------------------------------------------------------------------------------ 
'''
a = dict(a=1,b=2,c=3)

try:
    print(a['a'])
except KeyError as reason:
    print(': %s' %reason)
else:
    print('else')
finally:
    print('end')
'''
#------------------------------------------------------------------------------------------------ 
'''
class Person():
    def __init__(self,name):
        self.name = name
        
        print(self.name)

a = Person('xiaojiayu')
'''
#------------------------------------------------------------------------------------------------ 
'''
class Rectangle():
    def __init__(self):
        self.length = 5
        self.width = 4
        
    def getRect(self):
        print('这个矩形的长是： %s ，宽是： %s ' %(self.length,self.width))
        
    def setRect(self):
        print('请输入矩形的长和宽...')
        self.length = float(input('长： '))
        self.width = float(input('宽： '))        
        
    def getArea(self):
        area = self.length * self.width
        print('面积是：',area)


rect = Rectangle()
rect.getRect()

rect.setRect()

rect.getRect()

rect.getArea()
'''
#------------------------------------------------------------------------------------------------ 
'''
import os
os.chdir('D:\VDownload\新建文件夹\我的解析任务1804241345\合并')

for root,dirs,files in os.walk('D:\VDownload\新建文件夹\我的解析任务1804241345\合并'):
    for i in files:
        l = i.split(' ',1)[1].strip()
        print(l)

        os.rename(i,l)
'''
#------------------------------------------------------------------------------------------------ 
'''
class ticket:
    def __init__(self,adult,child,day_type):
        self.adult = int(adult)
        self.child = int(child)
        self.day = day_type
        
    def money(self):
        x = 'non_week'
        money = self.adult * 100 + self.child * 50
        if self.day == x:
            return money
        else:
            return money * 1.2
        
adult = input('adult:')
child = input('child:')        
day_type = input('day_type:')

a = ticket(adult,child,day_type)

print(a.money())
'''
#------------------------------------------------------------------------------------------------ 
'''
import random as r

legal_x = [0,100]
legal_y = [0,100]

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        
        #初始位置        
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])
        
    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_x = self.x + r.choice([1,-1,2,-2])
        new_y = self.y + r.choice([1,-1,2,-2])
        
        #检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x    

        #检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
            
        #体力消耗
        self.power -= 1
        
        #返回移动后的新位置
        return (self.x,self.y)
    
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100
            
class Fish:
    def __init__(self):
        #初始位置      
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])    

    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        
        #检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x    

        #检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        #返回移动后的新位置
        return (self.x,self.y)

turtle = Turtle()
fish = []
count = 1

for i in range(100):
    new_fish = Fish()
    fish.append(new_fish)
    
while True:
    if not len(fish):
        print('鱼儿都吃完了，游戏结束')
        break
    if not turtle.power:
        print('乌龟体力耗尽，挂掉了！')
        break
        
    pos = turtle.move()
    
    #在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    #这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    
    for each_fish in fish[:]:
        
        if each_fish.move() == pos:
            #鱼儿被吃掉了
            turtle.eat()
            
            fish.remove(each_fish)
            print('第 %s 条鱼儿被吃掉了...' %count)
            count += 1
'''
#------------------------------------------------------------------------------------------------ 
'''
import random as r

legal_x = [0,10]
legal_y = [0,10]

class Turtle_or_Fish:
    def __init__(self,turtle = False,fish = False):
        # 初始体力
        self.power = 100
        self.turtle = turtle
        self.fish = fish
        
        #初始位置        
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])
        
    def move(self):
        if self.turtle:
            #随机计算方向并移动到新的位置(x,y)
            new_x = self.x + r.choice([1,-1,2,-2])
            new_y = self.y + r.choice([1,-1,2,-2])
        else:
            #随机计算方向并移动到新的位置(x,y)
            new_x = self.x + r.choice([1,-1])
            new_y = self.y + r.choice([1,-1])            
                
        #检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x    

        #检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
            
        #体力消耗
        self.power -= 1
        
        #返回移动后的新位置
        return (self.x,self.y)
    
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100
            

turtle = Turtle_or_Fish(turtle = True)
fish = []
count = 1

for i in range(10):
    new_fish = Turtle_or_Fish(fish = True)
    fish.append(new_fish)
    
while True:
#    print(len(fish))
    if not len(fish):
        print('鱼儿都吃完了，游戏结束')
        break
    if not turtle.power:
        print('乌龟体力耗尽，挂掉了！')
        break
        
    pos = turtle.move()
    
    #在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    #这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    
    for each_fish in fish[:]:
        
        if each_fish.move() == pos:
            #鱼儿被吃掉了
            turtle.eat()
            
            fish.remove(each_fish)
            print('第 %s 条鱼儿被吃掉了...' %count)
            count += 1
'''
#------------------------------------------------------------------------------------------------ 
'''
a = 0
a = 1
class f:
#    global a
    a = 2
    def f1(self):
        print(a+5)
        
ff = f()
ff.f1()


b = 0

class l:
    def __init__(self,b):
        self.b = b
    
    def l1(self):
        print(self.b + 5)
        
ll = l(10)
ll.l1()
'''
#------------------------------------------------------------------------------------------------
'''
import matplotlib.pyplot as plt
import numpy as np

labels1 = ['Man', 'Women']

data1 = [18278,16852]

plt.pie(data1, labels=labels1, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

plt.show()
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np


# 数据集路径
df = pd.read_csv('survey.csv')

# 去掉可能存在的空格
df['Gender'] = df['Gender'].str.replace(' ','')
# 转换为小写
df['Gender'] = df['Gender'].str.lower()
#数据清洗
df['Gender'] = df['Gender'].replace({'m':'male','f':'female'})
#数据值合并
df = df[(df['Gender'] == 'male') | (df['Gender'] == 'female')]

table = pd.pivot_table(df, values=['Age'], index=['Country'],columns=['Gender'], aggfunc=np.size)

table.to_excel('666.xlsx')
'''
#------------------------------------------------------------------------------------------------
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','MN','ON'],
                        'City' : ['Toronto','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
                        'Sales' : [13,6,16,8,4,3,1]})
    
print(df)
print('='*50)

table = pd.pivot_table(df,values=['City'],index=['Province'],columns=['City'],aggfunc=np.size)

print(table)
print('='*50)

print(table.stack('City'))
'''
#------------------------------------------------------------------------------------------------
'''
import math

class Point():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Line(Point):
    def __init__(self,p1,p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x * self.x + self.y * self.y)
        
    def getLen(self):
        return self.len
    
p1 = Point(3,4)
p2 = Point(5,6)

line = Line(p1,p2)
print(line.getLen())        
'''
#------------------------------------------------------------------------------------------------  
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','$','ON'],
                        'City' : ['?','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
                        'Sales' : [13,6,16,8,np.NaN,3,1]})

print(df)
print('='*50)

df1 = df.replace({'$':1,'?':1})
print(df1)
print('='*50)

df2 = df.replace({0:'?'},np.nan)
print(df2)
print('='*50)
'''
#------------------------------------------------------------------------------------------------  
'''
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 100, normed=1, facecolor='g', alpha=0.8)


plt.xlabel('Smarts',fontsize=14, color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(20, .02, r'$\mu=100,\ \sigma=15,\bigcap $')
plt.axis([0, 160, 0, 0.03])
plt.grid(True)
plt.show()
'''
#------------------------------------------------------------------------------------------------ 
'''
import matplotlib.pyplot as plt
import numpy as np

#需要展现的数据
data = np.arange(100, 201)

#设定x，y轴的最大、最小值
#plt.axis([0,100,50,300])

#另一种设定x，y轴的最大、最小值的方式
plt.xlim(0,100)
plt.ylim(50,300)

#
plt.xticks(np.linspace(0,100,5,endpoint=True))
plt.yticks(np.linspace(50,300,5,endpoint=True))

plt.title('Easy as 1, 2, 3')      #补充，设定标题

#设定x，y轴标签,标签字体，颜色
plt.xlabel('x numbers',fontsize=14, color='red')      
plt.ylabel('y numbers',fontsize=14, color='red')

#在图表内增加公式
plt.text(20, 250, r'$\mu=100,\ \sigma=15,\bigcap $')

#设置背景网格线
plt.grid(True)

plt.plot(data,color="blue", linewidth=1.0, linestyle="-")

plt.show()
'''
#------------------------------------------------------------------------------------------------ 
'''
# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,5,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()
'''
#------------------------------------------------------------------------------------------------ 
'''
# 载入绘图模块
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 加载数据
iris_data = sns.load_dataset('iris')

# 散点图
#sns.lmplot(x='petal_length', y='petal_width', hue='species', data=iris_data)

#查看两个维度数据之间的关系
#sns.PairGrid(data=iris_data).map(plt.scatter)
#区分种类
#sns.PairGrid(data=iris_data, hue='species').map(plt.scatter)

#查看两个维度数据之间的关系
#sns.JointGrid(data=iris_data, x='sepal_length', y='sepal_width').plot(sns.regplot, sns.distplot)

#绘制单变量的核密度估计图
#sns.kdeplot(data=iris_data["sepal_length"])
#sns.kdeplot(data=iris_data["sepal_length"], shade=True, color='y')

#绘制二元变量的核密度估计图
#sns.kdeplot(data=iris_data["sepal_length"], data2=iris_data["sepal_width"], shade=True)

#绘制热力图
#matrix_data = np.random.rand(10, 10)
#sns.heatmap(data=matrix_data)

#层次聚类热图
iris_data.pop("species")  #去掉了花的类别列
sns.clustermap(iris_data)

plt.show()
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd

data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack'],
        'Age':[25,26,25,23,30,29,23],
        'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8]
        }

df = pd.DataFrame(data)

print(df)
print('='*50)

print(df['Age'].value_counts())
print('='*50)
    
print(df.count())
print('='*50)

print(df.dtypes)
print('='*50)


df['Age'] = df['Age'].astype('float64')
print(df.dtypes)
print('='*50)

print(df.index)
print(df.columns)
print('='*50)

x = df.loc[df['Name'].isin(['James','Tom']),['Name','Age']]
print(x)
'''
#------------------------------------------------------------------------------------------------ 
'''
import pandas as pd
import numpy as np

with pd.ExcelFile('01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'名单')
    df2 = pd.read_excel(xlsx,'注册')
    df3 = pd.read_excel(xlsx,'投资')
    
print('---------------------------read_ok---------------------------')

df2['add'] = 1

#print(df2)
#print(df2.columns)
#print(df3.columns)

df4 = pd.merge(df2,df3,how = 'left',on = '下线手机号')
df5 = pd.merge(df1,df4,how = 'left',left_on = '上线手机号',right_on = '上线邀请人')
df6 = df5[(df5['下线邀请渠道'] != '业务邀请')]

#print('select ok')
#print(df6)

#print(df5.head(20))
#print(df5.shape)
#print(df4['下线邀请渠道'].drop_duplicates())

gp = df6.groupby(['上线手机号','上线真实姓名'])
result = gp.agg({'add':np.sum,'标记':np.sum}).sort_values(by = ['add','标记'],ascending=False)
#print(result)

print('---------------------------merge_ok---------------------------')

with pd.ExcelWriter('001.xlsx') as writer:
    result.to_excel(writer,sheet_name = 'result')

    
print('---------------------------write_ok---------------------------')
'''
#------------------------------------------------------------------------------------------------ 
'''
import numpy as np
import pandas as pd


rng = pd.date_range('1/1/2018', periods=5, freq='M')
print()
print(rng)

ts = pd.Series(np.random.randn(len(rng)), index=rng)
print('\nts')
print (ts)

ps = ts.to_period()
print('\nps')
print(ps)

print('\nps')
print(ps.to_timestamp())
print('='*100)


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

print(df)
print()

print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])
print()

print(df[df['animal'].isin(['cat', 'dog'])])
print()

print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
print()

df2 = df['priority'].map({'yes': True, 'no': False})
print(df2)
print()
print('='*100)


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})
print(df)
print()

#数据列拆分
temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']
print(temp)
print()

#删除坏数据加入整理好的数据
df = df.drop('From_To', axis=1)
df = df.join(temp)
print(df)
print()

#去除多余字符
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
print(df)
print()

#格式规范
"""
在 RecentDelays 中记录的方式为列表类型，由于其长度不一，这会为后期数据分析造成很大麻烦。这里将 RecentDelays 的列表拆开，取出列表中的相同位置元素作为一列，若为空值即用 NaN 代替
"""
delays = df['RecentDelays'].apply(pd.Series)
print('delays:')
print(delays)
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
print('delays:')
print(delays)
df = df.drop('RecentDelays', axis=1).join(delays)
print('df:')
print(df)
print()
'''
#------------------------------------------------------------------------------------------------ 
'''
df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','$','ON'],
                        'City' : ['?','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
                        'Sales' : [13,6,16,8,np.NaN,3,1]})
print(df.corr())


print(df.index)

df2 = df.set_index('City')
print(df2)

df3 = df2.reset_index()
print(df3)

s = pd.Series(np.range(7))
print(s)
print()

df4 = pd.concat([df,s],axis = 1)
print(df4)
print()

print('idxmax:',df4['Sales'].idxmax())
'''
#------------------------------------------------------------------------------------------------ 
'''
data = {'Name':['Tom','James','Ricky'],
        'Age':[25,26,25],
        'Rating':[4.23,3.24,3.98]
        }

df = pd.DataFrame(data)


print(df)
print('_'*50)

max_index = df[['Age','Rating']].idxmax()
print(max_index)

min_index = df[['Age','Rating']].idxmin()
print(min_index)


'''
#------------------------------------------------------------------------------------------------ 
'''
df = pd.read_csv('country_additives.csv',encoding = 'gbk',names = ['country','point'])

print(df.info())
#print('='*50)
 
#print(df.dtypes)
#print('='*50)
 
df2 = df['country'].str.split(',',expand=True)
#print(df2.head())
#print('='*50)
 
df3 = pd.concat([df,df2],axis = 1)
#print(df3.head())
#print('='*50)
#print(df3.shape)
 
df4 = df3[['point',0]]
 
for i in range(1,14):
    df_temp = df3[['point',i]]
    df_temp = df_temp.rename(columns={i:0})
#    print(i,':df_temp:',df_temp.columns)
    df4 = df4.append(df_temp)
 
#print(df4.info())
'''
#------------------------------------------------------------------------------------------------ 
'''
df = pd.DataFrame({'date': pd.date_range('2015-01-01', freq='W',periods=5),'a': np.arange(5)},
    index=pd.MultiIndex.from_arrays([[1,2,3,4,5],pd.date_range('2015-01-01', freq='W',periods=5)],names=['v','d']))


date_sum = df.resample('M', on='date').sum()
print(date_sum)
print('='*50)

index_date_sum = df.resample('M', level='d').sum()
print(index_date_sum)
print('='*50)

print(df)
'''
#------------------------------------------------------------------------------------------------ 
'''
with pd.ExcelFile('01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'名单')
    df2 = pd.read_excel(xlsx,'注册')
    df3 = pd.read_excel(xlsx,'投资')
    
print('---------------------------read_ok---------------------------')

df4 = pd.merge(df2,df3,how = 'left',on = '下线手机号')
df5 = pd.merge(df1,df4,how = 'left',left_on = '上线手机号',right_on = '上线邀请人')
df6 = df5[(df5['下线邀请渠道'] != '业务邀请')]

gp = df6.groupby(['上线手机号','上线真实姓名'])
result = gp.agg({'注册标记':np.sum,'投资标记':np.sum}).sort_values(by = ['注册标记','投资标记'],ascending=False)

print('---------------------------merge_ok---------------------------')

with pd.ExcelWriter('001.xlsx') as writer:
    result.to_excel(writer,sheet_name = 'result')

    
print('---------------------------write_ok---------------------------')
'''
#------------------------------------------------------------------------------------------------ 
'''
sum_offset = pd.tseries.offsets.Week(2)

print(pd.date_range('1/1/2018', periods=5, freq=sum_offset))
#ts = pd.Series(np.arange(10), index=rng)
#
#print(ts.index)
#print('-'*50)

#print(ts[ts.index[2]])
#print('-'*50)

#print(ts[::2])
#print('-'*50)

#print(ts.index.is_unique)
#print('-'*50)

#print(ts['2018/01/13'])
#print('-'*50)

#print(ts['2018-2'])
#print('-'*50)

#print(ts.truncate(before='2018-3-1'))
#print('-'*50)
#
#print(ts.truncate(after='2018-3-1'))
#print('-'*50)

#print(ts.shift(1))
#print('-'*50)
#
#print(ts.shift(-1))
#print('-'*50)
'''
#------------------------------------------------------------------------------------------------ 
'''
df = pd.DataFrame(np.arange(5),
                 index=pd.date_range('20170101', periods=5),
                 columns=['S1'])

print(df.head())
print('-'*50)

#print(df.resample('M', level=0).sum())
#print('-'*50)

print(df['S1'].diff(2))
print('-'*50)
#
#print(df.groupby(lambda x: x.month).sum())
#print('-'*50)
#
#print(df.groupby(lambda x: x.weekday).sum())
#print('-'*50)
'''
#------------------------------------------------------------------------------------------------ 
'''
with pd.ExcelFile('a1.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'原始数据')
    df2 = pd.read_excel(xlsx,'业务员')
    df3 = pd.read_excel(xlsx,'推广')
   
print('---------------------------read_ok---------------------------')

df2['mark_2'] = 1
df3['mark_3'] = 1

#print(df1.info())
#print(df2.info())
#print(df3.info())

df4 = pd.merge(df1,df2,how = 'left',left_on = '邀请人',right_on = '业务员')
df5 = pd.merge(df4,df3,how = 'left',left_on = '用户名',right_on = '推广渠道用户名')

print('---------------------------merge_ok---------------------------')

df5['mark_2'] = df5['mark_2'].fillna(df5['邀请渠道'])
df5['mark_2'] = df5['mark_2'].replace(1,'业务邀请')

df5['mark_3'] = df5['mark_3'].fillna(df5['mark_2'])
df5['mark_3'] = df5['mark_3'].replace(1,'自主注册')

print('---------------------------modify_ok---------------------------')

reslut = df5.rename(columns={'mark_3' : 'new_邀请渠道'})

print('---------------------------rename_ok---------------------------')

with pd.ExcelWriter('a1.xlsx') as writer:
    reslut.to_excel(writer,sheet_name = 'result')

    
print('---------------------------write_ok---------------------------')
'''
#------------------------------------------------------------------------------------------------ 
'''
a = np.zeros((5,5))
#
#print('a:',a)
#print('='*10)
##
##b = np.matrix(np.arange(10).reshape((5,2)))
##print('b:',b)
##print('='*10)
##
##for i in range(5):
##    print('i:',i)
##    c = b[:,0].A
##    print('c:',c)
##    print('='*10)  
##    d = np.nonzero(b[:,0].A == i)[0]
##    print('d:',d)
##    print('='*10)            
##    p = a[np.nonzero(b[:,0].A == i)[0]]
##    print(p)
##    print('='*10)
#
##e = np.arange(4,step = 2)
##print(a[e])
#
#for i in range(5):
#    a[:,i] = np.random.randint(10)
#    
#print('a:',a)
#print('='*10)
#
#
#f = np.array([[30,40,70],[80,20,10],[50,90,60]]) 
#print('f:',f)
#print(np.mean(f,axis = 0))


#df = pd.DataFrame(np.arange(12).reshape(3,4),
#                 index=pd.date_range('20170101', periods=3)
#                 )
#
#print(df)
#print(type(df))
#
#fo1 = pd.DataFrame.as_matrix(df)
#
#print(fo1)
#print(type(fo1))
#
#fo2 = df.as_matrix()
#
#print(fo2)
#print(type(fo2))
#
#fo3 = df.values
#
#print(fo3)
#print(type(fo3))
'''
#--------------------------------------------------------------------------------------
'''
#dir_add = r'D:\小鸡理财\百度云同步盘\小鸡理财\数据报告\VIP报告\vip'
#
#num = 0
#for root,dirs,files in os.walk(dir_add):
#    x = os.path.split(root)
#    print(x[1])
#    print(type(x[1]))
'''
#--------------------------------------------------------------------------------------
'''
#VIP数据
with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'名单')
    df2 = pd.read_excel(xlsx,'注册')
#    df3 = pd.read_excel(xlsx,'投资')
   
print('---------------------------read_ok---------------------------')

print(df1.shape)

df4 = pd.merge(df1,df2,how = 'left',left_on = '邀请人',right_on = '手机号码')
#df5 = pd.merge(df4,df3,how = 'left',on = '用户名')

print('---------------------------merge_ok---------------------------')

print(df4.shape)

if df1.shape[0] == df4.shape[0]:
    result = df4[df4['mark'].notnull()]
    
    print('begin to write!!!')
    result.to_csv('001.csv')
    print('---------------------------write_ok---------------------------') 
'''
#--------------------------------------------------------------------------------------
'''
with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'名单')
    df2 = pd.read_excel(xlsx,'注册')
    df3 = pd.read_excel(xlsx,'投资')

print(df1.shape)   
print('---------------------------read_ok---------------------------')

df4 = pd.merge(df2,df3,how = 'left',left_on = '下线',right_on = '手机号码')
#gp = df4.groupby(by = '上线').agg({'下线':np.size,'mark':np.sum})
df5 = pd.merge(df4,df1,how = 'inner',left_on = '上线',right_on = '手机号')
#df1 = df1.set_index('手机号')


#df1['下线注册数'] = gp['下线']
#df1['下线投资人数'] = gp['mark']

print('---------------------------merge_ok---------------------------')

print(df1.shape)

if True:   
    print('begin to write!!!')
    df5.to_csv('001.csv')
    print('---------------------------write_ok---------------------------') 
'''
#--------------------------------------------------------------------------------------
'''
with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
    df = pd.read_excel(xlsx,'名单')


for i in range(1,df.shape[1]):
    x = np.arange(5)
    y = df.iloc[:,i]
#    plt.ylim(0,100)
    
    group_labels = ['2018.01', '2018.02', '2018.03', '2018.04', '2018.05']
    
    plt.subplot(3, 2, i)
    
    plt.plot(y,label = y.name)
    
    plt.xticks(x, group_labels , rotation=0)
#    plt.legend(loc='upper right')
    plt.legend()
#    plt.grid() 
    
   
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题    

    
#plt.suptitle('当月新增下线人数', fontsize=26) 
plt.show()
'''
#--------------------------------------------------------------------------------------
'''
with pd.ExcelFile(r'D:\小鸡理财\OneDrive\python\01.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx,'名单')
    df2 = pd.read_excel(xlsx,'注册')
#    df3 = pd.read_excel(xlsx,'投资')

print(df1.shape)   
print('---------------------------read_ok---------------------------')

df4 = pd.merge(df1,df2,how = 'left',on = '用户名')
#gp = df4.groupby(by = '上线').agg({'下线':np.size,'mark':np.sum})
#df5 = pd.merge(df4,df1,how = 'inner',left_on = '上线',right_on = '手机号')
#df1 = df1.set_index('手机号')


#df1['下线注册数'] = gp['下线']
#df1['下线投资人数'] = gp['mark']

print('---------------------------merge_ok---------------------------')

#print(df1.shape)

if True:   
    print('begin to write!!!')
    df4.to_csv('001.csv')
    print('---------------------------write_ok---------------------------') 
'''
#--------------------------------------------------------------------------------------
'''
import os

dir_path = 'G:\wangwangduilidagong\汪汪队立大功 第四季'

os.chdir(dir_path)

for i in os.listdir('.'):
    s = i.split(' ',3)[3]
    os.rename(i,s)
    print ("重命名成功。")
'''
#--------------------------------------------------------------------------------------
'''
#df = pd.DataFrame({'Sp':['a','b','c','d','e','f'], 
#                   'Mt':['s1', 's1', 's2','s2','s2','s3'], 
#                   'Value':[1,2,3,4,5,6], 
#                   'Count':[3,2,5,10,10,6]})
#    
#print(df)
#print('='*50)
#
##df_max = df.sort_values(by = 'Count',ascending = False).drop_duplicates('Mt')
#
##print(df_max)
#
##print( df.groupby(['Mt'])['Count'].agg(max))
# 
##idx=df.groupby(['Mt'])
##for i in idx:
##    print(i)
##idx1 =  idx == df['Count']
##print idx1
## 
##df[idx1] ['Count'].transform(max)
#
#
#score = lambda x: (x - x.mean()) / x.std()*10
#print(df.groupby('Mt').transform(score) )


df = pd.DataFrame ({'a' : np.random.randn(6),
             'b' : ['foo', 'bar'] * 3,
             'c' : np.random.randn(6)})
 
def my_test(a, b):
    return a + b
 
df['Value'] = df.apply(lambda row: my_test(row['a'], row['c']), axis=1)
print( df)
'''
#--------------------------------------------------------------------------------------
'''
path = 'C:\\Users\\ye\\Downloads\\excel转csv\\'
os.chdir(path)

filenames = os.listdir(path)
dd = []


for i in filenames:
    dd.append(pd.read_csv(i,engine = 'python')) 

#另一种读取方法    
#for i in filenames:
#    f = open(i,'r')
##    res = pd.read_csv(f)
#    dd.append(pd.read_csv(f)) 

df = pd.concat(dd)

print(df.shape)

df.to_csv('002.csv',index = False)
print('ok')
'''
#--------------------------------------------------------------------------------------
'''
df = pd.DataFrame({'id':[i for i in range(1,6)],
                         'gender':np.random.choice(['f','m'],5),
                         'age':np.random.randint(20,30,size = 5),
                         'level':np.random.choice(['v1','v2','v3','v4'],5)
                         })

print(df)

df_dum = pd.get_dummies(df,columns = ['gender','level'])

print(df_dum)
'''
#--------------------------------------------------------------------------------------
'''
age = np.random.randint(12,80,size = 1000)

#df = pd.DataFrame({'id':[i for i in range(len(age))],
#                        'age':age
#                        })
#
#print(df.describe())

s = pd.Series(age)
#print(s.describe())
#print('='*50)

age_cut = pd.cut(s,bins = [0,18,45,60,80],right = False,
                 labels = ['未成年','青年','中年','老年'])

print(age_cut.head())
'''
#--------------------------------------------------------------------------------------
'''
from lxml import objectify

xml = objectify.parse('tt.xls')
#print(xml)

root = xml.getroot()

print(root.Worksheet.Table.Row.Cell.Data)

#print('getchildren:',root.Worksheet.Table.Row.getchildren())

for i in root.Worksheet.Table.Row:
    x = i.getchildren()
    for j in x:
        print(j.getchildren().text)
'''
#--------------------------------------------------------------------------------------
'''
os.chdir(r'D:\小鸡理财\OneDrive\python')
df = pd.read_csv('02.csv',header = None,engine = 'python')

print(len(df))

l = [1,2,3,4,5,6,7,8]*428

df['m'] = l

#print(df.head(50))


df.to_pickle('df.pkl')
print('ok')
'''
#--------------------------------------------------------------------------------------
'''
import matplotlib.dates as mdates

s = pd.Series(pd.date_range(start='20180723',periods = 100))
x = np.random.randint(200,size=100)

months = mdates.MonthLocator()
days = mdates.DayLocator()

timeFmt = mdates.DateFormatter('%Y-%m')

fig,ax = plt.subplots()

plt.plot(s,x)

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(days)

#plt.show()
'''
#--------------------------------------------------------------------------------------
'''
from sklearn import datasets
import matplotlib.patches as mpatches

iris = datasets.load_iris()

print(iris)
print('='*50)
#
#print(iris.target_names)
#print('='*50)

x = iris.data[:,2]
y = iris.data[:,3]
species = iris.target

x_min,x_max = x.min()-0.5,x.max()+0.5
y_min,y_max = y.min()-0.5,y.max()+0.5

plt.figure()
plt.title('iris datasets')
plt.scatter(x,y,c=species)
plt.xlabel('length')
plt.ylabel('width')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks(())
plt.legend()
plt.yticks(())
'''
#--------------------------------------------------------------------------------------
'''
from sklearn.decomposition import PCA
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()
x = iris.data[:,1]
y = iris.data[:,2]
species = iris.target

x_reduced = PCA(n_components=3).fit_transform(iris.data)

#SCARRERPLOT 3D
fig = plt.figure()
ax = Axes3D(fig)

ax.set_title('iris datasets')
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel('first')
ax.set_ylabel('second')
ax.set_zlabel('third')

ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
'''
#--------------------------------------------------------------------------------------
'''
from sklearn import datasets

np.random.seed(0)
iris = datasets.load_iris()
x = iris.data
y = iris.target
i = np.random.permutation(len(iris.data))
#print(i)

x_train = x[i[:-10]]
print(x_train)


y_train = y[i[:-10]]
#print(y_train)

x_test = x[i[-10:]]
y_test = y[i[-10:]]

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print(knn.fit(x_train,y_train))
print('='*50)

print(knn.predict(x_test))
print(y_test)
'''
#--------------------------------------------------------------------------------------

from sklearn import datasets
diabetes = datasets.load_diabetes()

x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]


from sklearn import linear_model
linreg = linear_model.LinearRegression()

linreg.fit(x_train,y_train)

linreg.coef_

linreg.predict(x_test)

y_test

linreg.score(x_test,y_test)






































