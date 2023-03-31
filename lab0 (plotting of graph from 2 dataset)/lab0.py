#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets dir(datasets)


# In[2]:


from sklearn import datasets


# In[3]:


dir(datasets)


# In[4]:


iris=datasets.load_iris()


# In[5]:


dir(iris)


# In[6]:


iris['feature_names']


# In[7]:


iris['target']


# In[8]:


iris["data"][0:5]


# In[9]:


iris['target_names']


# In[10]:


iris['filename']


# In[11]:


n_sample, n_features = iris.data.shape


# In[12]:


n_sample


# In[13]:


n_feature


# In[14]:


n_features


# In[15]:


diabetes=datasets.load_diabetes()


# In[16]:


dir(diabetes)


# In[17]:


diabetes['feature_names']


# In[18]:


diabetes.data


# In[20]:


n_sample, n_features = diabetes.data.shape


# In[21]:


n_sample, n_features = diabetes.data.shape


# In[22]:


n_sample


# In[23]:


diabetes.feature_names.bmi


# In[24]:


diabetes.data


# In[25]:


diabetes['feature_names'][2]


# In[26]:


from matplotlib import pyplot as plt 


# In[27]:


diabetes.data.bmi


# In[28]:


diabetes["data"]


# In[29]:


x = diabetes["data"][0]


# In[30]:


x


# In[31]:


x = diabetes["data"]['bmi']


# In[32]:


x = diabetes["data"]["bmi"]


# In[33]:


x = diabetes["data"]


# In[34]:


x


# In[35]:


diabetes["data"][0]


# In[36]:


diabetes["data"][0][0]


# In[37]:


for x in diabetes["data"]
    print x


# In[38]:


for x in diabetes["data"]


# In[39]:


[row[0] for row in diabetes["data"]]


# In[40]:


x = [row[0] for row in diabetes["data"]]


# In[41]:


y = [row[1] for row in diabetes["data"]]


# In[42]:


x


# In[43]:


y


# In[44]:


plt.plot(x,y)    


# In[45]:


plt.title("Line graph")    


# In[46]:


plt.scatter(x, y)


# In[47]:


x = [row[4] for row in diabetes["data"]]


# In[48]:


y = [row[5] for row in diabetes["data"]]


# In[49]:


plt.scatter(x, y)


# In[50]:


plt.show()


# In[ ]:




