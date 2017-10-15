#!/usr/bin/python
#coding = UFT-8
#python --version 2.7.10
#by_xinlei_han
import os
import re

 #receive a string f
def count(f):

    #count tokens
    token_count=0
    token_list=[',','.','/','?','\'','"',':',';','(',')','!','-']
    for token in token_list:
        token_count+=f.count(token)
    #string => list    
    text=[]
    lines=f.split('\n')
    for line in lines:
        text.extend(line.strip().split(' '))
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


file_list = os.listdir(os.getcwd())
#for file_name in file_list:
#    print(file_name)
with open(file_list[1],'r') as f:
    result=count(f.read().decode("utf-8-sig").encode("utf-8"))
#print(sorted(tf.iteritems(),key=lambda d:d[1],reverse=True))
    print(result[0])
