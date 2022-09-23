import pandas as pd
import numpy as np

userData = pd.read_csv('User1.csv')
addicted = userData['AppName']
print(addicted[1])
