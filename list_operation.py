#-*- coding: utf-8 -*-
#判断两个列表的交集和并集
import pandas as pd
import xlrd
import numpy as np
#excel_path =r'/Users/kun/Desktop/Citation/patent3.xlsx'
#当前路径
excel_path =r'patent3.xlsx'
d1 = pd.read_excel(excel_path, header=0, index_col=None, na_values='NULL',dtype=str,sheet_name='Sheet1')
d2 = pd.read_excel(excel_path, header=0, index_col=None, na_values='NULL',dtype=str,sheet_name='Sheet2')
#d.columns = ['a']
#print(d.iloc[0,0])
#d2.columns = ['a']
#查看前5行
print(d1.head(5))
print(d1.tail(5))
#查看总行数
print(d1.iloc[:,0].size)
#查看总列数
print(d1.columns.size)
#print(d)
#print(d2)


#print(d['a'].values[0].split(';'))
#print(d2['a'].values.tolist())

#list1 = d['a'].values[313].split(';')
#list1 = d['a'].values[314]
#print(list1)
list1=d1['H1'].values.tolist()
list2=d2['H1'].values.tolist()

"""
# -*- coding=utf-8 -*-
 
#方法一:
a=[2,3,4,5]
b=[2,5,8]
tmp = [val for val in a if val in b]
print tmp
#[2, 5]
 
#方法二
print list(set(a).intersection(set(b)))
 
print list(set(a).union(set(b)))
 
print list(set(b).difference(set(a))) # b中有而a中没有的
print list(set(a).difference(set(b))) # a中有而b中没有的


"""
#求两个列表的差集 list2 中有，list1中没有
k = list(set(list2).difference(set(list1)))

print(k)
list2=k
#filename = r'/Users/kun/Desktop/Citation/k1.txt'
#当前路径 写入list数据导本地文件
filename = r'k1.txt'
data = list2
file = open(filename,'a+')
for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')
    #按行存储
    #s = s.replace("'",'').replace(',','') +'\t'
    #按列存储
    s = s.replace("'", '').replace(',', '') + '\n'
    file.write(s)
file.write('\n')
file.close()
print("保存文件成功")
#print(d1['Sheet1'])