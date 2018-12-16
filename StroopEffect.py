# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:09:03 2018

@author: praddyumna naik
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Creating dataframe
stroop_data = pd.read_csv('stroopdata.csv')
print(stroop_data.head())
print('-'*60)

# Descriptive stats calculation of data
stroop_data_summary = stroop_data.describe()
print(stroop_data_summary)
print('-'*60)

# Measures of Central Tendency and Variability 
mean_congruent = stroop_data_summary['Congruent'].loc['mean']
mean_incongruent = stroop_data_summary['Incongruent'].loc['mean']
std_congruent = stroop_data_summary['Congruent'].loc['std']
std_incongreunt = stroop_data_summary['Incongruent'].loc['std']

# Measures of Central Tendency and Variability 
print("\nMean Congruent reading times: {:.2f} s".format(mean_congruent))
print("\nMean Incongruent reading times: {:.2f} s".format(mean_incongruent))
print("\nStandard deviation of Congruent reading times: {:.2f} s".format(std_congruent))
print("\nStandard deviation of Incongruent reading times: {:.2f} s".format(std_incongreunt))
print('-'*60)

# Visulization
stroop_data.plot.box()
print(plt.ylabel('Reading times in seconds'))
print(plt.show())
print('-'*60)

# Calculation of difference between both independant variable and its respective stats data

difference = stroop_data['Congruent'] - stroop_data['Incongruent']
difference_summary = difference.describe()
mean_difference = difference_summary.loc['mean']
std_difference = difference_summary.loc['std']

print("\nMean of the difference is {:.4f} s".format(mean_difference))
print("\nStandard deviation of the difference is {:.4f} s".format(std_difference))
print('-'*60)


# Degree of freedom Calculation (dfr)
n = 24
dfr = n-1
print("Degree of Freedom : {}".format(dfr))
print('-'*60)


# T test Calculation
sd = std_difference / np.sqrt(24)
t_stats = mean_difference / sd
print("\nt-statistic for the test is {:.4f}".format(t_stats))
print('-'*60)
# t- critical value calculation

t_critical = (stats.t.ppf(q=0.025, df= dfr), stats.t.ppf(q=0.975, df =dfr))
print("t_critical values at alpha = 0.05 for two-tailed T test:\n ({:.4f}, {:.4f}).".format(*t_critical))
print('-'*60)

# P Value Calculation
pval = stats.t.cdf(t_stats, dfr)*2
print("P value is: {:.4e}".format(pval))
print('-'*60)
# we can directly calculate the values through scipy
print(stats.ttest_rel(stroop_data['Congruent'],stroop_data['Incongruent']))
print('-'*60)

# Calculation of Confidence interval

ci = stats.norm.interval(0.95, loc = mean_difference, scale = sd)
print("Confidence Intervel : {}".format(ci))


