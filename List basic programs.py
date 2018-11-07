
# coding: utf-8

# In[1]:


a=int(input("Enter a number :"))
if (a%2 ==0):
    print("Even number")
else:
    print("odd number")


# In[3]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = int(input("Enter the number:"))
new_list=[x for x in a if x<b]
print(a)


# In[10]:


while (True):
 a=int(input("Enter a number:"))
 divisor_list=[x for x in range(1,a+1) if a%x==0]
 print(divisor_list)
 b=input("Enter again..y/n: ")
 if ((b=='y') or (b=='Y')):
    continue
 else:
    break


# In[11]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# In[15]:


a1=set(a)


# In[16]:


b1=set(b)


# In[19]:


c=list(a1.intersection(b1))
c


# In[20]:


import random


# In[23]:


a=random.sample(range(1,30),10)


# In[24]:


a


# In[43]:


a=['a','f','c','f','g']
b=a.copy()


# In[44]:


a.reverse()


# In[45]:


b


# In[46]:


a


# In[51]:


a=[1,2,2,1]
b=a.copy()
a.reverse()
if a==b:
    print("palindrome")
else:
    print("Not Palindrome")


# In[78]:


a='aba'
b=''.join(a[len(a)-x] for x in range(1,len(a)+1))
if a==b:
    print("palindrome")
else:
    print("Not Palindrome")


# In[75]:


for x in range(1,len(a)+1):
    print(a[len(a)-x])


# In[71]:


len(a)


# In[80]:


a='abbc'
a[::-1]


# In[2]:


import random
a=random.randint(1,9)
print(a)
while(True):
  b=input("Enter your guess number between 1 and 9:.Enter exit to quit....")
  if (b=='exit'):
    break
  else:
    b=int(b)
    if(a==b):
     print("Correct guess..")
     break
    elif ((a-b) < -2):
     print("number too high")
    elif ((a-b)>2):
     print("number too high")
    elif (-2<=(a-b)<=2):
     print("You are close")
    


# In[14]:


def fib(number):
 fib =[1,1]
 if number>2: 
    c=2
    while(c<number):
        fib.append(fib[c-1]+fib[c-2])
        c+=1
    return(fib)
 else:
    return(fib[0:number])


# In[17]:


a=fib(3)


# In[18]:


a


# In[20]:


c=[1,2,3,3,4,]
s=set(c)


# In[23]:


s='I am going to give test in an hour'
l=s.split()


# In[25]:


l.reverse()


# In[29]:


rs=''.join(x for x in s)


# In[30]:


rs


# In[31]:


import random


# In[35]:


random.choice('abvcdfg')


# In[36]:


a='11011'
b='101'


# In[37]:


bin_add()

