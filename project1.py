import pandas as pd

df=pd.read_csv('BIKE DETAILS.csv')

#BASIC OPERATIONS

print("\nFirst 5 rows :\n")
print(df.head())

print("\n\nLast 5 rows :\n")
print(df.tail())

print("\n\nColumn names , data types and shape of dataset:")
print(df.columns)
print(df.dtypes)
print(df.shape)

print("\n\nInformation of the dataset :")
print(df.info())

print("\n\nStatistical data of numeric columns :")
print(df.describe())

print("\n\nAccess specific rows and columns :") #use iloc / loc( for specific columns) 
print(df.iloc[0:3])
print(df.loc[:,['name','owner']])

#DATA CLEANING

print("\n\nMissing or Duplicate values")
print(df.isnull().sum())
print(df.duplicated().sum())

print("\n\nDrop duplicates")
print(df.drop_duplicates(inplace=True))

print("\n\nConvert any columns numerics")
df['km_driven']=df['km_driven'].astype(float)
print(df['km_driven'])

#PRICE ANALYSIS

print("\n\nTop 10 most expensive Bikes :")
print(df.sort_values('selling_price',ascending=False)[['name','selling_price']].head(10))

print("\n\nPrice range of bikes")
print(df['selling_price'].describe())

print("\n\nCommon brands")
print(df['name'].value_counts().head(5))

#GENRAL QUESTIONS

print("\n\nLess driven bike under 75000")
print(df[df['selling_price']<75000][['name','km_driven']].sort_values('km_driven',ascending=False).head(5))

print("\n\nShow the count of bikes by year")
print(df['year'].value_counts().sort_index())

print("\n\nOwner type")
print(df['owner'].value_counts)

print("\n\nAverage price by owner type")
print(df.groupby('owner')['selling_price'].mean())

df.to_csv('BIKE DETAILS_CLEANED.csv',index=False) 