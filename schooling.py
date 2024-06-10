#!/usr/bin/env python3
import sys
for line in sys.stdin:
    words=line.split(',')
    if words[8]=='' or words[5]=='"Time"':
        continue
    else:
        if(words[5]=='"China'):
            continue
        else:
            print(words[5],',',words[8])