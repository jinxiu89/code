#!/usr/bin/env python3
from sys import argv
a=3500
sj=0.165
def count(*args):
    for i in args:
        try:        
            gz=int(i[1])
            bx=gz*sj
            yzs=gz-bx-a
            if yzs < 0:
                 sds=0
            elif yzs <= 1500 :
                 sds=yzs*0.03-0
            elif yzs > 1500 and yzs < 4500:
                 sds=yzs*0.1-105
            elif yzs > 4500 and yzs < 9000:
                 sds=yzs*0.2-555
            elif yzs > 9000 and yzs < 35000:
                 sds=yzs*0.25-1005
            elif yzs > 35000 and yzs < 55000:
                 sds=yzs*0.30-2755
            elif yzs > 55000 and yzs < 80000:
                 sds=yzs*0.35-5505
            elif yzs > 80000:
                 sds=yzs*0.45-13505
            shgz=format(gz-bx-sds,'.2f')
            print("{}:{}".format(i[0],shgz))
        except Exception as e:
            print(e)
arg=argv
list=argv[1:]
for i in list:
    list=i.split(":")
    count(list)


