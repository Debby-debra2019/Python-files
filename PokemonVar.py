import pandas as pd 
# This command allows us to use the tools from the pandas library. 
# This is the library we need to read data.

import numpy as np
#numpy has all of our mathematical tools built-in for use in python.

from scipy import stats
#stats has some special statistics functions that we need to analyze data.

#from matplotlib import pyplot as plt
#this allows us to make graphs so we can better visualize our data!

poke_data = pd.read_csv('Pokemon.csv')

mean_hp = np.mean(poke_data['HP'])
mean_spd = np.mean(poke_data['Speed'])
mean_atk = np.mean(poke_data['Attack'])
mean_def = np.mean(poke_data['Defense'])
mean_spatk = np.mean(poke_data['Sp. Atk'])
mean_spdef = np.mean(poke_data['Sp. Def'])

print('The mean HP is:')
print(mean_hp)
print('The mean Speed is:')
print(mean_spd)
print('The mean Attack is:')
print(mean_atk)
print('The mean Defense is:')
print(mean_def)
print('The mean Sp. Atk is:')
print(mean_spatk)
print('The mean Sp. Def is:')
print(mean_spdef)

#Write your commands in below this line:

std_hp = np.std(poke_data[ 'HP' ])
print("The standard deviation of HP is: ", std_hp)
std_spd = np.std(poke_data[ 'Speed' ])
print("The standard deviation of speed is: ", std_spd)
std_atk = np.std(poke_data[ 'Attack' ])
print("The standard deviation of Attack is: ", std_atk)
std_def = np.std(poke_data[ 'Defense' ])
print("The standard deviation of Defense is: ", std_def)
std_spatk = np.std(poke_data[ 'Sp. Atk' ])
print("The standard deviation of Sp. Atk is: ", std_spatk)
std_spdef = np.std(poke_data[ 'Sp. Def' ])
print("The standard deviation of Sp. Def is: ", std_spdef)

within_std_hp = poke_data.loc[ (poke_data['HP'] > mean_hp - std_hp) & (poke_data['HP'] < mean_hp + std_hp)]
print(within_std_hp)
print('------------------------------------------------------------------------------')
within_std_spd = poke_data.loc[ (poke_data['Speed'] > mean_hp - std_spd) & (poke_data['Speed'] < mean_hp + std_spd)]
print(within_std_spd)
print('------------------------------------------------------------------------------')
within_std_atk = poke_data.loc[ (poke_data['Attack'] > mean_hp - std_atk) & (poke_data['Attack'] < mean_hp + std_atk)]
print(within_std_atk)
print('------------------------------------------------------------------------------')
within_std_def = poke_data.loc[ (poke_data['Defense'] > mean_hp - std_def) & (poke_data['Defense'] < mean_hp + std_def)]
print(within_std_def)
print('------------------------------------------------------------------------------')
within_std_spatk = poke_data.loc[ (poke_data['Sp. Atk'] > mean_hp - std_spatk) & (poke_data['Sp. Atk'] < mean_hp + std_spatk)]
print(within_std_spatk)
print('------------------------------------------------------------------------------')
within_std_spdef = poke_data.loc[ (poke_data['Sp. Def'] > mean_hp - std_spdef) & (poke_data['Sp. Def'] < mean_hp + std_spdef)]
print(within_std_spdef)
print('------------------------------------------------------------------------------')

num_std_hp = len( within_std_hp[ 'HP' ] )
print(num_std_hp)
num_std_spd = len( within_std_spd[ 'Speed' ] )
print(num_std_spd)

num_std_atk = len( within_std_atk[ 'Attack' ] )
print(num_std_atk)

num_std_def = len( within_std_def[ 'Defense' ] )
print(num_std_def)

num_std_spatk = len( within_std_spatk[ 'Sp. Atk' ] )
print(num_std_spatk)

num_std_spdef = len( within_std_spatk[ 'Sp. Def' ] )
print(num_std_spdef)


frac_hp = num_std_hp / len( poke_data['HP'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean HP:')
print(frac_hp)
frac_spd = num_std_spd / len( poke_data['Speed'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean Speed:')
print(frac_spd)
frac_atk = num_std_atk / len( poke_data['Attack'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean Attack:')
print(frac_atk)
frac_def = num_std_def / len( poke_data['Defense'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean Defense:')
print(frac_def)
frac_spatk = num_std_hp / len( poke_data['Sp. Atk'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean Sp. Attack:')
print(frac_spatk)
frac_spdef = num_std_spdef / len( poke_data['Sp. Def'] )
print('This is the fraction of pokemon in 1 standard deviation of the mean Sp. Sp. Defense:')
print(frac_spdef)



#Question: Is there a pattern to these numbers? Yes, they are very close to one another in terms of range
#Question: Let’s say we have another stat called IV. What would you guess the fraction of IV’s that fall
#within one standard deviation of the mean would be? You can give a range, but that range better not be 0
#to 1. The fraction will fall between 0.60 to 0.80
#Question: If we were to calculate a mean of these six fractions, which mean do you think would be best?
#Arithmetic, geometric or harmonic? Arithmetic mean will be the best. Why? Because all the fractions have a similar range


















