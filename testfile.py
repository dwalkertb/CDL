# -*- coding: utf-8 -*- 
import codecs

'''
/software/python/3.6.1 
author:bin_t
e_mail:dwalkertb@qq.com
'''


s = ""
print(u'正在进行分词处理.....')
f = codecs.open('C:\\Users\\TBin\\Desktop\\beforedel.txt', 'r', "utf-8")
line = f.readlines()
s ="".join(line)
s = s.strip().encode('utf-8')
'''
for line in f:
    s = line.strip().encode('utf-8')
'''
print(u'文件去掉空格结果...')
#print(s)
print(s.decode("utf-8","ignore"))