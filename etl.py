import pandas as pd
import ppd

data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df1 = pd.read_csv("sales_data_sample.csv", encoding='ISO-8859-1')
print(df1)

# check for missing values
print(df1.isnull().sum())

# Handle missing value

df1.fillna(0,inplace= True)
print(df1.isnull().sum())

# Handle duplicates

df1.drop_duplicates(inplace= True)
print(df1)

#Convert 'JoinDate' to DateTime
print(df1["ORDERDATE"])

df1["ORDERDATE"] = pd.to_datetime(df1["ORDERDATE"])
print(df1["ORDERDATE"])

# Filter all the shipped orders

df1_shipped = df1[df1['STATUS'] == "Shipped"]
print((df1_shipped))

#  Total order by City
df1_city = df1.groupby("CITY")['ORDERNUMBER'].count()
print(df1_city)

# Tenure of orders place
df1["ORDERDATE"] = pd.to_datetime(df1["ORDERDATE"])
df1_order_tenure_days = (pd.Timestamp("today") - df1["ORDERDATE"]).dt.days
print(df1_order_tenure_days)









