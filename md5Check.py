#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:17:13 2019

@author: zhengguosong
"""


import hashlib
import os
import pandas as pd

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

filepath = '/home/data/Rseq/wangyangxian/'          # 上传文件存储路径
md5file = '/home/data/Rseq/wangyangxian/md5.txt'    # 原始md5文件
out_dir = '/home/data/Rseq/'             # 结果输出路径
# Md5 Check the file in path
file_lst = os.listdir(filepath)
ff = file_lst[:10]
ff = [x for x in ff if not x.endswith('.bai')]

df = pd.read_csv(md5file, sep = ' |/', header = None)

res_lst = []
for f in ff:
    m = GetFileMd5(f)
    n = list(df[df[3] == f][0])[0]
    aa = m==n
    if aa is not True:
        print('Warning !! %s is %s' %(f,aa))
        res_lst.append([f,m,n,aa])

res_df = pd.DataFrame(res_lst)
res_df.to_csv(out_dir + 'md5Comp.csv', index=False)
