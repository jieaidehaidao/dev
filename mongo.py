#!/usr/bin/python
#coding:utf-8
import pymongo
from bson.objectid import ObjectId
import datetime

# mongo操作类
class mongo:
    def __init__(self,ip='127.0.0.1',port='27017',username='',password='',dbname='testDB',collection='test'):
        # ip = ''
        # port = ''
        # username = ''
        # password = ''
        # mongodb://root:123456@localhost:27017/
        if username.__len__()>0 or password.__len__()>0:
            self.host = 'mongodb://{}:{}@{}:{}/'.format(username,password,ip,port)
        else:
            self.host = 'mongodb://{}:{}/'.format(ip, port)
        print(self.host)
        self.client = pymongo.MongoClient(self.host)
        self.db = self.client[dbname]
        self.collection = self.db[collection]

    def useCollection(self,collection):
        self.collection = self.db[collection]

    def getCollection(self):
        return self.collection

    def getByID(self,id):
        return self.getCollection().find_one({'_id':id})

    def findOne(self,data):
        return self.getCollection().find_one(data)

    def find(self,queryDict):
        return self.getCollection().find(queryDict)

    def insert(self,data):
        result=self.getCollection().insert_one(data)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write('[' + datetime.datetime.now().__str__() +  '] insert'+'\tdata:'+data.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    def insertMany(self,dataList):
        result=self.getCollection().insert_many(dataList)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write('[' + datetime.datetime.now().__str__() +  '] insertMany' + '\tdata:'+dataList.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    def update(self,query,data):
        result = self.getCollection().update_one(query, data)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write( '[' + datetime.datetime.now().__str__() + '] update\t'+'query:'+query.__str__()+'\tdata:'+data.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    def updateMany(self,query,data):
        result = self.getCollection().update_many(query,data)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write( '[' + datetime.datetime.now().__str__() + '] updateMany\t'+'query:'+query.__str__()+'\tdata:'+data.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    def delete(self,data):
        result=self.getCollection().delete_one(data)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write('[' + datetime.datetime.now().__str__() + '] delete'+'\tdata:'+data.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    def deleteMany(self,dataList):
        result = self.getCollection().delete_many(dataList)
        with open('logs/MongoOption.log',encoding='utf-8',mode='a') as f:
            f.write( '[' + datetime.datetime.now().__str__() + '] deleteMany'+'\tdata:'+dataList.__str__() +'\t' + str(result.acknowledged) + '\n')
        f.close()
        return result

    #查找某个字段是否存在的数据ID
    def findFieldIsExist(self,field,flag=False):
        idList=[]
        datalist = self.getCollection().find({field: {'$exists': flag}})
        for item in datalist:
            idList.append(item['_id'])
        return idList


    #获取Id的ObjectId
    def getObjId(id):
        try:
            _id=ObjectId(id)
        except:
            _id=id
        return _id

# 主函数执行入口
if __name__ == '__main__':
    test=mongo(collection='mongo')
    print(test.insert({'a':'a'}).acknowledged)
    print(test.findFieldIsExist(field='a',flag=True))
    print(test.update({'a':'a'},{'$set':{'a':'b'}}).acknowledged)
    print(test.findOne({'a':'b'}))
    print(test.deleteMany({'a':{'$regex':'[y-z]'}}).acknowledged)

