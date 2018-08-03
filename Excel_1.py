#-*- coding:utf8-*-
#kun@20180801_17:10
#读取两个文件每行数据存到列表中
import codecs
import sys
#/Users/kun/Desktop/
#f1 = codecs.open(r"/Users/kun/Desktop/Citation/Excel.xlsx", "r", "utf-8")


# -*- coding: utf-8 -*-
import xlrd
def read_excel():
    # 打开文件
    #workbook = xlrd.open_workbook(r"/Users/kun/Desktop/Citation/Excel.xlsx")
    workbook = xlrd.open_workbook(r"/Users/kun/Desktop/Citation/Patent.xlsx")
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
    #print( sheet2.name,sheet2.nrows,sheet2.ncols)
    #rows = sheet2.row_values(1) # 获取第四行内容
    cols_sheet1 = sheet1.col_values(0)  # 获取sheet1第一列内容
    cols_sheet2 = sheet2.col_values(0) # 获取sheet2第一列内容
    #print( rows)
    print("patent 1 citation num = "+ str(len(cols_sheet1)))
    print("total H04M num = " + str(len(cols_sheet2)))

    ####################
    #判断两个专利的交集
    tmp = [val for val in cols_sheet1 if val in cols_sheet2]
    print("patent 1 joint_citation num = "+ str(len(tmp)))
    print(tmp)

    ####################
    #获取单元格内容的三种方法
    #print( sheet2.cell(1,0).value.encode('utf-8'))
    #print( sheet2.cell_value(1,0).encode('utf-8'))
    #print( sheet2.row(1)[0].value.encode('utf-8'))
    # 获取单元格内容的数据类型
    #print( sheet2.cell(1,3).ctype)
if __name__ == '__main__':
    read_excel()