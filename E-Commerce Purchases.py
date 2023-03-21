import pandas as pd

data = pd.read_csv("Ecommerce Purchases")
#print(data)

#1. Display Top 10 Rows of The Dataset
print(data.head(10))

#2. Check Last 10 Rows of The Dataset
print(data.tail(10))

#3. Check Datatype of Each Column
print(data.dtypes)

#4. Check null values in the dataset
print(data.isnull)

#5. How many rows and columns are there in our Dataset?
print(f"{data.shape}\n{data.columns}")

#6. Highest and Lowest Purchase Prices.
print(f"{data['Purchase Price'].max()}\n{data['Purchase Price'].min()}")

#7. Average Purchase Price
print(data['Purchase Price'].mean())

#8. How many people have French 'fr' as their Language?
print((data['Language'] == 'fr').value_counts())
print(len(data[data['Language'] == 'fr']))
print(data[data['Language'] == 'fr'].count())

#9. Job Title Contains Engineer
print(data[data['Job'].str.contains('engineer', case = False)].count())

#10. Find The Email of the person with the following IP Address: 132.207.160.22
print(data[data['IP Address']=='132.207.160.22']['Email'])

#11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
print(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)].count())
print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))

#12. Find the email of the person with the following Credit Card Number: 4664825258997302
print(data[data['Credit Card'] == 4664825258997302]['Email'])

#13. How many people purchase during the AM and how many people purchase during PM?
print(data['AM or PM'].value_counts())

#14. How many people have a credit card that expires in 2020?
print(len(data[data['CC Exp Date'].str.contains('/20')]))

#15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)
print(data['Email'].str.split('@').str[1].value_counts().head(5))
