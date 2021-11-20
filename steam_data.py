import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

steam_data = pd.read_csv('steamData.csv')
pd.set_option('max_columns', None)
#print(steam_data)

#calculating the total number of players in the dataset
players = steam_data['Player ID']

counts = players.value_counts()
print(counts)

#calculating the total number of unique titles in the dataset
titles = steam_data['Title']

counts2 = titles.value_counts()
print(counts2)


# ﬁlter the data set to only those who have played the games
only_played_games = steam_data.loc[steam_data['Played or just Purchased?'] == "play"]
print(only_played_games)
count3 = only_played_games.value_counts()
print(count3)

# Showing the histogram of cleaned data_set
only_played_games.hist()
plt.show()


# calculate the arithmetic mean of the values of ﬁltered data set
mean_value = only_played_games.groupby(only_played_games['Player ID'])['Played or just Purchased?'].value_counts().mean()

print("the mean is ", mean_value)


# Finding the mode
# What game on Steam has the most players according to this data set? => using mode
game_with_most_players = only_played_games['Title'].mode()
print(game_with_most_players)
print(len(game_with_most_players))


# Top 5 most played games
n = 5
top_five_most_played_games = only_played_games['Title'].value_counts()[:n]
print(top_five_most_played_games)



# Drawing histogram of the top 5 most played games
top_five_most_played_games.hist()
plt.show()

# histogram after adding 'for Sid Meier’s Civilization V' game
top_five_most_played_games.hist()
plt.show()


# Top 5 most played games
n = 5
most_played_games = only_played_games['Title'].value_counts()[:n].index.tolist()
print("The most played game is before", most_played_games)


# Drawing histogram of the top 5 most played games
#st_played_games.hist()
#plt.show()

# adding Sid Meier’s Civilization V game to the top 5 most played games
most_played_games.append("for Sid Meier’s Civilization V")
print("The most played game is", most_played_games)

# histogram after adding 'for Sid Meier’s Civilization V' game
#most_played_games.hist()
#plt.show()


sns.boxplot(x="Title", y="Hours Played", data=steam_data)
plt.show()

# Calculating sum of hours played of the top 5 most played games
n = 5
hours_most_played = only_played_games['Hours Played'].value_counts()[:n]


# Calculating sum of hours played of the top 5 most played games
n = 5
hours_most_played = only_played_games['Hours Played'].value_counts()[:n].index.tolist()
total_hours = 0
for hr in hours_most_played:
    total_hours += hr


# On average, how many hours are spent playing each of the top 5 most played games (according toquestion 9)
length_of_games = only_played_games['Hours Played'].value_counts()[:n].count()
average = total_hours/length_of_games


print("hours", average)



sns.boxplot(y=steam_data["Player ID"], x=steam_data["Hours Played"])
plt.show()

# Calculating the average
#  total number of games we can ask How many ways can we arrange the games into groups of mean size

print(only_played_games.groupby(only_played_games['Player ID'])['Played or just Purchased?'].value_counts().mean())
