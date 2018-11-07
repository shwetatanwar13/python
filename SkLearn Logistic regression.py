
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[4]:


iris=pd.read_csv('iris.data',header=None,names=['sepal length','sepal width','petal length','petal width','class'])
bezdekIris=pd.read_csv('bezdekIris.data',header=None,names=['sepal length','sepal width','petal length','petal width','class'])


# In[5]:


iris.head()


# In[6]:


bezdekIris.head()


# In[7]:


sns.pairplot(iris,hue='class')


# In[8]:


sns.heatmap(iris.corr())


# In[9]:


print(iris.describe())


# In[11]:


iris.groupby('class').count()


# In[13]:


array = iris.values
array


# In[24]:


X = array[:,0:4]
Y = array[:,4]


# In[37]:


from sklearn import model_selection
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
Y
Y_validation


# In[42]:


from sklearn.linear_model import LogisticRegression


# In[44]:


lm = LogisticRegression()


# In[45]:


lm.fit(X_train,Y_train)


# In[48]:


predictions = lm.predict(X_validation)
predictions


# In[49]:


from matplotlib import pyplot as plt


# In[51]:


plt.scatter(predictions,Y_validation)
plt.ylabel("True Values")
plt.xlabel("Predictions")

