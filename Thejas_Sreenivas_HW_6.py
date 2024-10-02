import pandas as pd
import matplotlib.pyplot as plt

# Reads the CSV file into a Pandas DataFrame.
df = pd.read_csv('car_info.csv')

# 1. Print the shape of the dataframe
print("1. Shape of the dataframe:", df.shape)

# 2. Print the names of the Japanese cars having v6 engines
japanese_v6_cars = df[(df['origin'] == 'japan') & (df['cylinders'] == 6)]['name'].tolist()
print("\n2. Japanese v6 cars:", japanese_v6_cars)

# 3. Print the car names for which the horsepower data is missing
cars_missing_horsepower = df[df['horsepower'].isnull()]['name'].tolist()
print("\n3. Cars with missing horsepower data:", cars_missing_horsepower)

# 4. Print the number of cars having mpg >= 20
num_cars_mpg_20 = df[df['mpg'] >= 20].shape[0]
print("\n4. Number of cars having mpg >= 20:", num_cars_mpg_20)

# 5. Print the name of the car which has the highest mpg
highest_mpg_car = df[df['mpg'] == df['mpg'].max()]['name'].tolist()
print("\n5. Most fuel-efficient car:", highest_mpg_car)

# 6. Print the maximum, minimum, and average of the car weights
max_weight = df['weight'].max()
min_weight = df['weight'].min()
avg_weight = df['weight'].mean()
print("\n6. minimum weight:", min_weight, ", maximum weight:", max_weight, ", average weight:", avg_weight)

# 7. Drop the rows from the dataframe which have any missing value
df_cleaned = df.dropna()
print("\n7. Shape after removing the missing values:", df_cleaned.shape)

# 8. Create a pie chart showing the proportion of cars manufactured in different countries
country_counts = df['origin'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%')
plt.title('Proportion of Cars Manufactured in Different Countries')
plt.show()

# 9. Create a plot containing two subplots placed vertically
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# i. Scatter plot showing mpg vs. weight
axes[0].scatter(df['mpg'], df['weight'], label='mpg vs. weight', color='blue')
axes[0].set_xlabel('mpg')
axes[0].set_ylabel('weight')
axes[0].legend()

# ii. Line plot showing mpg vs. displacement
axes[1].plot(df['mpg'], df['displacement'], label='mpg vs. displacement', color='red')
axes[1].set_xlabel('mpg')
axes[1].set_ylabel('displacement')
axes[1].legend()

plt.tight_layout()
plt.show()