#!/usr/bin/python
#coding:utf-8
import redis

class redisOption:
    #初始化连接
    def __init__(self,ip='127.0.0.1',port=6379,db_index=0):
        self.myredis = redis.Redis(host=ip, port=port ,db=db_index)

#删除一个keyList列表中的所有key
    def delKeys(self,keyList):
        for key in keyList:
            self.myredis.delete(key)
        print("清除完成！")

# 删除key
    def delete(self, key):
        self.myredis.delete(key)

#新增一个keyList列表中的所有key  [{'key':'aaa','value':'aaa'},{'key':'bbb','value':'bbb'}]
    def addKeys(self,keyListDict):
        for each_dict in keyListDict:
            self.myredis.set(each_dict['key'],each_dict['value'])
        print("添加完成！")

#新增一个key值    {'key':'aaa','value':'aaa'}
    def set(self,addDict):
        self.myredis.set(addDict['key'],addDict['value'])
        print("添加成功")

#查看key的剩余生存时间
    def ttl(self,key):
        return self.myredis.ttl(key)

# 获取key值
    def get(self,key):
        return self.myredis.get(key)

#正则表达式获取keys列表
    def keys(self,pattern='*'):
        return self.myredis.keys(pattern)

if __name__ == '__main__':
# 此脚本redisOption类不好用，建议使用原redis模块
    # redisIp='127.0.0.1'
    # redisPort=6379
    # dbIndex=5;
    # r = redisOption(ip=redisIp, port=redisPort, db_index=dbIndex)
    r=redisOption()
    r.set({'key':'aaa','value':'bbb'})
    print(r.get('aaa'))
    