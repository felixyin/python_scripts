#!/bin/python
# coding: utf-8
import sys
import os
import re
import shutil

src_folder = '/home/fy/temp/python_scripts/test_src/'
des_folder = '/home/fy/temp/python_scripts/test_des/'

reload(sys)
sys.setdefaultencoding('utf-8')

# 测试代码

for old_file in os.listdir(src_folder):
    new_file_hz = re.findall(r".+(\..*)", old_file)[0].decode('utf-8')
    new_file = re.findall(r".*com.(.+?)\..*", old_file)[0].decode('utf-8')
    shutil.move(src_folder + old_file, des_folder + new_file + new_file_hz)
