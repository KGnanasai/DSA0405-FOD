import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset creation
data = {
    'Name': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8', 'Player9', 'Player10'],
    'Age': [25, 28, 23, 26, 22, 30, 27, 29, 24, 31],
    'Position': ['Forward', 'Midfielder', 'Defender', 'Forward', 'Midfielder', 'Forward', 'Defender', 'Midfielder', 'Defender', 'Forward'],
    'GoalsScored': [20, 15, 5, 18, 12, 25, 8, 14, 7, 22],
    'WeeklySalary': [10000, 12000, 8000, 15000, 11000, 18000, 9000, 13000, 7500, 20000]
}

df = pd.DataFrame(data)

# Find the top 5 players with the highest number of goals scored
top_goals_players = df.nlargest(5, 'GoalsScored')

# Find the top 5 players with the highest salaries
top_salary_players = df.nlargest(5, 'WeeklySalary')

# Calculate the average age of players
average_age = df['Age'].mean()

# Display the names of players above the average age
above_average_age_players = df[df['Age'] > average_age]['Name']

# Visualize the distribution of players based on their positions using a bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='Position', data=df, palette='viridis')
plt.title('Distribution of Players Based on Positions')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.show()

# Display the results
print("Top 5 Players with the Highest Goals Scored:")
print(top_goals_players[['Name', 'GoalsScored']])
print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players[['Name', 'WeeklySalary']])
print(f"\nAverage Age of Players: {average_age:.2f}")
print("\nPlayers Above the Average Age:")
print(above_average_age_players)
