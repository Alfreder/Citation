#-*- coding:utf8-*-
#kun@20180801_17:10
#读取两个文件每行数据存到列表中
import codecs
import sys
#/Users/kun/Desktop/
#C://2007//
#f1 = codecs.open(r"/Users/kun/Desktop/Citation/Excel.xlsx", "r", "utf-8")


# -*- coding: utf-8 -*-
import xlrd
def read_excel():
    # 打开文件
    #workbook = xlrd.open_workbook(r"/Users/kun/Desktop/Citation/Excel.xlsx")
    workbook = xlrd.open_workbook(r"/Users/kun/Desktop/Citation/Patent1.xlsx")
    # 获取所有sheet
    #print( workbook.sheet_names() )
    # [u'sheet1', u'sheet2'])
    #获取sheet2
    #sheet2_name = workbook.sheet_names()[0]
    #print( sheet2_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_name('Sheet1')
    sheet2 = workbook.sheet_by_name('Sheet2')
    # sheet的名称，行数，列数
    print( sheet1.name, sheet1.nrows, sheet1.ncols)
    print( sheet2.name, sheet2.nrows, sheet2.ncols)
    rows = sheet2.row_values(0) # 获取第1行内容
    #print(rows)
    cols_sheet1 = sheet1.col_values(0)  # 获取sheet1第一列内容
    cols_sheet1 = sheet1.cell_value(0,0)  # 获取sheet1第一行第一列内容
    #print(cols_sheet1)
    cols_sheet2 = sheet2.col_values(0) # 获取sheet2第一列内容
    #print( type(cols_sheet1))
    #print("patent 1 citation num = "+ str(len(cols_sheet1)))
    #print(type(cols_sheet1[0]))
    #print(cols_sheet1[0].split(';'))
    #cols_sheet1 = sheet1.cell_value(315, 0)
    #print(cols_sheet1)
    j = 0
    for i in range(0,sheet1.nrows):
        cols_sheet1_split = ""
        cols_sheet1 = sheet1.cell_value(i, 0)  # 获取sheet1第一列内容
        #print(type(cols_sheet1))
        if cols_sheet1 == '':
            print("空值 = " + cols_sheet1)
            #print(1)
        cols_sheet1_split = cols_sheet1.replace('\n', '').replace(' ','').strip('\r').split(';')
        #print(cols_sheet1_split)
        #print(cols_sheet1_split)

        #print("total H04M num = " + str(len(cols_sheet2)))


        ####################
        #判断两个专利的交集
        tmp = [val for val in cols_sheet1_split if val in cols_sheet2]
        print("patent "+str(i+1) +" joint_citation num = "+ str(len(tmp)))
        #print(tmp)

        j = j + len(tmp)
        ####################
        #获取单元格内容的三种方法
        #print( sheet2.cell(1,0).value.encode('utf-8'))
        #print( sheet2.cell_value(1,0).encode('utf-8'))
        #print( sheet2.row(1)[0].value.encode('utf-8'))
        # 获取单元格内容的数据类型
        #print( sheet2.cell(1,3).ctype)
    print("total citation = " + str(j))
if __name__ == '__main__':
    read_excel()