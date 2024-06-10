#!/usr/bin/env python3
import sys

years=[]
for line in sys.stdin:
    j=1
    words=line.split(',')
    for i in range(1,len(words)):
        temp_arr=[]
        d=dict()
        l=[]
        if words[6] not in d: 
            l.append([words[6],words[8]])
            temp_arr.append(words[5][1:((len(words[5]))-1)])
            temp_arr.append(l)
    years.append(temp_arr)

for i in years:
    print(i[0],',',i[1][0][1])
    #print('{0}\t{1}'.format(i[0], i[1][0][1]))
