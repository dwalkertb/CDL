# -*- coding: utf-8 -*-
'''
#_author_:bin_t
#Version:python 3.6.1 
#e_mail:dwalkertb@qq.com
'''

import xlrd
import codecs
import pynlpir


dataset = xlrd.open_workbook('../res/dataset.xlsx')
itemname = codecs.open('C:\\Users\\TBin\\Desktop\\itemname.txt', 'a+', "utf-8")

table = dataset.sheets()[0] #读取book的第一个sheet
nrows = table.nrows

titlandabstract = []
for i in range(nrows):
    if i == 0:
        continue # 第一行为表头
    titlandabstract.append(table.row_values(i)[2]+table.row_values(i)[4])

#print(titlandabstract)

def getCorpus():
    #获取预料（标题+摘要）
    dataset = xlrd.open_workbook('../res/dataset.xlsx')
    table = dataset.sheets()[0]  # 读取book的第一个sheet
    nrows = table.nrows
    titlandabstract = []
    for i in range(nrows):
        if i == 0:
            continue  # 第一行为表头跳过
        titlandabstract.append(table.row_values(i)[2] + table.row_values(i)[4])
    return titlandabstract

def wordSeg(corpus):
    # 文本分词
    s = ""
    wordSegresult = []
    print(u'正在进行分词处理.....')
    s = "".join(line)
    s = s.strip().encode('utf-8')
    print(u'文件去掉空格结果...')

    for item in pynlpir.segment(s):
        singletext_result.append(item[0])
    print(u'分词后的结果。。。')
    # 直接打印出结果
    for item in singletext_result:
        print(item)

    # 所有结果写入一个txt，一行一个文本
    for item in singletext_result:
        wordseg_result.write(item + '\t')
    wordseg_result.write('\n')
    wordseg_result.close()
    print(u'分词完毕！分词结果已输出到desktop的wordseg_result.txt！' + '\n')

def deltStopwords():