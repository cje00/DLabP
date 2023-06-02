#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
pd.__version__


# In[3]:


import numpy as np


# In[4]:


pd.__version__


# In[5]:


matrix = np.random.randint(1,10,(2,3))
matrix


# In[8]:


matrix.T   # transpose 


# In[6]:


matrix.ravel()


# In[7]:


matrix.reshape(2,3)


# In[ ]:


# resize vs. reshape

# reshize 에서 추가 요소는 0으로 채워진다


# In[10]:


a = np.random.randint(1,10,(2,6))
a


# In[11]:


a.resize(6,2)
a


# In[16]:


b = np.random.randint(1,10,(2,6))
# 추가요소는 0으로 채워짐 
b.resize((2,10))
b


# In[15]:


# 요소가 12개에서 9개로 줄어듬
c = np.random.randint(1,10,(2,6))
c.resize((3,3))
c


# In[ ]:


# append : 배열의 끝에 값 추가 value or 배열 추가 
# axis = 1 -> 열방향 추가
# axis = 0 -> 행방향 추가 


# In[18]:


ap_a = np.arange(1,10).reshape(3,3)
print('a=', ap_a)
ap_b = np.arange(10,19).reshape(3,3)
print('b=', ap_b)


# In[20]:


# no axis defined
result1 = np.append(ap_a, ap_b)
print(result1)


# In[22]:


# axis = 1   열방향 추가 
result2 = np.append(ap_a, ap_b, axis = 1)
print(result2)


# In[25]:


# axis = 0  행방향 추가 
result3 = np.append(ap_a, ap_b, axis = 0)
print(result3)


# In[26]:


# insert
ins_a = np.arange(1,10).reshape(3,3)
print(ins_a)


# In[27]:


np.insert(ins_a, 4, 999)


# In[28]:


np.insert(ins_a, 1, 999, axis = 0)


# In[ ]:


np.insert(lins, )


# In[29]:


# delete
del_a = np.arange(1,10).reshape(3,3)
print(del_a)


# In[31]:


np.delete(del_a,1)


# In[32]:


np.delete(del_a, 2, axis = 0)


# In[33]:


np.delete(del_a, 1, axis = 1)


# In[ ]:




