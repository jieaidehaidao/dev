#!/usr/bin/python
#coding:utf-8
import time

"""
常用 日期调用 api

历史修改记录：    
     
*序号    日期                作者        备注                    
*1.              
"""
class DateUtil:

    #定义静态方法，获取当前时间，格式：%Y-%m-%d %H:%M:%S
    @staticmethod
    def getCurrentDateStr():
        tim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return tim

    @staticmethod
    def getCurrentDateStr1():
        tim = time.strftime('%Y-%m-%d %H:%M:%S.%mZ', time.localtime(time.time()))
        return tim

    @staticmethod
    def getTime():
        return time.time()

    # 定义静态方法，获取当前时间，格式："%Y%m%d%H%M%S"
    @staticmethod
    def getStrTime():
        strtime=str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))
        return strtime

