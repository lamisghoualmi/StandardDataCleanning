# Standard Data Cleaning

This file contains a basic data cleaning pipeline that can be applied to a wide range of datasets. The data cleaning process includes the following steps:

## Steps

- **Check column names**

- **Inspect data types** for all variables

- **Clean variable names**
  - Remove spaces
  - Correct misspellings

- **Remove duplicate records**

- **Calculate the percentage of missing values** for each variable

- **Drop variables with excessive missing values**
  - Remove variables with missing values exceeding a predefined threshold  
  - The threshold is dataset-specific

- **Remove features with low variance**
  - Features with very low variance contribute little to distinguishing between samples and are often irrelevant

- **Identify ordinal variables**
  - Check for misspellings and inconsistent entries
  - Standardize categories

- **Isolate numeric variables**
  - Generate descriptive statistics
  - Identify potential outliers
  - Visualize suspected variables to determine thresholds for outlier removal
