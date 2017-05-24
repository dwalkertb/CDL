# -*- coding: utf-8 -*-
'''
#_author_:bin_t
#Version:python 3.6.1 
#e_mail:dwalkertb@qq.com
'''
import xlrd
import codecs
import pynlpir
import re
pynlpir.open()

allItemResult = []
data = xlrd.open_workbook('../res/dataset.xlsx')
table = data.sheets()[0]
nrows = table.nrows
item = []
for i in range(5):
    if i == 0:
        continue
    item.append(table.row_values(i)[2]+table.row_values(i)[4]) # 标题和摘要链接

    print('****************标题和摘要链接******************')
    print(item)
    print('**********************************************')

    singleItemResult = []
    s = ""
    s1 = "".join(item).strip() #列表转换为串
    symbol = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+" #正则表达式 删除标点符号
    s = re.sub(symbol, "", s1)

    print('****************列表转换为字符串并去掉标点符号******************')
    print(s)
    print('**********************************************')

    for item in pynlpir.segment(s): # 分词
        singleItemResult.append(item[0])

    print('****************分词后结果******************')
    print(singleItemResult)
    print('**********************************************')


    stopwords = []
    sw = codecs.open('../res/stopwords.txt', 'r+', encoding='utf-8')
    for line in sw:
        line = line.strip()
        stopwords.append(line)  # 获得停用词列表
    deltstopwords = []
    rowVec = ""
    for word in singleItemResult:
        word = word.strip()
        if word not in stopwords: # 去掉停用词
            deltstopwords.append(word)
    rowVec = rowVec + " ".join(deltstopwords)
    print('****************行向量******************')
    print(rowVec)
    print('**********************************************')
    allItemResult.append(rowVec)

print('****************每行结果作为列表元素存放在大列表******************')
print(allItemResult)
print('**********************************************')