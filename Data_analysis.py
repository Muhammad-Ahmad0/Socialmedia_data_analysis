#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as mplt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('realDonaldTrump_poll_tweets.csv')
df


# In[5]:


Sorted_df = df.sort_values(by='created_at',ascending=True)
x = Sorted_df['created_at']
x


# In[6]:


y=Sorted_df['id']
y


# In[7]:


get_ipython().run_line_magic('pylab', '')
import mplcursors
mplt.plot(x,y)
mplcursors.cursor(hover=True)
mplt.show()


# In[12]:


import mplcursors
fig = mplt.figure(figsize=(18,8))
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_title('Trumps poll tweet')
mplcursors.cursor(hover=True)
mplt.show()


# In[13]:


fig.savefig('tweetplot.png')


# In[ ]:




