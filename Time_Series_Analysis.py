#!/usr/bin/env python
# coding: utf-8

# Time Series Analysis:
# --------------------------------
# 
# 
# 1) Helpful in Tracking changes over time. 
# 2) Helpful in Analyzing Trends, Patterns etc to make better future predictions. 
# 
# Usage in Different Industries: 
# --------------------------------------------
# 1) Finance: Tracking stock prices, Profits over time.
# 2) Retail: Tracking Sales Data
# 
# 

# In[1]:


import pandas as pd 
import plotly.express as px 


# In[2]:


df=pd.read_csv('C:/Users/WIN11/Sales_OrgA.csv')


# In[3]:


# Gathering the information

df.info()


# In[4]:


df['Date']=pd.to_datetime(df['Date'])


# In[5]:


df.info()


# In[6]:


# Resampling Data 

df.resample('M',on='Date').sum()


# In[7]:


# Identifying changes in sales by using shift method 

df['Prev_Sale']=df['Sales'].shift(1)


# In[8]:


df['Change in Sale']=df['Sales'] - df['Prev_Sale']


# In[9]:


df['Change in Sale (%)'] = df['Change in Sale'] / df['Sales']*100


# In[10]:


df


# In[11]:


df['Change in Sales(diff)']=df['Sales'].diff()


# In[12]:


df


# In[13]:


df['Change in Sales(diff) (%)'] = df['Change in Sales(diff)'] / df['Sales'] * 100


# In[14]:


df


# In[15]:


df['Sales'].rolling(2).mean()


# In[16]:


df['RollingAverage']= df['Sales'].rolling(2).mean()


# In[17]:


df

