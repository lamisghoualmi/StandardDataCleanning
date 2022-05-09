# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:15:16 2022

@author: Benk
"""


import pandas as pd
from pandasql import sqldf
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

#-----------------Belleabeat datat=set-----------------------------
df = pd.read_csv('marketing_data.csv')
df.head()
# Check columns names
for col in df.columns:
    print(col)
# Data Types for our columns
print(df.dtypes)
# clean columns names (remove space)
df.columns = (df.columns.str.strip().str.upper()
              .str.replace(' ', '_')
              .str.replace('(', '')
              .str.replace(')', '')
              )
#------------------Removing duplicated samples (The same observation of differents )-----
duplicateObser = df[df.duplicated()]
LabelsDupObser=duplicateObser.axes[0].tolist()
print('Number of duplicated observations:', duplicateObser.shape[0])
print('List of the duplicated Observations', LabelsDupObser)


#------------------Check percentage of missing values for each variables----
for col in df.columns:
    PercentageMissing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(PercentageMissing *100)))

#------------------Removing variables with more than 50% of missing values----
ThresholdMissVals=.05
pct_null = df.isnull().sum() / len(df)
missing_features = pct_null[pct_null >= ThresholdMissVals].index
df.drop(missing_features, axis=1, inplace=True)
print('missing values removed, new data size:', df.shape)    
#-----------Automatically features with  var=0 -----------
Sdev=df.var(axis=0)
#hist = Sdev.hist()
Sdev=Sdev.sort_values()
NewSdev=Sdev[Sdev.values!=0]
LabelsNonZero=NewSdev.index.values

df1=df[LabelsNonZero]
df=df1
print('Constant features if there any are remove (Var(Feature-i=0)),  new df size:', df.shape) 
#-------------For data with ordinal values---------------
# ----------------- check missfield and spelling error-----------------
OridinalValue=df.MARITAL_STATUS.unique()
print(OridinalValue)
df.drop(df.loc[df['MARITAL_STATUS']=='Absurd'].index, inplace=True)
df['MARITAL_STATUS'] = df['MARITAL_STATUS'].replace(['Alone'],'Single')

#----------Get the statistical description of the numeric variables to get---- 
#----------the variables who have potentials outliers-------------
MarketingDescrib=df.describe()[['INCOME', 'KIDHOME',
      'TEENHOME', 'RECENCY', 'MNTWINES', 'MNTFRUITS',
      'MNTMEATPRODUCTS', 'MNTFISHPRODUCTS', 'MNTSWEETPRODUCTS',
      'MNTGOLDPRODS', 'NUMDEALSPURCHASES', 'NUMWEBPURCHASES',
      'NUMCATALOGPURCHASES', 'NUMSTOREPURCHASES', 'NUMWEBVISITSMONTH']]   
# MarketingDescrib.to_csv('MarketingDescrib.csv')

#--------Based On the desciption file the INCOME variables has outliers------
# Plot the income variables to define the threshold in order to remove 
# the outliers
sns.boxplot(df['INCOME'])
ListOutlierIndex=np.where(df['INCOME']>100000)
df.drop([140,  208,  323,  495,  525,  729,  830,  851, 1241, 1560, 1822,
        1921, 2200],inplace = True)
print('---done---')

#Store the cleanned data
df.to_csv('CleanMarketing_data.csv')

