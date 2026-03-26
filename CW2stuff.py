#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:32:54 2026

@author: calebpalluotto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def file_read(filename):
    """
    Reads a CSV file, returns two DataFrames, the one with years as the columns 
    and the other has countries as the columns
    please enter the correct path when using this fucntion
    """
    df_initial = pd.read_csv(filename,skiprows=[267,268,269,270])
    
    df_clean = df_initial.drop(['Series Name', 'Series Code','Country Code',
                                '2025 [YR2025]'],axis=1)
    df_clean.set_index('Country Name', inplace=True)
    # index is now country name
    
    df_clean.columns = df_clean.columns.str.replace(r'\s\[.*\]', '', 
                                                    regex=True).astype(int)
    # Removes " [YR...]" from all column names at once
    
    df_clean = df_clean.apply(pd.to_numeric, errors='coerce')
    # Allows all ops to be performed on data, forces it to be numeric
    
    df_t = df_clean.T
    
    return df_clean, df_t


GDP_clean, GDP_T = file_read("/Users/calebpalluotto/Downloads/Global_GDP.csv")

CO2_clean, CO2_T = file_read("/Users/calebpalluotto/Downloads/CO2.csv")
# %%


print(GDP_clean.describe())
print(GDP_T.describe())
print(CO2_clean.describe())
print(CO2_T.describe())

# %%
# base graph looking at global
plt.figure(figsize=(6,5))
plt.plot(GDP_T['World'], label = 'global')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('GDP from 1976 - 2024')
plt.legend()
plt.show()

# %%
# GDP only
plt.figure(figsize=(6,5))
plt.plot(GDP_T['Canada'], label = 'Canada')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('GDP from 1976 - 2024')
plt.legend()
plt.show()



# %%
# Canada GDP and CO2
plt.figure(figsize=(6,5))
plt.plot(GDP_T['Canada'], label = 'Canada GDP')
plt.twinx(CO2_T['Canada'])
plt.plot(CO2_T['Canada'], label = 'Canada CO2')
plt.xlabel('Years')
plt.ylabel('GDP')
#plt.yscale('log')
plt.title('GDP from 1976 - 2024')
plt.legend()
plt.show()

# %%

# Use .corr() to find the correlation between two Series
corr_Can = GDP_T['Canada'].corr(CO2_T['Canada'])
print("The corrulation between Canada's GDP and CO2 emissions is ",corr_Can,
      ", Which shows a strong positive corrulation between both indicators")

corr_UK = GDP_T['United Kingdom'].corr(CO2_T['United Kingdom'])
print("The corrulation between UK's GDP and CO2 emissions is ",corr_UK,
      ", Which shows a strong negative corrulation between both indicators")

# %%


recent_Can = GDP_T['Canada'].loc['2004':'2024'].corr(CO2_T['Canada'].loc
                                                     ['2004':'2024'])

recent_UK = GDP_T['United Kingdom'].loc['2004':'2024'].corr(
    CO2_T['United Kingdom'].loc['2004':'2024'])

print("the corrulation in Canada between 2004-24", recent_Can)

print("the corrulation in UK between 2004-24", recent_UK)

old_Can = GDP_T['Canada'].loc['1976':'1996'].corr(CO2_T['Canada'].loc
                                                     ['1976':'1996'])

old_UK = GDP_T['United Kingdom'].loc['1976':'1996'].corr(
    CO2_T['United Kingdom'].loc['1976':'1996'])

print("the corrulation in Canada between 1976-96", old_Can)

print("the corrulation in UK between 1976-96", old_UK)

# %%

#Rate of Change GDP Canada
GDP_Can_Diff_r = np.diff(GDP_T['Canada'].loc['2004':'2024'])
GDProc_Can_r = (GDP_Can_Diff_r / GDP_T['Canada'].loc['2004':'2024'][:-1]) * 100
print(GDProc_Can_r.mean())

GDP_Can_Diff_o = np.diff(GDP_T['Canada'].loc['1976':'1996'])
GDProc_Can_o = (GDP_Can_Diff_o / GDP_T['Canada'].loc['1976':'1996'][:-1]) * 100
print(GDProc_Can_o.mean())


# ROC GDP UK
GDP_UK_Diff_r = np.diff(GDP_T['United Kingdom'].loc['2004':'2024'])
GDProc_UK_r = (GDP_UK_Diff_r / GDP_T['United Kingdom'].loc['2004':'2024']
               [:-1]) * 100
print(GDProc_UK_r.mean())

GDP_UK_Diff_o = np.diff(GDP_T['United Kingdom'].loc['1976':'1996'])
GDProc_UK_o = (GDP_UK_Diff_o / GDP_T['United Kingdom'].loc['1976':'1996']
               [:-1]) * 100
print(GDProc_UK_o.mean())


#Rate of Change CO2 Canada
CO2_Can_Diff_r = np.diff(CO2_T['Canada'].loc['2004':'2024'])
CO2roc_Can_r = (CO2_Can_Diff_r / CO2_T['Canada'].loc['2004':'2024'][:-1]) * 100
print(CO2roc_Can_r.mean())

CO2_Can_Diff_o = np.diff(CO2_T['Canada'].loc['1976':'1996'])
CO2roc_Can_o = (CO2_Can_Diff_o / CO2_T['Canada'].loc['1976':'1996'][:-1]) * 100
print(CO2roc_Can_o.mean())


# ROC CO2 UK
CO2_UK_Diff_r = np.diff(CO2_T['United Kingdom'].loc['2004':'2024'])
CO2roc_UK_r = (CO2_UK_Diff_r / CO2_T['United Kingdom'].loc['2004':'2024']
               [:-1]) * 100
print(CO2roc_UK_r.mean())

CO2_UK_Diff_o = np.diff(CO2_T['United Kingdom'].loc['1976':'1996'])
CO2roc_UK_o = (CO2_UK_Diff_o / CO2_T['United Kingdom'].loc['1976':'1996']
               [:-1]) * 100
print(CO2roc_UK_o.mean())


