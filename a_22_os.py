#! /usr/bin/env python3

"""
This part shows you common os functions
"""
import os

directory= "/home/yuxiangyong/dev/temp"
path="{}/file.txt".format(directory)
#os.access(path, mode) : check file permission for current user

ret1 = os.access(path, os.F_OK) #check file exists
ret2 = os.access(path, os.R_OK) #check Ready permission on path
ret3 = os.access(path, os.W_OK) #check Write permission on path
ret4 = os.access(path, os.X_OK) #check Execute permission on path

print("Permission on file {} is exists-{}, R-{},W-{},E-{}".format(path, \
        ret1,ret2,ret3,ret4))


#chdir() change working directory
pwd=os.getcwd()
new_pwd=os.chdir(directory)
print("Previous working dir: {}, current is: {}".format(pwd,new_pwd))

#chflags(path, mode) change flags for a file (unix only)
import os, stat
#flag =stat.UF_IMMUTABLE
#os.chflags(path, flag)

#chmod(path, mode)
os.chmod(path, stat.S_IXOTH)

#os.remove(path)
#os.removedirs(path) --use recursive
#os.rmdir(path) --need empty dir
#os.rename(src,dst)
#os.renames(old, new) 
#os.path.basename(path)
#       .dirname(path)
#       .split(path)
#       .join(...)
#       .getatime(path)
#       .getctime(path)
#       .getsize(path)

import os
import time
 
file=path # 文件路径
 
print( os.path.getatime(file) )   # 输出最近访问时间
print( os.path.getctime(file) )   # 输出文件创建时间
print( os.path.getmtime(file) )   # 输出最近修改时间
print( time.gmtime(os.path.getmtime(file)) )  # 以struct_time形式输出最近修改时间
print( os.path.getsize(file) )   # 输出文件大小（字节为单位）
print( os.path.abspath(file) )   # 输出绝对路径
print( os.path.normpath(file) )  # 规范path字符串形式

