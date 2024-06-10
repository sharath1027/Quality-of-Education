import re

def calc(name):
    f=open(name)
    l=[]
    for i in f:
        temp_l=[]
        char=''
        num=''
        for j in range(len(i)):
            if(i[j]=="\""):
                continue
            else:
                if(re.match("[a-zA-Z ]",i[j])):
                    char=char+i[j]
                else:
                    if(re.match("^\d*[.,]?\d*$",i[j])):
                        num=num+i[j]
        temp_l.append(char)
        temp_l.append(float(num))
        l.append(temp_l)
    return l

final_list=[]
rating=0
expen=calc("/Users/rahul/Downloads/expen.txt")
schooling=calc("/Users/rahul/Downloads/schooling.txt")
for i in expen:
    list=[]
    rating=0
    for j in schooling:
        if(i[0]==j[0]):
            rating=(float(j[1])/float(i[1]))*1000
    list.append(i[0])
    list.append(rating)
    final_list.append(list)


f=open("final.txt",'w+')
f.write('Country : Quality\n')
for i in final_list:
    f.write(i[0]+':'+str(i[1])+'\n')



    

    
