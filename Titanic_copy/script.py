percentage = {
	"Pclass": {"search": "equals", "1": 0.6296, "2": 0.4728, "3": 0.2424 },
	"Name": {"search": "contains", "Master": 0.5609, "Miss.": 0.6978, "Mrs.": 0.792, "default": 1},
	"Sex": {"search": "equals", "male": 0.1889, "female": 0.742, "default": 1},
	"Age": {"search": "map"},
	"SibSp": {"search": "equals", "0": 0.3453, "1": 0.5359, "2": 0.4643, "3": 0.25, "4": 0.1667, "5": 0.1, "8":0.1},
#	"Ticket": {"search": "contains", },
	"Fare": {"search": "map"}
}

import csv, copy

def formatData(indata):
	outdata = copy.deepcopy(indata)
	rawcols = outdata[0]
	del outdata[0]
	curacols = list(percentage.keys())
	curaindex = []
	for col in curacols:
		curaindex.append(rawcols.index(col))
	for person in outdata:
		chances = [0] * len(curacols)
		composite = 1
		for i in range(len(person)):
			if i not in curaindex:
				continue
			if percentage[rawcols[i]]["search"] == "equals":
				for keyword in list(percentage[rawcols[i]].keys()):
					if keyword == str(person[i]):
						chances[curacols.index(rawcols[i])] = str(percentage[rawcols[i]][keyword])
					elif "default" in list(percentage[rawcols[i]].keys()):
						chances[curacols.index(rawcols[i])] = str(percentage[rawcols[i]]["default"])
					else:
						chances[curacols.index(rawcols[i])] = "0.384"
#			elif percentage[rawcols[i]]["search"] == "contains":
#				
#			elif percentage[rawcols[i]]["search"] == "map":
#				
		for item in chances:
			composite *= float(item)
		print(chances, composite)
		
file = list(csv.reader(open("train.csv")))
formatData(file)