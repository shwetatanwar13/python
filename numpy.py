
# coding: utf-8

# In[ ]:


import numpy as np
list1=[[1,2,3],[2,3,4],[4,5,6]]
list2=np.array(list1)


# In[ ]:


list3=list2-list2


# In[ ]:


list2.


# In[ ]:


list1


# In[ ]:


len(list1)


# In[ ]:


np.expand_dims(list2,axis=1)


# In[ ]:


np.sort(list1)


# In[ ]:


list1=[[7,2,3],[9,3,4],[7,4,6]]
list2=np.array(list1)
list2


# In[ ]:


np.sort(list2)


# In[ ]:


list2[[1,2]]


# In[ ]:


np.random.randint


# In[ ]:


dict={1:2,2:3,5:6,6:5}


# In[ ]:


max(dict.values())


# In[ ]:


max(dict,key=dict.get)


# In[ ]:


i=123
while i
   


# In[ ]:



        


# In[ ]:


list1=[1,2,3]
list2=[1,2,3]
list1.reverse()
list1


# In[ ]:


list1==list2


# In[ ]:


y=str(-121)
list1=[j for j in y]
print(list1)
list2=list1
print(list2)
print(list1)
list1.reverse()
print(list2)
if list1==list2:
 print ("is palindrome")
else:
  print ('not a palindrome')


# In[1]:


i=1121
num=i
rev1=0
while True:
   rem=i%10
   i=i//10
   rev1=rev1*10+rem
   print(i,rem,rev1)
   if i==0:
    break


# In[2]:


i=-12
abs(i)


# In[5]:


x=121
if x in range(-2**31,(2**31)-1):
     negative=False
     if x<0:
        negative=True
     rev=0
     x=abs(x)
     while True:
        rem=x%10
        x=x//10
        rev=rev*10+rem
        if x==0:
         break
     print (-rev if negative else rev)
   else
     print 0


# In[6]:


x=1534236469
if x in range(-2**31,2**31-1):
    print(True)
else:
    print(False)


# In[11]:


list1=[1,1,2]
set1=set(list1)
list1=list(set1)
list1


# In[12]:


class Solution:
    def removeDuplicates(self, nums):
       set1=set(nums)
       list1=list(set1)
       return list1


# In[14]:


s=Solution()
s.removeDuplicates([1,1,2])


# In[24]:


list1=[1,2,3,4,5]
list2=[1,4,6,8,11,12]
for i in list2:
  list1.append(i)
list1.sort()
for i in range(len(list1)-1,-1,-1):
    print(list1[i])


# In[41]:


s='IV'
dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
list1=[]
for i in s:
   list1.append(dict1[i])
sum=0
prev=0
print(list1)
for i in list1[::-1]:
       if i<prev:
        sum=sum-i
       else:
        sum=sum+i
       prev=i
print(sum)
    


# In[71]:


strs= ["flower","flow","flight"]
list3=list(zip(*strs))
print(list3)

            


# In[58]:


for i in set1:
    print (i)


# In[69]:


list3=list(zip(list1,list2,list1))
print(list1)
print(list2)


# In[76]:


list1.sort()
list1[-1]


# In[77]:


str=['abc', 'xyz', 'aba', '1221']
count=0
for i in str:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print (count)   


# In[85]:


list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted(list1,key=lambda x:x[1])


# In[92]:


list3=[1,2,3,4]
list2=list3.copy()


# In[98]:


list2+list1


# In[84]:


help(sorted)


# In[95]:


import itertools as il


# In[105]:


nums=[0,0,1,1,1,2,2,3,3,4]
prev=-1
count=[]
c=1
for i in range(0,len(nums)):
  if nums[i]==prev:
      count.append(i)
  prev=nums[i]
for i in count:
  nums.pop(i-c)
  c+=1
print(len(nums))


# In[106]:


list1=[1,2,3]
list1.reverse()
list1


# In[107]:


A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]


# In[108]:


list1=[1,2,3]
list1[:0]=[4,5,6]


# In[109]:


list1

