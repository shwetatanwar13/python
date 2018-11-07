
# coding: utf-8

# In[1]:


import numpy as np


# In[13]:


print('Do you want to roll the dice....[yes/y]')
dec=input()
while dec == 'yes' or dec == 'y':
  output=np.random.randint(1,high=6)
  print(output)
  print('Wanna roll again....[yes/y]')
  dec=input()

