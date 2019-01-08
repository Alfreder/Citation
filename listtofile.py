#写入列表到文件
list2=[1,2,3,4,5]
#filename = r'/Users/kun/Desktop/Citation/list.txt'
filename = r'list.txt'
data = list2
#追加写入
# file = open(filename,'a+')
#写入
file = open(filename,'w+')
for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')
    s = s.replace("'",'').replace(',','') +'\t'
    file.write(s)
    #按列写入
    file.write('\n')
file.close()
print("保存文件成功")
#print(d['Sheet1'])