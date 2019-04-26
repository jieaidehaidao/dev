#!/usr/bin/python
#coding:utf-8
import os
import hashlib

def get_file_md5(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
  return md5

def get_bigfile_md5(file_path):
  f = open(file_path,'rb')
  md5_obj = hashlib.md5()
  while True:
    d = f.read(8096)
    if not d:
      break
    md5_obj.update(d)
  hash_code = md5_obj.hexdigest()
  f.close()
  md5 = str(hash_code).lower()
  return md5


def get_string_md5(string):
  """
  计算字符串md5值
  :param string: 输入字符串
  :return: 字符串md5
  """
  md5 = hashlib.md5()
  md5.update(string.encode())
  return md5.hexdigest()

print(get_string_md5('test1234'))