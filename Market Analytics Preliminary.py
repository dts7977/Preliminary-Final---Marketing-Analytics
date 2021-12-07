#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
pd.set_option("display.max.columns", None)


# In[3]:


df=pd.read_csv('subscribers.csv')
df1=pd.read_csv('channel_spend_graduate.csv')
df2=pd.read_csv('CQM_engagement_4mo_en.csv')


# In[4]:


#dataframe
df.head(50)


# In[35]:


#male numbers
len(df[df['male_TF']==False])


# In[11]:


df.describe()


# In[28]:


#trials completed/current_subs
subst=df[df['current_sub_TF']==True]
subsf=df[df['current_sub_TF']==False]
subnum=df['current_sub_TF'].value_counts()

trialscompt=df[df['trial_completed']==True]
trialscompf=df[df['trial_completed']==False]

trialnum=df['trial_completed'].value_counts()


# In[ ]:


subst.drop(['weekly_consumption_hour','num_ideal_streaming_services','age'],axis=1,inplace=True)


# In[29]:


subst.describe(include=object)


# In[30]:


subsf.describe(include=object)


# In[33]:


subst=subsf[subsf['account_creation_date'] > 2019-06-01]


# In[ ]:





# In[22]:


#Subscribers
subst.drop(['weekly_consumption_hour','num_ideal_streaming_services','age'],axis=1,inplace=True)



# In[24]:


subst.describe()


# In[25]:


subsf.drop(['subid','num_weekly_services_utilized','weekly_consumption_hour','num_ideal_streaming_services','age'],axis=1,inplace=True)


# In[27]:


#Subscribers
subst.describe()


# In[26]:


#Non-subscribers
subsf.describe()


# In[ ]:





# In[8]:


subg=['True','False']
plt.bar(subg,subnum)
plt.title('Current Sub (T/F)')
plt.show()


# In[9]:


plt.bar(subg,trialnum)
plt.title('Trial Completed (T/F)')

plt.show()


# In[16]:


#useful information about our dataset
df.describe(include=object)


# In[86]:


x=df.value_counts(df['preferred_genre'])

xx=df.value_counts(df['cancel_date'],ascending=True).head(50)
#understand why cancel date was high
dfgroup=df.groupby('account_creation_date')
y=dfgroup.get_group('2020-02-29 19:26:26').head(31)
y.describe(include=object)


# In[10]:


#bar graph of comedy layed out
valuegenre=df['preferred_genre'].value_counts()
valuegenrelist=['comedy','drama','regional','international','other']

plt.bar(valuegenrelist,valuegenre)
plt.title('Channel Popularity')
plt.show()


# In[ ]:





# In[75]:


yy=dfgroup.get_group('2019-07-01 00:00:00')
df.describe()


# In[28]:


#dataframe1
df1.head(50)


# In[108]:


df1['channel'].value_counts()


# In[25]:


df1.describe(include=object)


# In[34]:


bingcount=df1.loc[df1['channel'] == 'bing', 'spend_AED'].sum()
searchcount=df1.loc[df1['channel'] == 'search', 'spend_AED'].sum()
displaycount=df1.loc[df1['channel'] == 'display', 'spend_AED'].sum()
facebookcount=df1.loc[df1['channel'] == 'facebook', 'spend_AED'].sum()
youtubecount=df1.loc[df1['channel'] == 'youtube', 'spend_AED'].sum()

countlist=[bingcount,searchcount,displaycount,facebookcount,youtubecount]
namelist=['bing','search','display','facebook','youtube']
plt.bar(namelist,countlist)
plt.title('Channel spend')
plt.show()

youtubecount


# In[121]:


#bar graph of a attribution_survey (finding of streaming service)
attributioncounts=df['attribution_survey'].value_counts()
attributioncounts


# In[ ]:





# In[36]:


x1=df1.value_counts(df1['channel'])
x1


# In[39]:


#dataframe2 - not sure if this is correct
df2.head(50)


# In[85]:


df2.describe()


# In[56]:


df2.value_counts(df2['access_code'],ascending=False).head(50)


# In[ ]:


df2group=df2.groupby('access_code')
df2group.get_group('1SFXNN2U')


# In[ ]:





# In[ ]:




