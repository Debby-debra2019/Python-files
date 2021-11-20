import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

print('you have the necessary packages!')

#All your code should go here:

movie_data = pd.read_csv("IMDb-clean.csv")

print(movie_data.columns)


group1 = movie_data['allgenders_0age_avg_vote']
print(group1)
group2 = movie_data['allgenders_0age_votes']
print(group2)
group3 = movie_data['allgenders_18age_avg_vote']
print(group3)
group4 = movie_data['allgenders_18age_votes']
print(group4)
group5 = movie_data['allgenders_30age_avg_vote']
print(group5)
group6 = movie_data['allgenders_30age_votes']
print(group6)
group7 = movie_data['allgenders_45age_avg_vote']
print(group7)
group8 = movie_data['allgenders_45age_votes']
print(group8)

fig = plt.figure()
ax = fig.add_subplot(111)
x = movie_data['year']
y = movie_data['avg_vote']
ax.scatter(x,y)
fig.savefig('filename.png', bbox_inches = 'tight')
plt.xticks(rotation = 45)
plt.show()

sns.histplot(x = movie_data['duration'])
plt.xticks(rotation = 45)
plt.show()
duration_mean = np.mean(movie_data['duration'])
print(duration_mean)
duration_median = np.median(movie_data['duration'])
print(duration_median)

sns.countplot(x = movie_data['language'])
plt.xticks(rotation = 45)
plt.show()

sns.scatterplot(x = movie_data['year'], y = movie_data['avg_vote'], hue = movie_data['genre'], palette = 'Paired')
plt.show()

sns.scatterplot( x=movie_data['males_allages_avg_vote'], y=movie_data['females_allages_avg_vote'], hue=movie_data['genre'], palette = 'Paired')
plt.plot(range(1,10),range(1,10),color='red')
plt.show()


