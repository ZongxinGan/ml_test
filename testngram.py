# -*-coding:utf-8-*-
import re
import codecs
import jieba
from sklearn import feature_extraction

with codecs.open("neirong.txt",'r') as f:
    text = f.read()
text = re.sub(r"\s{2,}","",text)
text = re.sub(r"\n","",text)
#text = "基于Flink流处理的动态实时超大规模用户行为分析"

cut = jieba.cut(text)
listcut = list(cut)
print(listcut)

ngram_vectorizer = feature_extraction.text.CountVectorizer()
count_vec = ngram_vectorizer.fit_transform(listcut)
words = ngram_vectorizer.get_feature_names()

transformer=feature_extraction.text.TfidfTransformer()
tfidf=transformer.fit_transform(count_vec)

print(count_vec)
print(words)
print(count_vec.todense())
print(tfidf)
