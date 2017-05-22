#! /software/python/3.6.1 
# -*- coding: utf-8 -*- 
# author:bin_t
# e_mail:dwalkertb@qq.com

#import codecs


stopwords=[]
st = open('C:\\Users\\TBin\\Desktop\\stopwords.txt','r')
for line in st.readlines():
    stopwords.append(line)

beforedel =[]
f = open('C:\\Users\\TBin\\Desktop\\beforedel.txt','r')
for line in f.readlines():
    beforedel.append(line)

print(u'正在处理...')
afterdel = open('C:\\Users\\TBin\\Desktop\\afterdel.txt','w')

for i in range(len(beforedel)):
    if beforedel[i] not in stopwords:
        afterdel.write(beforedel[i])
st.close()
f.close()
afterdel.close()