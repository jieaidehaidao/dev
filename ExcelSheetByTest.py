#!/usr/bin/python
#coding:utf-8
import xlrd
from xlutils.copy import copy
"""
excel 读取
安装xlrd模块
pip3 install xlrd -U

参数测试模版参考：testTpl.xlsx
测试报告模版参考：testReprotTpl.xlsx

*序号    日期                作者        备注    
*1.      
"""

class ExcelSheetByTest:
    """ sFile 文件路径，index sheet位置，从0开始"""
    def __init__(self, sFile, index=0):
        try:
            self.workbook = xlrd.open_workbook(sFile)
            self.table=self.workbook.sheets()[index]#新增索引查找sheet
        except Exception as e:
            print(e)
            exit()

        self.sheet = self.workbook.sheet_by_index(index)  # 查询Excel的第一个sheet

    #读取excel当前sheet的名称
    def sheet_name(self):
        return self.sheet.name
    #excel 当前sheet可读取的行数
    def nrows(self):
        return self.sheet.nrows
    #excel 当前sheet可读取的列数
    def ncols(self):
        return self.sheet.ncols
    #读取excel指定单元格的内容
    def cellxy(self, rowx, colx):
        # type: (object, object) -> object
        cell_value = self.sheet.cell(rowx, colx).value
        return cell_value


    # 读取excel单元格第一列的内容
    def col_values(self,colx):
        moduleData = dict()
        for i in range(0,self.nrows(),2):
            if i%2 == 0:
                j = int(i/2)
                val = self.cellxy(i, 0)
                moduleData[j]=val
        return moduleData

    """ 返回excel 
        A 列 #serviceName# 定义接口名称，返回的data对象可以通过data[#serviceName#]获得对应接口下的参数定义
        B、C列的key-value值，跳过###开头的说明内容 
    """
    def getData(self):
        list = []
        moduleData = dict()
        for line in range(0, self.nrows()):
            val = self.cellxy(line, 0)
            if val.find("###") != 0:
                if val.find("#serviceName#") != 0:
                    moduleData[list[len(list) - 1]][self.cellxy(line, 1)] = self.cellxy(line, 2)
                else:
                    serviceName = self.cellxy(line, 1).strip()
                    list.append(serviceName)
                    moduleData[list[len(list) - 1]] = dict()

        return moduleData



    """ 返回excel 
        row1 定义参数名称
        row2 定义参数值
        其中 A、B列特殊处理：A列定义接口名称，B列定义接口测试服务编码
        返回的data对象可以通过data[#serviceName#]获得对应接口下的参数定义，其中#serviceName#对应row2-B列值
    """
    def getDataByRow(self):
        list = []
        moduleData = dict()
        for line in range(0, self.nrows(), 2):
            if self.get_merged_cells_value(line,0).startswith('###'):
                print(self.get_merged_cells_value(line,0)+"### \t\t'#'跳过验证")
                continue

            for col in range(1, self.ncols()):
                key = self.cellxy(line, col)
                key=key.partition("|")[0]
                val = self.cellxy(line + 1, col)
                #从第三列开始为参数
                if col > 1 :
                    moduleData[list[len(list) - 1]][key] = val
                elif col == 1:
                    serviceName = val.strip()
                    list.append(serviceName)
                    moduleData[list[len(list) - 1]] = dict()
        print(moduleData)
        return moduleData

    def get_merged_cells_value(self, row_index, col_index):
        """
        先判断给定的单元格，是否属于合并单元格；
        如果是合并单元格，就返回合并单元格的内容
        :return:
        """
        merged = self.sheet.merged_cells
        for (rlow, rhigh, clow, chigh) in merged:
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.sheet.cell_value(rlow, clow)
                    # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                    return cell_value
                    break
        return None
