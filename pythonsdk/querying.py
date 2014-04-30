import cPickle as pickle
import re
import math
import time
from operator import itemgetter
from stemming.porter2 import stem
def querying(query) :
    print "loading index .... "
    f = open("fullIndex.txt", "rb")
    completeIndex = pickle.load(f)
    print "Index loaded ... "
    final = []
    qDict = dict()
    index = completeIndex["index"]
    docIndex = completeIndex["docIndex"]
    docModIndex = completeIndex["docModIndex"]
    N = len(docModIndex.keys())
    #query = raw_input("Enter Query")
    #if(query == 'exit'):
    #    break;
    query=query.lower()
    qWords = re.split('[\W_]+', query)
    stemWords = []	
    for word in qWords :
	stemWords.append(stem(word))	
    for word in stemWords :
	qWords.append(word)	
    qDict.clear()
    for i in range(len(qWords)) :
            if qWords[i] in qDict :
                qDict[qWords[i]] = qDict[qWords[i]]+1
            else :
                qDict[qWords[i]] = 1
    qWords = []
    qVecMod = 0
    #print "Here 30 querying" 	
    for key in qDict:
        qWords.append(key)
        qVecMod = qVecMod + qDict[key]*qDict[key]
    qVecMod = math.sqrt(qVecMod)
    if(len(qWords) == 0) :
        print("Sorry, No match found!")
        final = []
        return [-1]
    if(len(qWords) == 1) :
        if(qWords[0] in index) :
            final = index[qWords[0]]
        else :
            final = []
    if(len(qWords) >= 2) :
	if((qWords[0] in index) and (qWords[1] in index)) :
            final = set(index[qWords[0]]).union(index[qWords[1]])
            newQ = qWords[2:len(qWords)]
	    for qWord in newQ :
     	       if qWord in index :
                 final = set(final).union(index[qWord])
               else :
                 final = set()
                 break
    #print "54 querying" 
    queryNumerator = dict()
    final = list(final)
    if(len(final)>0) :
        fileVectors = dict();
        fileVector = [];
        fileVectorsList = [];
        for file in final :
            fileVector = []
	    val = 0
	    for qWord in qWords:
		if qWord in index :
			if file in index[qWord]: 
				tf = (1+math.log10(index[qWord][file]))
				df = len(index[qWord])
				idf = math.log10(N)-math.log10(df)
				tfidf = (tf * idf)
				val = val + tfidf*(qDict[qWord])
	    queryNumerator[file]=val
	    val = val/(docModIndex[file]*qVecMod)
	    fileVectorsList.append([file, val])
        fileVectorsList.sort(key=itemgetter(1),reverse=True)
	
	count = 0
        return fileVectorsList[0:len(fileVectorsList)-1]
    else :
        print("Sorry, No matches found")
	return [-1]
    	
#postIds = []
#postIds = querying("Aggie")
#print "postIds = ",postIds
