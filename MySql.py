#!/usr/bin/python
#coding:utf-8
import pymysql

"""
mysql 数据库操作
"""
class MySql:
    def __init__(self, host, port=3306,
                 user="", passwd="", db="", charset='utf8'):
        # 创建连接
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

    """
    执行sql 操作
    """
    def exec(self, sql, params = ()):
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql, params)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 如果发生错误则回滚
            self.conn.rollback()

    """
    查询当条结果集
    """
    def selectOne(self, sql, params=()):
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        # 执行sql语句
        cursor.execute(sql, params)
        row = cursor.fetchone()
        # 提交到数据库执行
        self.conn.commit()
        cursor.close()

        return row

    """
    查询多条结果集
    """
    def selectAll(self, sql, params=()):
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        # 执行sql语句
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        # 提交到数据库执行
        self.conn.commit()
        cursor.close()

        return rows

    """
    关闭数据源
    """
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    #构建MySql对象，指定ip、端口、用户名、密码、链接的数据库实例
    mysql = MySql("192.168.1.84", 3306, "root","123456", "customer")

    #demo 查询当条记录
    result = mysql.selectOne("select serialNO,subject,detail from tcustomer_editdetail")
    print(result)
    #demo 删除指定serialNO的数据
    mysql.exec("delete from tcustomer_editdetail where serialNO=%s",(result[0]))

    #MySql 使用完 需要关闭链接
    mysql.close()