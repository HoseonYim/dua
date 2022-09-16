# Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
# /python.py python.py
from cmath import log
import matplotlib.pyplot as plt
import numpy as np
import csv

csvPath = 'sample.csv'
csvFile = open(csvPath, 'r', encoding='utf-8')
csvRdr = csv.reader(csvFile)

app = []
time = []

logTimestamp = []
logApp = []
logCategory = []
logTag = []

next(csvRdr)

for line in csvRdr:
    logTimestamp.append(int(line[0]))
    logApp.append(line[1])
    logCategory.append(line[2])
    logTag.append(line[3])

print(logTimestamp)
print(logApp)
print(logCategory)
print(logTag)

for i in range(len(logTimestamp)):
    if logTag[i] == 'False':
        app.append(logApp[i])
        time.append(logTimestamp[i] - logTimestamp[i - 1])

plt.bar(app, time)
plt.show()