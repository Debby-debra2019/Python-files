import pandas as pd 
# This command allows us to use the tools from the pandas library. 
# This is the library we need to read data.

import numpy as np
#numpy has all of our mathematical tools built-in for use in python.

from scipy import stats
#stats has some special statistics functions that we need to analyze data.

#All of the commands necessary for the assignment should go here:

#Reading data into python from pokemon and printing it
poke_data = pd.read_csv('Pokemon.csv')
pd.set_option('max_columns', None)
print(poke_data)

#Giving column Type 1 a special name
poke_main_type = poke_data['Type 1']
#finding the mode
type_mode = stats.mode(poke_main_type)
print('The mode of Type 1 column is: ' , type_mode)

#pokemon types
possible_types = set(poke_main_type)
print('The possible pokemon types are: ' ,possible_types)

#Calculating the mean HP of each type
poke_HP = poke_data['HP']
HP_mean = np.mean(poke_HP)
print('The mean of the HP column is:' , HP_mean)
mean_HP_by_type = {}
for p_type in possible_types:
    type_set = poke_data.loc[poke_data['Type 1'] == str(p_type)]
    mean_HP_by_type[p_type] = np.mean(type_set['HP'])
    print(type_set)
    print(mean_HP_by_type)

   


