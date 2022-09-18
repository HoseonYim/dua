import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

userData = pd.read_csv('Users.csv')
charaters = userData.drop(columns=['Addicted'])
addicted = userData['Addicted']

userModel = DecisionTreeClassifier()
userModel.fit(charaters, addicted)

tree.export_graphviz(userModel, out_file='userModelData.dot', feature_names=['Age', 'Gender'], class_names=sorted(addicted.unique()), label='all', rounded='True', filled='True')

predcition = userModel.predict(['User6', 26, 'Male', 11.7])
predcition