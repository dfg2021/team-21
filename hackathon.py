#!/usr/bin/env python
# coding: utf-8

# In[145]:


import pandas as pd


# In[146]:


ls


# In[147]:


country = pd.read_csv("FFG_Hackathon_Country_Level_Data.csv")


# In[148]:


country


# In[149]:


country.columns


# In[150]:


country[['Country Name','EN.ATM.CO2E.KT']].sort_values('EN.ATM.CO2E.KT', ascending = False)


# In[151]:


temps = pd.read_csv("annual_csv.csv")
temps


# In[152]:


temps = temps.loc[temps['Source'] == 'GCAG']
temps


# In[153]:


temps = temps.loc[temps['Year'] > 2006]
temps


# In[154]:


ls


# In[155]:


region = pd.read_csv("FFG_Hackathon_Region_Level_Data.csv")
region = region[['Region Name', 'Year','EN.ATM.CO2E.KT']]
region = region.loc[region['Region Name'] == 'World']
region


# In[156]:


import matplotlib.pyplot as plt
import numpy as np


# In[157]:


x = region[['EN.ATM.CO2E.KT']] .to_numpy().flatten()
x


# In[158]:


temps[['Mean']].values


# In[159]:


y = temps[['Mean']] .to_numpy().flatten()
y = np.flip(y)
y


# In[160]:


time=np.linspace(2007,2016, 10)
time


# In[161]:


plt.plot(time,x)
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (10^7 kiloton)')
plt.show()
plt.plot(time,y)
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (Celsius)')
plt.show()


# In[162]:


plt.scatter(x, y)
plt.xlabel('CO2 Emissions (10^7 kiloton)')
plt.ylabel('Temperature Anomaly (Celsius)')


# In[163]:


len(y)


# In[164]:


r = np.corrcoef(x, y)
r


# In[165]:


country


# In[166]:


country = country.loc[country['Year'] == 2016]
country = country[['Country Name','EN.ATM.CO2E.KT', 'EN.POP.DNST']]
country.sort_values('EN.ATM.CO2E.KT', ascending = False)


# In[168]:


country.columns = ['Country', 'Total CO2 Emissions (kt)',  'Population Density (people/sq. km land)']
country = country.sort_values('Total CO2 Emissions (kt)', ascending = False)
country.drop_duplicates(subset = 'Country').head(10)
  


# In[ ]:




