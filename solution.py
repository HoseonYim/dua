import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

userData = pd.read_csv('Users.csv')
characters = userData.drop(columns=['Addicted', 'UserName'])
addicted = userData['Addicted']

userModel = DecisionTreeClassifier()
userModel.fit(characters.values, addicted.values)

#tree.export_graphviz(userModel, out_file='userModelData.dot', feature_names=['Age', 'Gender', 'UserTime'], class_names=sorted(addicted.unique()), label='all', rounded='True', filled='True')

predcition = userModel.predict([[26, 1, 11.7], [23, 1, 1.7]])

print(predcition)