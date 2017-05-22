# -*- coding: utf-8 -*-
'''
#excel读取数据测试
#_author_:bin_t
#Version:python 3.6.1 
#e_mail:dwalkertb@qq.com
'''

import xlrd
import codecs

item = []
data = xlrd.open_workbook('C:\\Users\\TBin\\Desktop\\dataset.xlsx')
itemname = codecs.open('C:\\Users\\TBin\\Desktop\\itemname.txt', 'a+', "utf-8")
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i == 0:
        continue
    item.append(table.row_values(i)[2:3])

print(type(item))
print(type(table.row_values(i)[2:3]))
'''
for n in item:
    itemname.write(n+'\n')
itemname.close()

'''
