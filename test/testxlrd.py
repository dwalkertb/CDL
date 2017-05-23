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
import re
pynlpir.open()

item = []
data = xlrd.open_workbook('../res/dataset.xlsx')
#itemname = codecs.open('C:\\Users\\TBin\\Desktop\\itemname.txt', 'a+', "utf-8")
table = data.sheets()[0]
nrows = table.nrows

# 标题和摘要链接
for i in range(2):
    if i == 0:
        continue
    item.append(table.row_values(i)[2]+table.row_values(i)[4])

print(item)
print('以上链接后的结果**********************************')

singletextResult = []
s = ""
s1 = "".join(item).strip().encode('utf-8')

s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+".decode('utf8'), "".decode('utf8'), s1)

print(s)
print('以上为列表转换为字符串**********************************')

# 分词
for item in pynlpir.segment(s):
    singletextResult.append(item[0])
print(singletextResult)
print(type(singletextResult))
print('以上为分词后结果**********************************')

# 去掉停用词
stopwords = []
sw = codecs.open('../res/stopwords.txt', 'r+', encoding='utf-8')

for line in sw:
    line = line.strip()
    stopwords.append(line)  # 获得停用词列表

deltstopwords = []
for word in singletextResult:
    word = word.strip()
    #print(word)
    if word not in stopwords:
        #if word >= u'\u4e00' and word <= u'\u9fa5':  # 判断是否是汉字
            deltstopwords.append(word)
print(deltstopwords)


