import simplejson as json
import re
import os
import math
import time
from decimal import *
from operator import itemgetter
import cPickle as pickle
from stemming.porter2 import stem
completeIndexFile = open("fullIndex.txt", "wb+")
files = []
index =dict() 
docIndex = dict()
start = time.time()
splitTime = 0
pTime = 0
oTime = 0
nInsert = 0
fInsert = 0
words=set()
count = 0;
pathList = ["./pagePostDir","./groupPostDir"]
for path in pathList :
	for root,dirs,files in os.walk(path):
	    for page in files :
	        if page.endswith(".txt"):
			#if not file in docIndex :
			#    docIndex[file]=dict()
	                cFile = open(os.path.join(root,page), "r")
			print "page = ",page
			for line in cFile :
				print "count = ",count
				data = json.loads(line)
					
				if not ("message" in data.keys()) :
					continue
				print data["message"].encode("utf-8"),"\n" 	
				#print "list of keys = ",data.keys()
				file = data["id"]
				post = data["message"]
				if not file in docIndex :
				    docIndex[file]=dict()	
	                	words = re.split('[\W_]+', post.lower())
			        stemWords = []
				for word in words :
					stemWords.append(stem(word))
				for word in stemWords :
					words.append(word)
	                	for word in words :  
				    if(len(word)>0) :
	                	    	if not word in index :
	                	        	index[word]=dict()
	                	    	if file in index[word]:
	                	        	index[word][file] += 1
	                	   	else:
	                	        	index[word][file] = 1
				    	if word in docIndex[file] :
						docIndex[file][word] +=1
				    	else :
						docIndex[file][word]=1
				count = count + 1
			
end = time.time()
start1 = time.time()
N = count
docModIndex = dict()

for doc in docIndex :
	val = 0
	for word in docIndex[doc] :
		tf = 1+math.log10(docIndex[doc][word])
		df = len(index[word])
		idf = math.log10(N)-math.log10(df)
		tfidf = tf*idf
                if(doc == "a0318637.txt"):
			print word, tf, df, tfidf
		val = val + (tfidf*tfidf)

	val = math.sqrt(val)
	docModIndex[doc]=val
end1 = time.time()		
docIndex.clear()

completeIndex = dict()
completeIndex["index"] = index
completeIndex["docIndex"] = docIndex
completeIndex["docModIndex"] = docModIndex
print "Dumping Index .. please wait"
pickle.dump(completeIndex, completeIndexFile,-1 )
print "Index dumped"
print("Time taken for building index = ")
print(end-start)
print("Time taken for building docIndex = ")
print(end1-start1)

print("Number of files =")
print(count)
print("Number of words in the index = ")
print(len(index))
final = []
qDict = dict();

while 1 :
    query = raw_input("Enter Query")
    if(query == 'exit'):
        break;
    query=query.lower()
    qWords = re.split('[\W_]+', query)
    qDict.clear()
    for i in range(len(qWords)) :
            if qWords[i] in qDict :
                qDict[qWords[i]] = qDict[qWords[i]]+1
            else :
                qDict[qWords[i]] = 1
    qWords = []
    qVecMod = 0
    for key in qDict:
        qWords.append(key)
        qVecMod = qVecMod + qDict[key]*qDict[key]
    qVecMod = math.sqrt(qVecMod)
    if(len(qWords) == 0) :
        print("Sorry, No match found!")
        final = []
        continue
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
        for s in fileVectorsList :
		if count == 50 :
			break;
		print s[0],"[",s[1],"]"
		count=count+1;
    else :
        print("Sorry, No matches found")

