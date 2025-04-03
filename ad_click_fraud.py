import pandas as pd

df = pd.read_csv("ad_click_data.csv")

df.ffill(inplace=True) #Missing DataApply Forward Fill for time-structured numerical data

df.fillna({
    'ip_address' : 'Unknown',
    'user_agent' : 'Unknown User Agent'
}, inplace=True)

print(df.head())            # shows the first 5 rows
print(df.info())            # how many columns and rows, data type, if there is missing values
print(df.describe())        # count, standard deviantion, min/max, 25th, 50th(median), 75th percentile
print(df.isnull().sum())    # Check for missing values

