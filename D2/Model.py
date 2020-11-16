#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd


# In[2]:


df = pd.read_csv("cleaned.csv",encoding = "ISO-8859-1", index_col=0, nrows=50000)
df


# In[3]:


tfidfvectorizer = TfidfVectorizer(analyzer='word' , stop_words='english')


# In[4]:


X = tfidfvectorizer.fit_transform(df['tweet'])


# In[5]:


kmeans = KMeans(n_clusters=50).fit(X)


# In[6]:


kmeans.labels_


# In[7]:


df['cluster']=kmeans.labels_


# In[8]:


df


# In[9]:


df0=df[df['cluster']==0]


# In[10]:


df0


# In[12]:


df0=df0.to_csv('exp1.csv')


# In[ ]:




