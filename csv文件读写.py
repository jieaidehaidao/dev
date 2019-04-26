#!/usr/bin/python
#coding:utf-8
import csv

csvFile = csv.reader(open(filestr='',encoding='utf-8',mode='r'))
csvFileWrite = csv.writer(open(filestr+'csv_write.csv',encoding='utf-8',mode='a',newline=''),dialect='excel')

for row in csvFile:
    print(row)
row='a,b.c'
csvFileWrite.writerow(row)




