#-*- coding:utf8-*-
#kun@20180801_17:10
#读取两个文件每行数据存到列表中
import codecs
import sys
#/Users/kun/Desktop/
f1 = codecs.open(r"/Users/kun/Desktop/Citation/citation", "r", "utf-8")
#f1 = open(r"C://2007//3_2","a+",encoding='utf-8')
result1=[]
#with open('accounts.txt','r') as f:
for line in f1:
    result1.append(list(line.strip('\n').split(',')))

print(result1)

f2 = codecs.open(r"/Users/kun/Desktop/Citation/patent", "r", "utf-8")
#f1 = open(r"C://2007//3_2","a+",encoding='utf-8')
result2=[]
#with open('accounts.txt','r') as f:
for line in f2:
    result2.append(list(line.strip('\n').split(',')))
print(result2)
#求两个列表的交集
tmp = [val for val in result1 if val in result2]

#print (tmp)

#打印出交集的数量
print("引用的个数为："+str(len(tmp)))