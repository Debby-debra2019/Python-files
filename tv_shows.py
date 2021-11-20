import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

tv_shows = pd.read_csv('IMdB-TV-clean.csv')
pd.set_option('max_columns', None)
print(tv_shows)
rating = tv_shows['averageRating']
print(rating)

#Determining if averageRating column is normally distributed using the empirical rule
mean_rating = np.mean(tv_shows['averageRating'])
print(mean_rating)
std_rating = np.std(tv_shows['averageRating'])
print(std_rating)
within_std_rating = tv_shows.loc[(tv_shows['averageRating'] > mean_rating -std_rating) & (tv_shows['averageRating'] < mean_rating + std_rating)]
print(within_std_rating)
num_pts_within = len(within_std_rating)
print(num_pts_within)
sns.histplot(x = tv_shows['averageRating'])
plt.show()
min_rating = np.min(tv_shows['averageRating'])
print(min_rating)
max_rating = np.max(tv_shows['averageRating'])
print(max_rating)
x = np.linspace(min_rating, max_rating, 1000)
p = stats.norm.pdf(x, mean_rating, std_rating)

plt.plot(x, p, 'k', linewidth = 2)

plt.show()
sns.histplot(tv_shows, x = 'averageRating', stat = 'density', common_norm = False)
plt.show()

#total number of series
num_shows = len(tv_shows['SeriesName'])
print(num_shows)

count = 0
for i in rating:
    if (i > mean_rating):
        count = count + 1
print(count)

#determining the total number of series with crime as the primary genre and rating greater than mean
primary_genre = tv_shows['primary genre']
print(primary_genre)
primary_counts = primary_genre.value_counts()
print(primary_counts)
crime_counts = tv_shows.loc[(tv_shows['primary genre'] == 'Crime') & (tv_shows['averageRating'] > mean_rating)]
print(crime_counts)

#Histogram to determine the most popular primary genre
sns.histplot(x = tv_shows['primary genre'], binwidth = 2)
plt.xticks(rotation = 45)
plt.show()

# Filtering the Top 10
#the best way i could answer number 10 an 11 was plot a violin plot for all the primary genres then concentrate on the top ten that i filtered out
n = 10
top_ten = primary_genre.value_counts()[:n]
print(top_ten)
ax = sns.violinplot(x='primary genre', y='averageRating', data=tv_shows)
plt.xticks(rotation = 45)
plt.show()



