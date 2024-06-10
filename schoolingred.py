#!/usr/bin/env python3
import sys
curr_word = None
curr_count = 0
i=1
for line in sys.stdin:
    word,count=line.split(',')
    count=float(count)
    if word==curr_word:
        i=i+1
        curr_count=curr_count+count
    else:
        if curr_word:
            print('{0}\t{1}'.format(curr_word, curr_count/i))
            i=1
        curr_word=word
        curr_count=count
if(curr_word==word):
    print('{0}\t{1}'.format(curr_word, curr_count/i))