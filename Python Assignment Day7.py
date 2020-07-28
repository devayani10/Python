#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dict= {port1={21: "FTP",22: "SSH",23:"telnet",80:"HTTP"}
port2= {"FTP":21,"SSH":22,"TELNET":23,"HTTP":80}}
dict = {value: key for key, value in dict.items()}
print(dict)


# In[ ]:


list1=input()
list1=[]
for i in range(0,len(list1)):
    list1.append(list1[i][0]+list1[i][1])
    print(list1)


# In[ ]:


x=(1,2,3), [1,2] 
y=['a','hit','less']
x=list(input())
y=len(x)
res=[]
for i in range(0,y):
    for j in range(0,len(x[i])):
        res.append(x[i][j])
print(res)


# In[ ]:




