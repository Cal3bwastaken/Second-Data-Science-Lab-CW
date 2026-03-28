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
    df_initial = pd.read_csv(filename, skiprows=[267, 268, 269, 270])

    df_clean = df_initial.drop(['Series Name', 'Series Code', 'Country Code',
                                '2025 [YR2025]'], axis=1)
    df_clean.set_index('Country Name', inplace=True)
    # index is now country name

    df_clean.columns = df_clean.columns.str.replace(r'\s\[.*\]', '',
                                                    regex=True).astype(int)
    # Removes " [YR...]" from all column names at once

    df_clean = df_clean.apply(pd.to_numeric, errors='coerce')
    # Allows all ops to be performed on data, forces it to be numeric

    df_t = df_clean.T

    return df_clean, df_t


def roc_func(df, country, first_year, second_year):
    """
    Finds the rate of change of a DataFrame, you can select a country and the 
    start and end year
    """
    df_roc = np.diff(df[country].loc[first_year:second_year])
    df_roc1 = (df_roc / df[country].loc[first_year:second_year][:-1]) * 100
    mean = df_roc1.mean()
    skew = df_roc1.skew()
    return print('mean:', mean,'skewness:', skew)


def corr_func(df1, df2, country, first_year, second_year):
    """
    finds the corrulation between two DataFrames, you can select a country and 
    the start and end year
    """
    corr_btw_df = df1[country].loc[first_year:second_year].corr(df2[country]
                                                .loc[first_year:second_year])
    return corr_btw_df


GDP_clean, GDP_T = file_read("Global_GDP.csv")

CO2_clean, CO2_T = file_read("CO2.csv")
# %% .describe()

print(GDP_clean.describe())
print(GDP_T.describe())
print(CO2_clean.describe())
print(CO2_T.describe())

# %% base graph looking at global
plt.figure(figsize=(6, 5))
plt.plot(GDP_T['World'], label='global')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('GDP from 1976 - 2024')
plt.legend()
plt.show()


# %% corrulation info

# Use .corr() to find the correlation between two Series
corr_Can = GDP_T['Canada'].corr(CO2_T['Canada'])
print("The corrulation between Canada's GDP and CO2 emissions is ", corr_Can,
      ", Which shows a strong positive corrulation between both indicators")

corr_UK = GDP_T['United Kingdom'].corr(CO2_T['United Kingdom'])
print("The corrulation between UK's GDP and CO2 emissions is ", corr_UK,
      ", Which shows a strong negative corrulation between both indicators")


# %% United Arab Emirates high income

roc_func(GDP_T, 'United Arab Emirates', '2004', '2024')
roc_func(GDP_T, 'United Arab Emirates', '1976', '1996')

roc_func(CO2_T, 'United Arab Emirates', '2004', '2024')
roc_func(CO2_T, 'United Arab Emirates', '1976', '1996')

roc_func(GDP_T, 'United Arab Emirates', '1976', '2024')
roc_func(CO2_T, 'United Arab Emirates', '1976', '2024')

corr_func(GDP_T, CO2_T, 'United Arab Emirates', '2004', '2024')
corr_func(GDP_T, CO2_T, 'United Arab Emirates', '1976', '1996')

# %% China high middle income

roc_func(GDP_T, 'China', '2004', '2024')
roc_func(GDP_T, 'China', '1976', '1996')

roc_func(CO2_T, 'China', '2004', '2024')
roc_func(CO2_T, 'China', '1976', '1996')

roc_func(GDP_T, 'China', '1976', '2024')
roc_func(CO2_T, 'China', '1976', '2024')

corr_func(GDP_T, CO2_T, 'China', '2004', '2024')
corr_func(GDP_T, CO2_T, 'China', '1976', '1996')

# %% Bolivia low middle income
roc_func(GDP_T, 'Bolivia', '2004', '2024')
roc_func(GDP_T, 'Bolivia', '1976', '1996')

roc_func(CO2_T, 'Bolivia', '2004', '2024')
roc_func(CO2_T, 'Bolivia', '1976', '1996')

roc_func(GDP_T, 'Bolivia', '1976', '2024')
roc_func(CO2_T, 'Bolivia', '1976', '2024')

corr_func(GDP_T, CO2_T, 'Bolivia', '2004', '2024')
corr_func(GDP_T, CO2_T, 'Bolivia', '1976', '1996')

# %% Uganda low income
roc_func(GDP_T, 'Uganda', '2004', '2024')
roc_func(GDP_T, 'Uganda', '1976', '1996')

roc_func(CO2_T, 'Uganda', '2004', '2024')
roc_func(CO2_T, 'Uganda', '1976', '1996')

roc_func(GDP_T, 'Uganda', '1976', '2024')
roc_func(CO2_T, 'Uganda', '1976', '2024')

corr_func(GDP_T, CO2_T, 'Uganda', '2004', '2024')
corr_func(GDP_T, CO2_T, 'Uganda', '1976', '1996')

# %% Global
roc_func(GDP_T, 'World', '2004', '2024')
roc_func(GDP_T, 'World', '1976', '1996')

roc_func(CO2_T, 'World', '2004', '2024')
roc_func(CO2_T, 'World', '1976', '1996')

roc_func(GDP_T, 'World', '1976', '2024')
roc_func(CO2_T, 'World', '1976', '2024')

corr_func(GDP_T, CO2_T, 'World', '2004', '2024')
corr_func(GDP_T, CO2_T, 'World', '1976', '1996')

# %% Graph looking at global GDP andCO2 emissions
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(GDP_T['World'], label='World (GDP)', color='blue',
         linestyle='-')
ax1.set_xlabel('Years')
ax1.set_ylabel('GDP', color='blue')

ax2 = ax1.twinx()
ax2.plot(CO2_T['World'], label='World (CO2)', color='green',
         linestyle='-')
ax2.set_ylabel('CO2 Emissions', color='green')

plt.title('Figure 1: GDP and CO2 Emissions Globally (1976 - 2024)')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
           fontsize='small')

plt.show()
# %% Graph comapring CO2 and GDP from chosen countries

fig, ax1 = plt.subplots(figsize=(10, 6))

# Axis 1 GDP
ax1.plot(GDP_T['United Arab Emirates'], label='UAE (GDP)', color='green',
         linestyle='-')
ax1.plot(GDP_T['China'], label='China (GDP)', color='blue', linestyle='-')
ax1.plot(GDP_T['Bolivia'], label='Bolivia (GDP)', color='red', linestyle='-')
ax1.plot(GDP_T['Uganda'], label='Uganda (GDP)', color='orange', linestyle='-')

ax1.set_yscale('log')
ax1.set_xlabel('Years')
ax1.set_ylabel('GDP', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Axis 2 CO2
ax2 = ax1.twinx()
ax2.plot(CO2_T['United Arab Emirates'], label='UAE (CO2)', color='green',
         linestyle='--')
ax2.plot(CO2_T['China'], label='China (CO2)', color='blue', linestyle='--')
ax2.plot(CO2_T['Bolivia'], label='Bolivia (CO2)', color='red',
         linestyle='--')
ax2.plot(CO2_T['Uganda'], label='Uganda (CO2)', color='orange', linestyle='--')

ax2.set_yscale('log')
ax2.set_ylabel('CO2 Emissions', color='black')
ax2.tick_params(axis='y', labelcolor='black')


plt.title('Figure 2: GDP and CO2 Emissions (1976 - 2024)')
# Combine handles and labels for a single legend box
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
           fontsize='small')

plt.tight_layout()
plt.show()
