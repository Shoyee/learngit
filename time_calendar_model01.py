#!/usr/bin/env python3
#coding:utf-8
'''
import  time
local_time = time.localtime()
print(local_time)
print(type(local_time))

gm_time = time.gmtime()
print(gm_time)
print(type(gm_time))

asc_time = time.asctime()
print(asc_time)
print(type(asc_time))

c_time = time.ctime()
print(c_time)
print(type(c_time))

strf_time = time.strftime("%Y-%m-%d %H:%M:%S",local_time)
print(strf_time)
print(type(strf_time))

strp_time = time.strptime(strf_time,"%Y-%m-%d %H:%M:%S")
print(strp_time)
print(type(strp_time))

mk_time = time.mktime(local_time)
print(mk_time)
print(type(mk_time))
'''
'''
#time.sleep(秒)--->可以使程序暂停指定的秒数，然后继续执行下面的程序
print("倒计时10s开始计时：")
sleep = time.sleep(1)
print("10s")
sleep = time.sleep(1)
print("09s")
sleep = time.sleep(1)
print("08s")
sleep = time.sleep(1)
print("07s")
sleep = time.sleep(1)
print("06s")
sleep = time.sleep(1)
print("05s")
sleep = time.sleep(1)
print("04s")
sleep = time.sleep(1)
print("03s")
sleep = time.sleep(1)
print("02s")
sleep = time.sleep(1)
print("00s")
sleep = time.sleep(1)
print("发射！")
'''
import time
print("倒计时开始：")
for i in range(10,-1,-1):
    time.sleep(1)
    print(i,"s")
print("发射！")
