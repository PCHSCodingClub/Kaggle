'''
1. 'PassengerId', 'Survived', and 'Name' columns are used for identification, and not training.
2. 'Pclass', 'Fare', 'Cabin', and 'Ticket' columns are likely to show correlation, and since we are using a decision tree model, we will use 'Pclass' to represent all of them.
3. The 'Embarked' column is logically irrelevant to a passanger's survival.
4. A higher number of parents should increase a child's rate of survival, but a higher number of children should decreate a parent's rate of survival. Because of this contradiction, these columns are unreliable for now (we will still use them and see what we get).

Useful: ['Pclass', 'Sex', 'Age', 'Sibsp', 'Parch']
Not Useful: ['PassengerId', 'Survived', 'Name', 'Ticket', 'Fare', 'Cabin', 'Embarked']
'''



import csv
from sklearn import tree

def formatdata(data):
    outdata = data
    rawcols = outdata[0]
    del outdata[0]
    for item in outdata:
        sex = item[rawcols.index('Sex')]
        if sex == 'male':
            sex = 1
        elif sex == 'female':
            sex = 0
        item[rawcols.index('Sex')] = sex
        for col in item:
            if col == '':
                outdata[outdata.index(item)][item.index(col)] = '0'
    return outdata

def getcols(data, rawcols, cols):
    outdata = data
    colindex = []
    for col in cols:
        colindex.append(rawcols.index(col))
    colindex.sort(reverse=True)
    for item in outdata:
        length = len(item)
        for i in range(length-1, -1, -1):
            if i not in colindex:
                del item[i]
    return outdata

def train(file, inCols, outCols):
    rawfile = list(csv.reader(open(file)))
    rawcols = rawfile[0]
    data = formatdata(rawfile)
#    X = getcols(data, rawcols, inCols)
    X = getcols(data, rawcols, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'])
    print(X)
    Y = getcols(data, rawcols, outCols)
    clf = tree.DecisionTreeClassifier()
    return clf.fit(X, Y)

def predict(infile, inCols, outfile, model, format):
    rawfile = list(csv.reader(open(infile)))
    rawcols = rawfile[0]
    data = formatdata(rawfile)
#    X = getcols(data, rawcols, inCols)
    X = getcols(data, rawcols, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'])
    prediction = model.predict(X)
    print(prediction)
#    with open(outfile, 'w') as file:
#        header = ''
#        for item in format:
#            header += item + ','
#        header = header[:-1]
#        header += '\n'
#        file.write(header)
#        for item in range(len(prediction)):
#            output = ''
#            for col in item:
#                output += 
#            file.write(test[item][0] + ',' + prediction[item] + '\n')

inCols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
outCols = ['Survived']

clf = train('train.csv', inCols, outCols)
predict('test.csv', inCols, 'prediction.csv', clf, ['PassengerId', 'Survived'])

# Prediction Score: 0.70813