
Importing Libraries
"""

import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

"""Mounting Drive"""

from google.colab import drive
drive.mount('/content/drive/')

"""Directory"""

!ls "/content/drive/My Drive/cse422/"

"""Loading Data"""

heart_data="/content/drive/My Drive/cse422/heart failur classification dataset.csv"

dataframe=pd.read_csv(heart_data)
dataframe

"""Shape of the dataset"""

dataframe.shape

"""Checking Null Value"""

dataframe.isnull().sum()

"""Dropping missing value coloums"""

dataframe=dataframe.drop(['serum_sodium','time'], axis=1)

"""Shape after dropping"""

dataframe.shape

"""Datatype"""

dataframe.info()

"""unique values of "sex""""

dataframe['sex'].unique()

"""Encoding Categorical Values of sex"""

enc=LabelEncoder()
dataframe['sex']=enc.fit_transform(dataframe['sex'])
print(dataframe[['sex']].head())

"""unique values of "smoking""""

dataframe['smoking'].unique()

"""Encoding Categorical Values of smoking"""

enc=LabelEncoder()
dataframe['smoking']=enc.fit_transform(dataframe['smoking'])
print(dataframe[['smoking']].head())

"""Datatype"""

dataframe.info()

"""Seperating features and labels"""

X = dataframe.iloc[:, :-1]
y = dataframe.iloc[:, -1]

"""Split the data into 80% training and 20% testing"""

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Train the model using logistic regression"""

model = LogisticRegression()
#Training the model
model.fit(x_train, y_train)
predictions = model.predict(x_test)
#Printing predictions
print(predictions)

"""Printing Accuracy Score using Logistic Regression"""

Logistic_reg_accscore=accuracy_score(y_test, predictions)
print(Logistic_reg_accscore)

"""Using Scikit Learn Library for Decision Tree and printing accuracy score"""

X = dataframe.iloc[:, :-1]
y = dataframe.iloc[:, -1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
clf = DecisionTreeClassifier(criterion='entropy',random_state=42)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
Decision_tree_accscore=accuracy_score(y_pred,y_test)
print(Decision_tree_accscore)

"""Comparing the accuracy and ploting them as a bar chart"""

fig = plt.figure()
s = fig.add_subplot(111)
s.bar([1, 2], [Logistic_reg_accscore,Decision_tree_accscore], width=1)
s.set_xlim(0.5, 3.5)
fig.savefig('t.png')
