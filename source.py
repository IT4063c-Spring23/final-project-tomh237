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

# In[2]:


# Start your code here

import numpy as np
import pandas as pd
from scipy.stats import trim_mean
import openpyxl

pd.set_option('display.max_rows', 500)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
plt.style.use("bmh")



# In[22]:


cpi_df = pd.read_excel('CPI Report.xlsx', header = 0)

oil_df = pd.read_excel('Oil prices per barrel.xlsx')

currency_df = pd.read_excel('closing exchange rates.xlsx', header = 0)

#display(
#    print(oil_df.info())
    #print(currency_df.head(5))
#)

x_oil = np.array(oil_df[['Month']]).reshape(-1, 1)
y_oil = np.array(oil_df[['FOB Dollars per Barrel']]).reshape(-1, 1)

x_oil_train, x_oil_test, y_oil_train, y_oil_test = train_test_split(x_oil, y_oil, test_size = 0.25)
oil_regr = LinearRegression()
oil_regr.fit(x_oil_train, y_oil_train)
oil_pred = oil_regr.predict(x_oil_test)

plt.scatter(x = 'Month', y = 'FOB Dollars per Barrel', data = oil_df)
plt.plot(x_oil_test, oil_pred, color = 'r')

plt.show


# In[23]:


x_jpy = np.array(currency_df[['Month']]).reshape(-1, 1)
y_jpy = np.array(currency_df[['USD/JPY Close']]).reshape(-1, 1)

x_jpy_train, x_jpy_test, y_jpy_train, y_jpy_test = train_test_split(x_jpy, y_jpy, test_size = 0.25)
jpy_regr = LinearRegression()
jpy_regr.fit(x_jpy_train, y_jpy_train)
jpy_pred = jpy_regr.predict(x_jpy_test)

plt.scatter(x = 'Month', y = 'USD/JPY Close', data = currency_df)
plt.plot(x_jpy_test, jpy_pred, color = 'r')

plt.show


# In[24]:


x_eur = np.array(currency_df[['Month']]).reshape(-1, 1)
y_eur = np.array(currency_df[['EUR/USD Close']]).reshape(-1, 1)

x_eur_train, x_eur_test, y_eur_train, y_eur_test = train_test_split(x_eur, y_eur, test_size = 0.25)
eur_regr = LinearRegression()
eur_regr.fit(x_eur_train, y_eur_train)
eur_pred = eur_regr.predict(x_eur_test)

plt.scatter(x = 'Month', y = 'EUR/USD Close', data = currency_df)
plt.plot(x_eur_test, eur_pred, color = 'r')

plt.show


# In[25]:


x_gbp = np.array(currency_df[['Month']]).reshape(-1, 1)
y_gbp = np.array(currency_df[['GBP/USD Close']]).reshape(-1, 1)

x_gbp_train, x_gbp_test, y_gbp_train, y_gbp_test = train_test_split(x_gbp, y_gbp, test_size = 0.25)
gbp_regr = LinearRegression()
gbp_regr.fit(x_gbp_train, y_gbp_train)
gbp_pred = gbp_regr.predict(x_gbp_test)

plt.scatter(x = 'Month', y = 'GBP/USD Close', data = currency_df)
plt.plot(x_gbp_test, gbp_pred, color = 'r')

plt.show


# In[26]:


x_cad = np.array(currency_df[['Month']]).reshape(-1, 1)
y_cad = np.array(currency_df[['USD/CAD Close']]).reshape(-1, 1)

x_cad_train, x_cad_test, y_cad_train, y_cad_test = train_test_split(x_cad, y_cad, test_size = 0.25)
cad_regr = LinearRegression()
cad_regr.fit(x_cad_train, y_cad_train)
cad_pred = cad_regr.predict(x_cad_test)

plt.scatter(x = 'Month', y = 'USD/CAD Close', data = currency_df)
plt.plot(x_cad_test, cad_pred, color = 'r')

plt.show


# In[31]:


oil2_df = pd.read_excel('Oil prices per barrel 2.xlsx')
cpi_df.plot(kind = 'line', x = 'Month', figsize = (35, 20))

oil2_df.plot(kind = 'line', x = 'Month', figsize = (35,20))


# In All Plots: Time period of all plots is Jan 2009 to Dec 2019, values are represented by an interger representing days from Jan 1, 1900
# 
# In Plot 1: The cost of oil per barrel in US Dollars (USD) is shown and how the price has changed
# In Plot 2 and 3: The exchange rate at the end of the specified month is shown for USD to Japanese Yen (JPY)[Plot 2] and USD to Euros (EUR)[Plot 3]
# In Plot 4: Cost of standard grocery items are shown by month
# 

# After looking through the data, there are no missing values nor outlying values, therefore no data cleaning was needed for the project

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[36]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

