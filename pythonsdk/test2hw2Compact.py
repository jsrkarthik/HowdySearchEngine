import re
import time
import numpy
import os
from sklearn import svm
from operator import itemgetter
import cPickle as pickle
#path = '/home/javar/Downloads/Homework2/homework2 files/part 2/'
#The method to separate and store the data queryID wise.
def createDict(path1):
	qDict1 = dict()	
	with open(path1) as f:
		count = 0
		for line in f:
			if(len(line)>1):
				flist = re.split('[ ]+',line)
				tempList = [0]*47
				qid = re.split('[:]', flist[1])[1]
				qid = int(qid)
				if not qid in qDict1 :
					qDict1[qid]= list()
				relevance = flist[0]
				tempList[0] = relevance
				i = 2;
				while i<42 :
					feature = re.split('[:]', flist[i])
					tempList[int(feature[0])] = feature[1]
					i = i+1
				qDict1[qid].append(tempList)
		
	return qDict1

#Method to transform the data and create Feature and label list. Takes the data generated in the above function. 
def createFeatureLabelList(qDict1) :
	featureList1 = list()
	labelList1 = list()
	for key in qDict1 :
		listLen = len(qDict1[key])
		for i in range(listLen) :
			'''print qDict1[key][i]
			for j in range(listLen) :'''
			tempList2 = []
			#if(  i!=j and float(qDict1[key][i][0])!=float(qDict1[key][j][0])) :
			for k in range(4) :
				tempList2.append(0)
			for k in range(4) :
				tempList2[k] = (float(qDict1[key][i][k+1]))
			featureList1.append(tempList2)
					#if( float(qDict1[key][i][0])>float(qDict1[key][j][0])) :
					#	labelList1.append(1)
					#else :
					#	labelList1.append(-1)
			labelList1.append(float(qDict1[key][i][0]))
	return featureList1[:], labelList1[:]
		
#os walk for 3 folders
fold = 0
qDict = dict()
qDictTest = dict()
#qDict = createDict(os.path.join(dir1,'train.txt'))
#qDictTest = createDict(os.path.join(dir1,'test.txt'))
f = open("/home/javar/Desktop/Dropbox/IRProject/pythonsdk/trainDict.data")
qDict = pickle.load(f)
f.close()
f = open("/home/javar/Desktop/Dropbox/IRProject/pythonsdk/testDict.data")
qDictTest = pickle.load(f)
f.close()
featureList = list()
labelList = list()
featureListTest = list()
labelListTest = list()
#creating feature vectors and corresponding labels for training data
featureList, labelList = createFeatureLabelList(qDict)
#creating feature vectors and corresponding labels for training data
featureListTest, labelListTest = createFeatureLabelList(qDictTest)
maxAccuracy = 0
maxC = 0
c = 0.1
while ( c < 100 ) :
	print "Training SVM"
	lin_clf = svm.SVC(C=c,kernel='linear')
	lin_clf.fit(featureList, labelList)
	print "Training SVM finish"
	predictedLabelListTest = lin_clf.predict(featureListTest)
	count = 0
	print "predictedLabelListTest = ",predictedLabelListTest
	for i in range(len(predictedLabelListTest)) :
		if(predictedLabelListTest[i] == labelListTest[i]) :
			count=count+1
	#print "Number of Correct labels predicted =", count
	#print "Number of inputs =", 
	accuracy = (float(count)/float(len(predictedLabelListTest)))*100	
	print "C = ",c,"  Accuracy ", " = ", accuracy
	if (maxAccuracy < accuracy ) : 
		maxAccuracy = 0	
		maxC = c 
	c =  c + 0.1	
print "maxAccuracy = ",maxAccuracy, "  maxC = ",c
'''coef = lin_clf.coef_[0]
		coefList = []
		for i in range(len(coef)) :
			temp =list()
			temp.append(i+1)
			temp.append(abs(float(coef[i])))
			if(coef[i]<0) :
				temp.append(1)
			else :
				temp.append(0)
					
			coefList.append(temp)
		coefList.sort(key=itemgetter(1),reverse=True)
		count = 0
		#sorting the feature vectors based on the absolute value.
		print "List of top 10 features with their weights"
		for s in coefList :
			if count == 10 :
				break;
			val = s[1]
			if(s[2]==1) :
				val = -val
			print "feature[ ",s[0],"]=",val
			count=count+1;
		fold = fold+1'''
		
