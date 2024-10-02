import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a Pandas DataFrame
df = pd.read_csv('car_info.csv')
print(f"Shape of the dataframe: {df.shape}")

# Print the names of the japanese cars having v6 engines
japanese_v6_cars = df[(df['Origin'] == 'Japan') & (df['EngineType'] == 'V6')]
print("Japanese cars with V6 engines:")
print(japanese_v6_cars['Car'])

# Print the car names for which the horsepower data is missing
cars_with_missing_hp = df[df['Horsepower'].isnull()]
print("Cars with missing horsepower data:")
print(cars_with_missing_hp['Car'])

# Print the number of cars having mpg >= 20
cars_with_high_mpg = df[df['MPG'] >= 20]
print(f"Number of cars with MPG >= 20: {len(cars_with_high_mpg)}")

# Print the name of the car which have the highest mpg
car_with_highest_mpg = df[df['MPG'] == df['MPG'].max()]['Car']
print("Car with the highest MPG:")
print(car_with_highest_mpg)

# Print the maximum, minimum, and average of the car weights
print(f"Max car weight: {df['Weight'].max()}")
print(f"Min car weight: {df['Weight'].min()}")
print(f"Average car weight: {df['Weight'].mean()}")

# Drop the rows from the dataframe which have any missing value
df_dropped = df.dropna()
print(f"Shape of the dataframe after dropping rows with missing values: {df_dropped.shape}")

# Create a pie chart showing proportion of cars manufactured in different countries
df['Origin'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proportion of cars manufactured in different countries')
plt.show()

# Create a plot containing two subplots placed vertically
fig, axs = plt.subplots(2)
# Scatter plot showing mpg vs. weight
axs[0].scatter(df['Weight'], df['MPG'])
axs[0].set_xlabel('Weight')
axs[0].set_ylabel('MPG')
axs[0].legend(['MPG vs Weight'])
# Line plot showing mpg vs displacement
axs[1].plot(df['Displacement'], df['MPG'])
axs[1].set_xlabel('Displacement')
axs[1].set_ylabel('MPG')
axs[1].legend(['MPG vs Displacement'])
plt.tight_layout()
plt.show()
