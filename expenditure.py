#!/usr/bin/env python3
import sys
expenditure=[]
for line in sys.stdin:
    words=line.split(',')
    if words[7]=='' or words[7]=='"Flag Codes"':
        continue
    else:
        if(words[4]=='"China'):
            continue
        else:
            i=words[7].strip()
            for j in i:
                if j=='"':
                    continue
                else:
                    print(words[4],',',words[7])