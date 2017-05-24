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

singleItemResult = []
allItemResult = []
s = ""
s1 = "".join(item).strip() #列表转换为串
symbol = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+" #正则表达式 删除标点符号
s = re.sub(symbol, "", s1)

print(s)
print('以上为列表转换为字符串并且去掉了标点符号**********************************')

# 分词
for item in pynlpir.segment(s):
    singleItemResult.append(item[0])
print(singleItemResult)
print(type(singleItemResult))
print('以上为分词后结果**********************************')

# 去掉停用词
stopwords = []
sw = codecs.open('../res/stopwords.txt', 'r+', encoding='utf-8')

for line in sw:
    line = line.strip()
    stopwords.append(line)  # 获得停用词列表

deltstopwords = []
rowVec = ""
for word in singleItemResult:
    word = word.strip()
    #print(word)
    if word not in stopwords:
        deltstopwords.append(word)

rowVec = rowVec + " ".join(deltstopwords)
print(rowVec)


