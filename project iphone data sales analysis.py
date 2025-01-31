#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip3 install plotly')


# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


data = pd.read_csv("apple_products.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.isnull().sum()


# In[7]:


data.describe()


# In[8]:


#Top 10 highest-rated iPhones on Flipkart in India.


# In[9]:


data.head()


# In[11]:


highest_rated = data.sort_values(by = ["Star Rating"],ascending = False)

highest_rated = highest_rated.head(10)


# In[12]:


print(highest_rated['Product Name'])


# In[13]:


print(highest_rated)


# In[14]:


#How many ratings do the highest - rated iPhones on the Flipkart App?


# In[16]:


data.head()               


# In[19]:


iPhones = highest_rated['Product Name'].value_counts()
label = iPhones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, y = counts)
figure.show()


# In[20]:


iPhones = highest_rated['Product Name'].value_counts()
label = iPhones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, y = counts, title = "number of Ratings of Highest Rated iPhones")
figure.show()


# In[21]:


#Relationship between the sale price of iPhones and number of ratings on Flipkart


# In[22]:


data.head()


# In[26]:


get_ipython().system('pip3 install statsmodels')


# In[28]:


figure = px.scatter(data_frame = data, x ="Number Of Ratings", y="Sale Price", size = 'Discount Percentage', trendline = 'ols', title = "relationship between sales price and number of rating")

figure.show()


# There is a negative relationship between the sales of iPhones and the number ofratings. It means iPhones with lower prices are mostly sold in India

# In[29]:


#What is the relationship between the discount percentage and the number of ratings on Flipkart?


# In[30]:


figure = px.scatter(data_frame = data, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount and Number of iPhones")
figure.show()


# In[31]:


#Most expensive and Least expensive


# In[33]:


data.head()


# In[35]:


most_expensive = data.loc[data['Sale Price'].idxmax()]
least_expensive = data.loc[data['Sale Price'].idxmax()]

#display the results
print("Most Expensive Product:")
print(most_expensive)

print("\nLeast Expensive Product:")
print(least_expensive)


# In[ ]:




