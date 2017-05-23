# -*- coding: utf-8 -*-
'''
#excel读取数据测试
#_author_:bin_t
#Version:python 3.6.1 
#e_mail:dwalkertb@qq.com
'''

import xlrd
import codecs
import pynlpir

item = []
data = xlrd.open_workbook('../res/dataset.xlsx')
#itemname = codecs.open('C:\\Users\\TBin\\Desktop\\itemname.txt', 'a+', "utf-8")
table = data.sheets()[0]
nrows = table.nrows
for i in range(5):
    if i == 0:
        continue
    item.append(table.row_values(i)[2]+table.row_values(i)[4])
print(item)
print('**********************************')

singletextResult = []
s = ""
s1 = "".join(item).strip().encode('utf-8')

print(s1)
print('**********************************')

for item in pynlpir.segment(s1):
    singletextResult.append(item)
print(singletextResult)



