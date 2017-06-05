# -*- coding: utf-8 -*-
'''
#_author_:bin_t
#Version:python 3.6.1 
#e_mail:dwalkertb@qq.com
'''
import codecs
import re
from time import time

import jieba
import pynlpir
import xlrd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# 英文正则表达式
engRe = r'[A-Za-z0-9]+'
begin = time()
pynlpir.open()

allItemResult = []
data = xlrd.open_workbook('../res/datasetfortest.xlsx')
table = data.sheets()[0]
nrows = table.nrows
item = []
stopwords = []
sw = codecs.open('../res/stopwords.txt', 'r+', encoding='utf-8')

for line in sw:
    line = line.strip()
    stopwords.append(line)  # 获得停用词列表


class ReadData(object):
    def __iter__(self):
        for i in range(nrows):
            if i == 0:
                continue
            r = table.row_values(i)[2] + table.row_values(i)[4]
            yield r


records = ReadData()
count = 1
for row in records:
    # 去除英文
    cleanedRow = re.sub(engRe, '', row)

    # singleItemResult = [item[0] for item in pynlpir.segment(cleanedRow)]
    singleItemResult = list(jieba.cut(cleanedRow, cut_all=False))
    cleanedST = [word.strip() for word in singleItemResult if word not in stopwords]

    rowVec = " ".join(cleanedST)
    allItemResult.append(rowVec)
    count = count + 1

print('已完成数据预处理(数据清洗、分词等)！')

end = time()

# 保存分词后数据
cleanedData = '\n'.join(allItemResult)
open("../tmp/cleaneddataset.txt", "a", encoding='UTF-8').write(cleanedData)

print("\n第一阶段共花费时间 %f 秒，共读取记录数: %d, 实际处理记录数：%d" % (end - begin, nrows, count))

vectorizer = CountVectorizer(min_df=2)  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
tfidf = transformer.fit_transform(
    vectorizer.fit_transform(allItemResult))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵

word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

'''
for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word)):
        print(word[j], weight[i][j])

print(tfidf)
'''
