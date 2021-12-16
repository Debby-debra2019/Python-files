import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

covid_data = pd.read_excel('All_ages_for_Matt-1.xls',sheet_name = None)
print(covid_data)

print(covid_data['Age1'])
covid_data = pd.read_excel('All_ages_for_Matt-1.xls',sheet_name = None,header=None)
print(covid_data)


age_averages_array = np.zeros((701,16))

for i in range(1,17):
    age_sheet = covid_data['Age'+str(i)]
    age_mean_cases = np.mean(age_sheet,axis=1)
    age_averages_array[:,i-1] = age_mean_cases
print(age_sheet)
print(age_mean_cases)

col_names = ['0-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','64-69','70-74','75-79','80+']
clean_mean_data = pd.DataFrame(age_averages_array,columns =col_names)

clean_mean_data.to_csv('Filename.csv')
sns.lineplot(data=clean_mean_data, palette='CMRmap')
plt.show()

