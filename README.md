### CNLAB-协同推荐专家系统
数据处理过程依据论文：**Collaborative Topic Modeling for Recommending Scientific Articles**

_论文中相关描述：
For each article, we concatenate its title and abstract. We remove stop words and
use tf-idf to choose the top 8000 distinct words as the vocabulary 。_

本实验处理流程：
1. 给定的文件每行对应一个项目名字、专家、摘要。将项目名字和摘要链接，得到的文本用pynlpir进行中文分词，
并且去掉停用词，用tf-idf算法，选择一定数量的词，构成最后词袋。
