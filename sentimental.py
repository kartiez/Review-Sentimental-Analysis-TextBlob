#!/usr/bin/env python
# coding: utf-8

# In[10]:


from textblob import TextBlob as tb
import numpy as np
import pandas as pd


# In[35]:


df = pd.read_excel('Data.xlsx')
df.head()


# In[51]:


reviews = df.iloc[:,9]
reviews[4]


# In[49]:


blob = tb(reviews[2])
print(format(blob.sentiment))


# In[47]:


for i, review in enumerate(reviews):
    blob = tb(review)
    if blob.sentiment.polarity>0.1:
        df['polarity'][i] = 'Positive'
    elif blob.sentiment.polarity<-0.1:
        df['polarity'][i] = 'Negative'
    else:
        df['polarity'][i] = 'Neutral'


# In[48]:


df


# In[55]:


df.to_excel('tim_data.xlsx', index = False)


# In[ ]:




