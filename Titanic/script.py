import csv
def importcols(file):
    return list(csv.reader(open(file)))[0]
def importdata(file):
    l = list(csv.reader(open(file)))
    del l[0]
    return l

cols = importcols('train.csv')
data = importdata('train.csv')

#['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

# Without looking at the data:
# 'PassengerId', 'Survived', and 'Name' columns are used for identification, not training.
# 'Pclass' and 'Fare' columns ('Cabin', 'Ticket') are likely to be highly correlated. Since we are using a decision tree as our first model, we will represent all of these using Pclass.
# 'Embarked' locations should not affect survival.
# Higher # of parents should increase child's survival, but higher # of children should decrease parents survival. Therefore, the 'Parch' column is unclear.
# 'Ticket' and 'Cabin' could show clusters of survivers and casualties.

# Useful: ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
# Not Useful: ['PassengerId', 'Survived', 'Name', 'Ticket', 'Fare', 'Cabin', 'Embarked']



# Now let's look at the data.

import numpy as np
import matplotlib.pyplot as plt

#N = 3
#survived = [0, 0, 0]
#died = [0, 0, 0]
#
#for person in data:
#    if person[1] == "1":
#        survived[int(person[2])-1] += 1
#    elif person[1] == "0":
#        died[int(person[2])-1] += 1
#
#ind = np.arange(N)
#width = 0.35
#
#p1 = plt.bar(ind, survived, width)
#p2 = plt.bar(ind, died, width, bottom=survived)
#
#plt.title('Survival by Class')
#plt.ylabel('People')
#plt.xticks(ind, ('Class 1', 'Class 2', 'Class 3'))
#plt.yticks(np.arange(0, 501, 100))
#plt.legend((p1[0], p2[0]), ('Alive', 'Dead'))
#
#plt.show()

#N = 3
#survived = [0, 0]
#died = [0, 0]
#
#for person in data:
#    if person[1] == '1':
#        if person[4] == 'male':
#            survived[0] += 1
#        elif person[4] == 'female':
#            survived[1] += 1
#    elif person[1] == '0':
#        if person[4] == 'male':
#            died[0] += 1
#        elif person[4] == 'female':
#            died[1] += 1
#            
#print(survived, died)
#
#ind = np.arange(N)
#width = 0.35
#p1 = plt.bar(ind, survived, width)
#p2 = plt.bar(ind, died, width, bottom=survived)
#plt.title("Survival by Sex")
#plt.ylabel('People')
#plt.xticks(ind, ('Male', 'Female'))
#plt.yticks(np.arange(0, 501, 100))
#plt.legend((p1[0], p2[0]), ('Alive', 'Dead'))
#plt.show()

cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
rawcols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

X = []
Y = []

for person in data:
    if person[rawcols.index('Sex')] == 'male':
        person[rawcols.index('Sex')] = 1
    elif person[rawcols.index('Sex')] == 'female':
        person[rawcols.index('Sex')] = 0
    output = []
    for col in cols:
        if person[rawcols.index(col)] != '':
            output.append(float(person[rawcols.index(col)]))
        else:
            output.append(0)
    X.append(output)
    Y.append(person[1])
    
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

test = importdata('test.csv')
testX = []
rawcols = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
for person in test:
    if person[rawcols.index('Sex')] == 'male':
        person[rawcols.index('Sex')] = 1
    elif person[rawcols.index('Sex')] == 'female':
        person[rawcols.index('Sex')] = 0
    output = []
    for col in cols:
        if person[importcols('test.csv').index(col)] != '':
            output.append(person[importcols('test.csv').index(col)])
        else:
            output.append(0)
    testX.append(output)
    
prediction = clf.predict(testX)
print(len(prediction))

with open('prediction.csv', 'w') as file:
    file.write('PassengerId,Survived\n')
    for item in range(len(prediction)):
        file.write(test[item][0] + ',' + prediction[item] + '\n')

# Prediction Score: 0.70813