
# coding: utf-8

# In[36]:


A=[1,2,3,4]
B=[]
C=[]


# In[37]:


j=len(A)
for i in range(0,j):
    if A[i]%2==0:
        B.append(A[i])
    else:
        C.append(A[i])
B=B+C
B


# In[38]:


C


# In[31]:


B


# In[58]:


A=['FizzBuzz' if i%3==0 and i%5==0  else 'Buzz' if i%5==0 else 'Fizz' if i%3==0 else str(i) for i in range(1,16)]


# In[59]:


A

