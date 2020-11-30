#!/bin/python
# coding: utf-8
import sys
import os
import re

# import shutil # 太慢，已废弃

# 用来添加为系统定时任务，定期将dsget下载的“电影天堂网址”的电影，处理后移动到video station电影库中


reload(sys)
sys.setdefaultencoding('utf-8')


def do(src_folder, des_folder):
    for old_file in os.listdir(src_folder):
        new_file_hz = re.findall(r".+(\..*)", old_file)[0].decode('utf-8')
        new_file = re.findall(r".*com.(.+?)\..*", old_file)[0].decode('utf-8')
        os.system('mv ' + src_folder + old_file + ' ' + des_folder + new_file + new_file_hz)
    #    shutil.move(src_folder + old_file, des_folder + new_file + new_file_hz)


# 修改为你的nas服务器路径
src = '/home/fy/temp/python_scripts/test_src/'
dest = '/home/fy/temp/python_scripts/test_des/'
do(src, dest)

