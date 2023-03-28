#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# In[35]:


# Start your code here

import pandas as pd
from scipy.stats import trim_mean
import openpyxl

pd.set_option('display.max_rows', 500)

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
plt.style.use("bmh")

cpi_df = pd.read_excel('CPI Report.xlsx', header = 0)

oil_df = pd.read_excel('Oil prices per barrel.xlsx')

currency_df = pd.read_excel('closing exchange rates.xlsx', header = 0)

oil_df.plot(kind = 'line', x = 'Month')
currency_df.plot(kind = 'scatter', x = 'Month', y = 'USD/JPY Close')
currency_df.plot(kind = 'scatter', x = 'Month', y = 'EUR/USD Close')
cpi_df.plot(kind = 'line', x = 'Month')
plt.show


# In All Plots: Time period of all plots is Jan 2009 to Dec 2019
# 
# In Plot 1: The cost of oil per barrel in US Dollars (USD) is shown and how the price has changed
# In Plot 2 and 3: The exchange rate at the end of the specified month is shown for USD to Japanese Yen (JPY)[Plot 2] and USD to Euros (EUR)[Plot 3]
# In Plot 4: Cost of standard grocery items are shown by month

# After looking through the data, there are no missing values nor outlying values, therefore no data cleaning was needed for the project

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

