# coding=utf-8

#该程序借鉴了学长的思路与代码

#模块引入
import jieba
import re
import gensim

#文件模块，获取文本内容
def getFileContents(path):
    str=''
    f=open(path,'r',encoding='UTF-8')
    line=f.readline()
    while line:
        str=str+line
        line=f.readline()
    f.close()
    return str


#语句处理模块，将句子分词且过滤掉标点和转义符号
def strFilter(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = pattern.sub("", string)
    result = jieba.lcut(string)
    return result

#转换和计算模块，将文字转换为向量并计算其余弦相似度
def transAndComput(text1,text2):
    texts=[text1,text2]
    #文字转换为向量
    dictionary=gensim.corpora.Dictionary(texts)
    corpus=[dictionary.doc2bow(text) for text in texts]    
    #计算余弦相似度
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

def conduct(path1,path2):
    save_path = "D:\PythonApplication1\save.txt"
    str1 = getFileContents(path1)
    str2 = getFileContents(path2)
    text1 = strFilter(str1)
    text2 = strFilter(str2)
    similarity = transAndComput(text1, text2)
    print("\nSimilarity Of 2 passages:%.4f\n"%similarity)
    #将相似度结果写入指定文件
    f = open(save_path, 'a', encoding='UTF-8')
    f.write("Similarity Of 2 passages:%.4f\n"%similarity)
    f.close()



if __name__ == '__main__':
    conduct("D:\PythonApplication1\orig_0.8_dis_10.txt","D:\PythonApplication1\orig_0.8_dis_15.txt")
    conduct("D:\PythonApplication1\orig_0.8_add.txt","D:\PythonApplication1\orig.txt")
    conduct("D:\PythonApplication1\orig_0.8_dis_1.txt","D:\PythonApplication1\orig_0.8_del.txt")
