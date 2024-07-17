#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("population.csv")


# In[3]:


data.head(266)


# In[4]:


data.describe


# In[5]:


#List of contries for the graph.
countries_to_plot = ['United States', 'Canada', 'Brazil', 'Japan', 'Germany', 'France']

#Filtering the data frame
filtered_data = data[data['Country Name'].isin(countries_to_plot)]

#Creating the bar chart
plt.bar (filtered_data['Country Name'], filtered_data['2022'])
plt.xlabel ('Country Name')
plt.ylabel ('Population in 2022')
plt.title('Population of selected countries in 2022')
plt.xticks(rotation=45, ha='right') #Rotating the x-axis labels for readability
plt.show()


# In[ ]:




