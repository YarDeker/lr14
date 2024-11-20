import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('education_statistics.csv')

years = list(range(2002, 2015))

ukraine_data = data[data['Country Name'] == 'Ukraine']
usa_data = data[data['Country Name'] == 'United Kingdom']

ukraine_values = ukraine_data.iloc[0, 4:4 + len(years)].replace('..', np.nan).astype(float).values
usa_values = usa_data.iloc[0, 4:4 + len(years)].replace('..', np.nan).astype(float).values

plt.figure(figsize=(10, 5))
plt.plot(years, ukraine_values, label='Ukraine', linestyle='-', color='b')
plt.plot(years, usa_values, label='UK', linestyle='-', color='r')
plt.xlabel('Year')
plt.ylabel('Children out of school, primary')
plt.title('Children out of school, primary (2002-2014)')
plt.legend()
plt.grid()
plt.show()

country = input("Enter country name for bar chart (Ukraine or United Kingdom): ")

if country == 'Ukraine':
    country_data = ukraine_values
    color = 'b'
elif country == 'United Kingdom':
    country_data = usa_values
    color = 'r'
else:
    print("Invalid country name.")
    exit()

plt.figure(figsize=(10, 5))
plt.bar(years, country_data, color=color)
plt.xlabel('Year')
plt.ylabel('Children out of school, primary')
plt.title(f'Children out of school, primary in {country} (2002-2014)')
plt.grid(axis='y')
plt.show()

