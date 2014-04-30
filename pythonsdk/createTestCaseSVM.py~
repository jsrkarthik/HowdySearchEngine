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
featureList = []
labelList = []

def createQdict(path) :
	qDict = dict()
	ID = 0	
	for root,dirs,files in os.walk(path):
		for testcase in files :
			qDict[ID] = list()
			cosineList = []
			pageScoreList = []
			postScoreList = []
			epochScoreList = []
			postLenList = []
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
				pageScoreMin = 0.0
				pageScoreMax = 0.0
				pageScoreMax = max(pageScoreList)
				pageScoreMin = min(pageScoreList)
				postScoreMax = 0.0
				postScoreMin = 0.0
				postScoreMax = max(postScoreList)
				postScoreMin = min(postScoreList)
				cosineMax = 0.0
				cosineMin = 0.0
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
				indexi = 0
				while(indexi < len(cosineList)) :
					temp2 =list()	
					temp2.append(labelList[indexi])
					temp2.append(pageScoreList[indexi])
					temp2.append(postScoreList[indexi])
					temp2.append(epochScoreList[indexi])
					temp2.append(postLenList[indexi])
					qDict[ID].append(temp2[:])	
					indexi = indexi + 1
	  		ID = ID + 1
	return deepcopy(qDict)		
qDict = dict()
path = "/home/javar/Desktop/Dropbox/IRProject/pythonsdk/testcase4"
qDict = createQdict(path)

qDictTest = dict()
path = "/home/javar/Desktop/Dropbox/IRProject/pythonsdk/testcase3"
qDictTest = createQdict(path)
f = open("/home/javar/Desktop/Dropbox/IRProject/pythonsdk/trainDict.data","wb+")
pickle.dump(qDict,f,-1)
f.close()
f = open("/home/javar/Desktop/Dropbox/IRProject/pythonsdk/testDict.data","wb+")
pickle.dump(qDict,f,-1)
f.close()

'''paraDict = dict()			
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

#clf = linear_model.LinearRegression()
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
print "pageScoreList = ",pageScoreList'''
