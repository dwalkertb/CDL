# -*- coding: utf-8 -*-

""" 
功能：PyNLPIR文本预处理 
过程：文本分词，过滤停用词，词频统计，特征选择，文本表示 
时间：2016年8月25日10:52:43 
"""

import pynlpir
import codecs
import math

pynlpir.open()

# 文本分词
typelist = [u"财经", u"IT", u"健康", u"体育", u"旅游", u"教育", u"招聘", u"文化", u"军事"]

typetxt = codecs.open('C:\\Users\\TBin\\Desktop\\typetxt.txt', 'a', encoding='utf-8')
wordseg_result = codecs.open('C:\\Users\\TBin\\Desktop\\wordseg_result.txt', 'a', encoding='utf-8')

allresult = []
for j in range(1, 10):
    for i in range(10, 510):
        typetxt.write(typelist[j - 1] + "\n")
        s = ""
        singletext_result = []
        print(u'正在对第 %s 个文件夹的第 %s 个文本进行分词处理.....' % (j, i))
        f = codecs.open(
            'C:\\Users\\Administrator\\Desktop\\textmining_experiment2\\Word Segment\\traintxt500\\%d\\%d.txt' % (j, i),
            'r', "gb18030")
        for line in f:
            s += line.strip().encode('utf-8')

        for item in pynlpir.segment(s):
            singletext_result.append(item[0])
        allresult.append(singletext_result)

typetxt.close()
print(u'文本类别析出完毕！结果已输出到desktop的txttype.txt！')
# 直接打印出结果
# for singletext_result in allresult:
#    for item in singletext_result:
#       print item

# 所有结果写入一个txt，一行一个文本
for singletext_result in allresult:
    for item in singletext_result:
        wordseg_result.write(item + '\t')
    wordseg_result.write('\n')
wordseg_result.close()
print(u'分词完毕！分词结果已输出到desktop的wordseg_result.txt！' + '\n')