import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from lmfit import Model

def fitting_function(x,m,b):
    #This is called a python function. Is it a chunk of code we give a
    #name to so that we can use it over and over again. It is JUST LIKE
    #a mathematical function. When we want to use this code, we must provide
    #the function name (fitting_function) and values for its inputs

    return m*x+b
    #return A*(np.exp(b*x)) + C

    #In this case, we are going to start by fitting a LINE to some data so we
    #RETURN the equation for a line.

#Write your commands here:

all_seasons = pd.read_csv('all_seasons.csv')
pd.set_option('max_columns', None)
print(all_seasons)
nba_salary = pd.read_csv('NBA_season1718_salary.csv')
pd.set_option('max_columns', None)
print(nba_salary)
season2017_18 = all_seasons.loc[all_seasons['season'] == '2017-18']
print(season2017_18)
merge_data = nba_salary.merge(season2017_18, on = 'player_name')
print(merge_data)

X = merge_data['pts']
Y = merge_data['season17_18']
linear_model = Model(fitting_function, independent_vars=['x'])
result = linear_model.fit(Y, x=X, m=3,b=2)
print(result.fit_report())
r2 = 1 - result.residual.var() / np.var(Y)
print(r2)

plt.figure()
sns.scatterplot(x=X,y=Y)
sns.lineplot(x=X,y=result.best_fit)
plt.show()

# Modify the code to fit to the function Ae^(bx) + C
def fitting_function2(x,A,b,C):
    return A*(np.exp(b*x)) + C
linear_model2 = Model(fitting_function2, independent_vars=['x'])
result2 = linear_model2.fit(Y, x=X, A=1,b=1, C=2)
print(result2.fit_report())
r2 = 1 - result2.residual.var() / np.var(Y)
print(r2)

