'''
1. 'PassengerId', 'Survived', and 'Name' columns are used for identification, and not training.
2. 'Pclass', 'Fare', 'Cabin', and 'Ticket' columns are likely to show correlation, and since we are using a decision tree model, we will use 'Pclass' to represent all of them.
3. The 'Embarked' column is logically irrelevant to a passanger's survival.
4. A higher number of parents should increase a child's rate of survival, but a higher number of children should decreate a parent's rate of survival. Because of this contradiction, these columns are unreliable for now (we will still use them and see what we get).

Useful: ['Pclass', 'Sex', 'Age', 'Sibsp', 'Parch']
Not Useful: ['PassengerId', 'Survived', 'Name', 'Ticket', 'Fare', 'Cabin', 'Embarked']
'''



import csv, copy, os, pydot
from sklearn import tree
from sklearn.externals.six import StringIO

def formatdata(indata):
    outdata = copy.deepcopy(indata)
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

def getcols(indata, rawcols, cols):
    outdata = copy.deepcopy(indata)
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
    print("\nTraining the model...")
    rawfile = list(csv.reader(open(file)))
    rawcols = rawfile[0]
    data = formatdata(rawfile)
    trainInput = getcols(data, rawcols, inCols)
    trainOutput = getcols(data, rawcols, outCols)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(trainInput, trainOutput)
    print('Done')
    return clf

def predict(infile, inCols, outfile, model, format):
    print("\nGenerating predictions...")
    rawfile = list(csv.reader(open(infile)))
    rawcols = rawfile[0]
    data = formatdata(rawfile)
    predictInput = getcols(data, rawcols, inCols)
    prediction = model.predict(predictInput)
    with open(outfile, 'w') as file:
        header = ''
        rawcoli = []
        for item in format:
            header += item + ','
        header = header[:-1]
        header += '\n'
        file.write(header)
        rawcoli = []
        cols = []
        for i in range(len(format)-1):
            cols.append(format[i])
        attributes = getcols(data, rawcols, cols)
        output = ''
        for i in range(len(prediction)):
            for att in attributes[i]:
                output += att + ','
            output += prediction[i] + '\n'
        file.write(output)
    print('Done')
    dir_path = os.path.dirname(os.path.realpath(__file__)) + outfile
    print("\nPrediction Successful\nExported to '" + dir_path + "'\n")
    
def main(inCols, outCols, trainfile, testfile, exportfile, exportformat):
    clf = train(trainfile, inCols, outCols)
    predict(testfile, inCols, exportfile, clf, exportformat)
    
main(['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'], ['Survived'], 'train.csv', 'test.csv', 'prediction.csv', ['PassengerId', 'Survived'])

# Submission Scores (Goal: 97+)
scores = {1: 0.70813, 2: 0.72248}