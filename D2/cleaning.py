#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[47]:


df = pd.read_csv("training.1600000.processed.noemoticon.csv",names=['0','1','2','3','username','tweet'],encoding = "ISO-8859-1")


# In[48]:


df = df[['username','tweet']]


# In[49]:


df = df.groupby(['username']).agg(lambda col: ','.join(col)).reset_index()
#df=df.pivot_table(index=['username'], values=['username'], aggfunc=lambda x: ','.join(x)).reset_index()
#df=df.groupby(['username'])['tweet'].apply(lambda x: ' '.join(x)).reset_index()
#df['tweet'] = df.groupby(['username'])['tweet'].transform(lambda x : ' '.join(x))
df


# In[50]:


df['tweet']=df['tweet'].str.replace('[^a-zA-Z0-9#@]', ' ')
df

