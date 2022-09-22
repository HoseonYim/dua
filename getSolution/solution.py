import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

usersData = pd.read_csv('Users.csv')
characters = usersData.drop(columns=['Addicted', 'UserName'])
addicted = usersData['Addicted']

print(characters)

userModel = DecisionTreeClassifier()
userModel.fit(characters.values, addicted.values)

predcition = userModel.predict_proba([[26, 1, 11.7], [23, 1, 1.7]])

print(predcition)
