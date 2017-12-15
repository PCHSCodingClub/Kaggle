import csv, sys

infile = "train.csv"

def getData(file):
	data = list(csv.reader(open(file)))
	del data[0]
	return data

def getCols(file):
	data = list(csv.reader(open(file)))
	cols = data[0]
	return cols

def filter(data, cols, col, keyword):
	print("Keyword: " + keyword)
	colIndex = cols.index(col)
	colData = []
	for list in data:
		colData.append(list[colIndex])
	matchIndex = []
	for i in range(len(colData)):
		if colData[i] == '':
			continue
		if keyword == colData[i]:##Equals
#		if keyword in colData[i]:##Contains
#		if float(keyword) >= float(colData[i]) and float(keyword)-10 < float(colData[i]):
			matchIndex.append(i)
	outData = []
	for index in matchIndex:
		outData.append(data[index])
	return outData
	
def output(data, file):
	data.insert(0, getCols(infile))
	with open(file, 'w') as extfile:
		for list in data:
			str = ""
			for item in list:
				str += item + ','
			str = str[:-1]
			extfile.write(str+'\n')
	print(rate(data, getCols(infile)))

def rate(data, cols):
	index = cols.index("Survived")
	total = len(data)-1
	count = 0
	for list in data:
		if list[index] == '1':
			count += 1
	percentage = (count/total) * 100
	return "Survival rate: " + str(percentage) + "\nRatio: " + str(count) + "/" + str(total)
		
# PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked

first_arg = sys.argv[1] #CATEGORY
second_arg = sys.argv[2] #KEYWORD
	
infile = "train.csv"
output(filter(getData(infile), getCols(infile), first_arg, second_arg), "category.csv")