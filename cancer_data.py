import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from lmfit import Model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

breast_cancer = pd.read_csv('breast-cancer.csv')
pd.set_option('max_columns', None)
print(breast_cancer)

data_known = breast_cancer.dropna()
print(data_known)

#X = data_known.loc[:, 'radius_mean': 'fractal_dimension_worst']
#y = data_known['daignosis']
logistic_model = LogisticRegression(max_iter=6000)
result = logistic_model.fit(X,data_known['diagnosis'])
data_predict = data.loc[data['diagnosis'].isna()]
predict_indeces = data_predict.index

true_data = pd.read_csv("true_data.csv")
pd.set_option('max_columns', None)
print(true_data)

data_actual = true_data.iloc[predict_indeces]
predicted_values = result.predict(data_predict.loc[:,'radius_mean':'fractal_dimension_worst'])
accuracy = accuracy_score(predicted_values,data_actual['diagnosis'])
prob_pred = result.predict_proba(true_data.loc[:,'radius_mean':'fractal_dimension_worst'])
print(prob_pred)
true_data['probability_B'] = pred_prob[:,0]
true_data['probability_M'] = pred_prob[:,1]
