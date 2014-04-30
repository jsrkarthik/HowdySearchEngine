import os
import re
from sklearn import linear_model
import cPickle as pickle
from copy import deepcopy
fo = open("./featureList","wb+")
path = "./testcase2"

def getMax(inputList ) :
	indexi = 0;
	minValue = 1000000;
	maxValue = 0
	while(indexi < len(inputList)) :
		if(inputList[indexi] < minValue) :
			minValue = inputList[indexi]
		elif(inputList[indexi] > maxValue) :
			maxValue = inputList[indexi]
		indexi = indexi + 1
	return minValue, maxValue

cosineList = []
pageScoreList = [] 
postScoreList = []
postLenList = []
postRankList = []
epochScoreList = []


def createFeatureLabelList(path) :
	featureList = []
	labelList = []
	ID = 0
	for root,dirs,files in os.walk(path):
		for testcase in files :
			print "file = ",testcase
			if( testcase.endswith("karthik") or testcase.endswith("karthi") ) :
				cFile = open(os.path.join(root,testcase), "r")
				content = (cFile.read()).split("$$$$")
				index = 0
				while(index < len(content) ) :
					parameters = []
					parameters = re.split("[| \n]",content[index])
					if(parameters[1]=="START" ) :
						cosineList.append(float(parameters[2]))
						pageScoreList.append(float(parameters[3]))
						postScoreList.append(float(parameters[4]))
						epochScoreList.append(float(parameters[5]))
						postLenList.append(float(parameters[6]))
						postRankList.append(float(parameters[7]))
						indexi = len(cosineList)-1
						featureList.append([float(cosineList[indexi]),float(pageScoreList[indexi]),float(postScoreList[indexi]),float(epochScoreList[indexi]),float(postLenList[indexi])])
						print "indexi = ",indexi," postRank = ",postRankList[indexi],"pageScore = ",pageScoreList[indexi]," postScoreList = ",postScoreList[indexi]
						labelList.append(float(postRankList[indexi]))
						#fo.write(str(cosineList[indexi])+" "+str(pageScoreList[indexi])+" "+str(postScoreList[indexi])+" "+str(epochScoreList[indexi])+str(postLenList[indexi])+" "+str(postRankList[indexi]))
						#fo.write("\n")
					index = index + 1
				
				index = 0
	pageScoreMin = 0.0
	pageScoreMax = 0.0		
	#pageScoreMin, pageScoreMax = getMax(pageScoreList)
	pageScoreMax = max(pageScoreList)
	pageScoreMin = min(pageScoreList)
	postScoreMax = 0.0
	postScoreMin = 0.0
	postScoreMax = max(postScoreList)
	postScoreMin = min(postScoreList)
	#postScoreMin, postScoreMax = getMax(postScoreList)
	cosineMax = 0.0
	cosineMin = 0.0
	#cosineMin, cosineMax = getMax(cosineList)
	cosineMax = max(cosineList)
	cosineMin = min(cosineList)
	epochMax = 0.0
	epochMin = 0.0
	#epochMin, epochMax = getMax(epochScoreList)
	epochMax = max(epochScoreList)
	epochMin = min(epochScoreList)
	postLenMin = 0.0
	postLenMax = 0.0
	#postLenMin, postLenMax = getMax(postLenList)
	postLenMin = min(postLenList)
	postLenMax = max(postLenList)
	indexi = 0 
	paraDict = dict()
	while(indexi < len(cosineList)) :
		if((float(pageScoreMax) - float(pageScoreMin)) > 0 ) :
			pageScoreList[indexi] = (float(pageScoreList[indexi]) - float(pageScoreMin))/(float(pageScoreMax) - float(pageScoreMin))
		if((float(postScoreMax) - float(postScoreMin)) > 0 ) :
			postScoreList[indexi] = float((postScoreList[indexi]) - float(postScoreMin))/(float(postScoreMax) - float(postScoreMin))
		if((float(cosineMax) - float(cosineMin)) > 0 ) :
			cosineList[indexi] = float((cosineList[indexi]) - float(cosineMin))/(float(cosineMax) - float(cosineMin))
		if((float(epochMax) - float(epochMin))>0) :
			epochScoreList[indexi] = (float(epochScoreList[indexi]) - float(epochMin))/(float(epochMax) - float(epochMin))
		if((float(postLenMax) - float(postLenMin))>0) :	
			postLenList[indexi] = (float(postLenList[indexi]) - float(postLenMin))/(float(postLenMax) - float(postLenMin))
		fo.write(str(cosineList[indexi])+" "+str(pageScoreList[indexi])+" "+str(postScoreList[indexi])+" "+str(epochScoreList[indexi])+str(postLenList[indexi])+" "+str(postRankList[indexi]))
		fo.write("\n")
		featureList.append([float(cosineList[indexi]),float(pageScoreList[indexi]),float(postScoreList[indexi]),float(epochScoreList[indexi]),float(postLenList[indexi])])
		labelList.append(float(postRankList[indexi]))
		indexi = indexi + 1
	paraDict["postScoreMin"] = postScoreMin
	paraDict["postScoreMax"] = postScoreMax
	paraDict["pageScoreMax"] = pageScoreMax
	paraDict["pageScoreMin"] = pageScoreMin
	paraDict["epochScoreMax"] = epochMax
	paraDict["epochScoreMin"] = epochMin
	paraDict["postLenMax"] = postLenMax
	paraDict["postLenMin"] = postLenMin
	paraDict["cosineScoreMax"] = cosineMax
	paraDict["cosineScoreMin"] = cosineMin
	return featureList[:], labelList[:], deepcopy(paraDict)
featureList = []
labelList = []
paraDict = dict()
path = "./testcase4"
featureList, labelList, paraDict = createFeatureLabelList("./testcase4")
clf = linear_model.Ridge(alpha=0.5, normalize=True)
clf.fit(featureList,labelList)
	
paraDict["cosineParam"] = clf.coef_[0]
paraDict["pageScoreParam"] = clf.coef_[1]
paraDict["postScoreParam"] = clf.coef_[2]
paraDict["epochScoreParam"] = clf.coef_[3]
paraDict["postLenParam"] = clf.coef_[4]
featureValues = open("featureValue","wb+")
pickle.dump(paraDict,featureValues,-1)
featureValues.close()
print "weight vector = ",clf.coef_
print "cosineList = ",cosineList
print "postScoreList = ",postScoreList
print "pageScoreList = ",pageScoreList
featureListTest = []
predictedLabelListTest = []
labelListTest = []
paraDictTest = dict()
#clf = linear_model.LinearRegression()
clf = linear_model.Ridge(alpha=0.5, normalize=True)
clf.fit(featureList,labelList)
featureListTest,labelListTest, paraDictTest = createFeatureLabelList("./testcase3")
predictedLabelListTest = clf.predict(featureListTest)	
count = 0
for i in range(len(predictedLabelListTest)) :
	predictedLabelListTest[i]= int(predictedLabelListTest[i] + 0.5)
	print "actual Label = ", labelListTest[i], " predictedLabel = ",predictedLabelListTest[i]
	if(labelListTest[i] == predictedLabelListTest[i] ) :
		count = count + 1

print "Accuracy = ", (float(count)/float(len(predictedLabelListTest)))*100
	
