
# coding: utf-8

# In[1]:


import re


# In[2]:


pattern=re.compile(r'<HTML>')


# In[6]:


print(pattern.match("<HTML>"))


# In[41]:


pattern=re.compile('a[bcd]+')


# In[42]:


pattern.match('a')


# In[23]:


pattern=re.compile('ab[^a-z]')


# In[25]:


pattern.match('ab@')


# In[48]:


pattern=re.compile('\d[- ]?\d[- ]?\d')


# In[50]:


pattern.match("555555-555")

