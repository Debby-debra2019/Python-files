import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from lmfit import Model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

true_data = pd.read_csv("true_data.csv")
pd.set_option('max_columns', None)
print(true_data)

#use all columns to determine the sex of the speaker
X = true_data.loc[:,'radius_mean':'fractal_dimension_worst']
y = true_data['diagnosis']

#split the data into a random training set
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
print(X_train,X_test,y_train,y_test)

#establish a model
RF_model = RandomForestClassifier(n_estimators=100)
results = RF_model.fit(X_train,y_train)
print("result: ", results)
y_pred = results.predict(X_test)
print("y_predict: ", y_pred)

score = accuracy_score(y_pred,y_test)
print("score: ", score)

#features of the data are most useful in determining sex of the speaker
importance = results.feature_importances_
print(importance)

#Create a barplot with the columns of X (i.e. X.columns ) in the x-axis and importance in
#the y-axis.
plt.bar(X.columns, importance)
plt.title('X.columns Vs importance')
plt.xticks(rotation = 50)
plt.show()

#using the 5 most important features to make predictions
X2 = true_data[['texture_worst','concavity_mean', 'concavity_worst', 'perimeter_worst', 'fractal_dimension_se']]
print(X2)
X_train,X_test,y_train,y_test = train_test_split(X2,y,test_size=0.25)
RF_model2 = RandomForestClassifier(n_estimators=100)
results2 = RF_model2.fit(X_train,y_train)
y_pred2 = results2.predict(X_test)
score2 = accuracy_score(y_pred2,y_test)
print("score2: ", score2)

cm = confusion_matrix(y_test, y_pred2,labels=["M", "B"],normalize='pred')
print(cm)
its sns.heatmap(cm, cmap = "tab10")
plt.xticks(ticks = [0.5, 1.5],labels=['M','B'])
plt.yticks(ticks = [0.5,1.5],labels=['M','B'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.text(0.5,0.5, str(cm[0][0]))
plt.text(0.5,1.5, str(cm[0][1]))
plt.text(1.5,1.5, str(cm[1][1]))
plt.text(1.5,0.5, str(cm[1][0]))
plt.show()

