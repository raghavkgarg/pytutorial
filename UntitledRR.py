import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.__version__
sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])
sales.head()
sales['unit price'].describe()
sales.dtypes
customers = sales[['name','ext price','date']]
customers.head

customer_group = customers.groupby('name')
customer_group.size()
sales_totals = customer_group.sum()
sales_totals.sort(columns='ext price').head()

my_plot = sales_totals.plot(kind='bar')
