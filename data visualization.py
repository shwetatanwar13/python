
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


pwd


# In[7]:


df=pd.read_csv('biostats.csv')
df


# In[12]:


sns.barplot(df['Sex'],df['Weight'],hue=df['Age'])


# In[15]:


sns.countplot('Sex',data=df)


# In[20]:


sns.boxplot('Sex','Height',data=df,color='green')


# In[28]:


sns.boxplot('Sex','Height',data=df,hue='Sex')


# In[32]:


sns.violinplot('Sex','Height',data=df)


# In[34]:


ds=pd.read_csv('airtravel.csv')
ds


# In[35]:


sns.violinplot('Month','1958',data=ds)


# In[37]:


df=sns.load_dataset('exercise')
df


# In[53]:


sns.boxplot(x='diet',y='pulse',data=df,hue='kind',palette='rainbow',linewidth=2)


# In[61]:


sns.violinplot(x='kind',y='pulse',data=df)


# In[67]:


sns.stripplot(x='diet',y='pulse',data=df,hue='kind',jitter=True)


# In[70]:


sns.swarmplot(x='diet',y='pulse',data=df,color='black')
sns.violinplot(x='diet',y='pulse',data=df)


# In[71]:


df


# In[72]:


ds=df.corr()


# In[74]:


sns.heatmap(df.corr(),)


# In[83]:


ds1=df.pivot_table('pulse','time','id')
ds2=df.pivot_table('pulse','time','kind')
ds2


# In[85]:


sns.heatmap(ds2,annot=True,cmap='coolwarm')


# In[86]:


sns.countplot(x='diet',data=df)

