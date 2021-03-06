#!/usr/bin/python
#coding = UFT-8
#python --version 2.7.10
#by_xinlei_han
import os
import re
import math

def count(f):
#receive a string f
# count details in each file
    #lower
    f=f.lower()
    #count tokens
    token_count=0
    token_list=[',','.','/','?','\'','"',':',';','(',')','!','-']
    for token in token_list:
        token_count+=f.count(token)
    #string => list    
    text=[]
    lines=f.strip().split('\n')
    for line in lines:
        text.extend(re.sub(r'[,\./?\'":;()!\-\s]+',' ',line).strip().split())
    #count unique terms
    unique_term=[]
    tf={}
    for i in range(0,len(text)):
        if text[i] in unique_term:
            pass
        else:
            unique_term.append(text[i])
            tf[text[i]]=text.count(text[i])
    return([token_count,tf])

#assignment1 request         
token_num=0
unique_num=0
val_eq1_num=0
val_top30=[]
docs_num=0
#main
results=[]
file_list = os.listdir(os.getcwd())
for file_name in file_list:
    docs_num+=1
    with open(file_name,'r') as f:
        #results is a list in form of[[token_count,tf],..]
        results.append(count(f.read().decode("utf-8-sig").encode("utf-8")))

#calculate answer of request
aggregate={}#unique terms from all file & their freq
#1
for i in results:
    token_num+=i[0]
for i in results:
    for (k,v) in i[1].items():
        if aggregate.get(k, -1) == -1:
           aggregate[k]=v
        else:
           aggregate[k]+=v 

#2
unique_num=len(aggregate)
Nt=0#sum all terms up
for (k,v) in aggregate.items():
        Nt+=v
        if v==1:
            #3
            val_eq1_num+=1
list_top30=sorted(aggregate.iteritems(),key=lambda d:d[1],reverse=True)[0:30]

#4
for (k,v) in list_top30:
    #val_top30[term,TF,IDF,TF*IDF,P]
    DFt=0
    for obj in results:#each obj of result =>a file. obj[1] unique words dict.
        if obj[1].get(k,-1) != -1:
            DFt+=1
    IDF=math.log(docs_num*1.0/DFt,10)
    val_top30.append([k,v,IDF,IDF*v,v*1.0/Nt])

#5
avg_t=token_num*1.0/docs_num

#main end, print start 

print "total_tokens=%s\nunique_terms=%s\nunique_terms_only1=%s\navg_tokens_per_doc=%s" \
          %(token_num,unique_num,val_eq1_num,avg_t)
print '************TOP30*************\n' 
for term in val_top30:
    print term

