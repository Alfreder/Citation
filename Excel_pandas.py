#-*- coding:utf8-*-
#测试pandas
import pandas as pd
#excelFile = r'/Users/kun/Desktop/Citation/Patent1.xlsx'
excelFile2 = r'/Users/kun/Desktop/Citation/1.xlsx'
#d = pd.read_excel(excelFile, header=0)
d2 = pd.read_excel(excelFile2, header=0, index_col=None, na_values='NULL',dtype=str,sheet_name='Sheet2')
#print(d)
#df = pd.DataFrame(d)
df2 = pd.DataFrame(d2)
print('-'*10)
print(df2['H1'].values.tolist())
print('-'*10)
print(df2.iloc[:,1])
print("-"*10)
print(df2.loc[0])


list1 = df2['H1'].values.tolist()
#(list1)
