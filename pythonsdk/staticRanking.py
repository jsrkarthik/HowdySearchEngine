import MySQLdb as mdb
import querying as ql
from copy import copy
from operator import itemgetter
import time
import datetime
import cPickle as pickle
def staticRanking(query) :
	if(query == 'exit'):
        	return [-1];
	cosineResults = ql.querying(query)
	print "Retrieved cosine resulst"	
	con = mdb.connect('localhost', 'root', 'javar', 'nkj255-db1')
	print "got the connection"
	if(len(cosineResults) == 0) :
		return [-1]
	if(len(cosineResults) == 1 and cosineResults[0]==-1) :
		return [-1]
	#print "Cosine Rsults  = ",cosineResults
        with con :
        	cur = con.cursor(mdb.cursors.DictCursor)
		cosine = []
		cosineNorm = []
		ppIDScore = []
		
		pageScore = []
		pageScoreNorm = []
		postScore = []
		postScoreNorm = []
	        postLen = []
		postLenNorm = []
		postList = []
		postListNorm = []
		epochTime = []
		epochTimeNorm = []
		post  = str("")
		iden = []	
        	for postPageId in cosineResults:
			postId = postPageId[0].split("_")[1]
			pageId = postPageId[0].split("_")[0]	
                  	cur.execute("SELECT * FROM PostInfo,PageInfo WHERE PageInfo.pageID = PostInfo.pageID  and PostInfo.postID=%s and PostInfo.pageID=%s ORDER BY date ASC",(postId,pageId))
                  	row = cur.fetchone()
			if not row :
				continue 
			post = row["post"]
			if(len(post) > 40 ) :
				#print "row = ",row
		        	cosine.append( float(postPageId[1]) )
				cosineNorm.append(float(postPageId[1]))	
				iden.append(postPageId[0])
				
				likes = row["likes"]
				comments = row["comments"]
				shares = row["shares"]
				pageLikes = row["PageInfo.likes"]
				postScore.append( likes+shares+comments	)
				pageScore.append( pageLikes )
				postLen.append(len(post))
				postList.append(post)
				postScoreNorm.append( likes+shares+comments	)
				pageScoreNorm.append( pageLikes )
				postLenNorm.append(len(post))
				postListNorm.append(post)

				date = row["date"].split("-")
				s = str(date[2])+"/"+str(date[1])+"/"+str(date[0])	
                                epochTime.append(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
				epochTimeNorm.append(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))				
				#print "postId = ",postId," pageId = ",pageId	
		#if(len(pageScore) > 0 ) :
		f = open("featureValue","rb+")
		paraDict = pickle.load(f)
		f.close()
		maxPageScore = paraDict["pageScoreMax"]
		minPageScore = paraDict["pageScoreMin"]
		maxPostScore = paraDict["postScoreMax"]
		minPostScore = paraDict["postScoreMin"]
		maxCosineScore = paraDict["cosineScoreMax"]
		minCosineScore = paraDict["cosineScoreMin"]
		maxPostLength = paraDict["postLenMax"]
		minPostLength = paraDict["postLenMin"]
		maxDate = paraDict["epochScoreMax"]
		minDate = paraDict["epochScoreMin"]
		cosineParam = paraDict["cosineParam"]
		pageScoreParam = paraDict["pageScoreParam"]
		postScoreParam = paraDict["postScoreParam"]
		epochScoreParam = paraDict["epochScoreParam"]
		postLenParam = paraDict["postLenParam"]
		static = True
		if(static ) :
			maxPageScore = max(pageScore)
			minPageScore = min(pageScore)
			minPostScore = max(postScore)
			maxPostScore = min(postScore)
			maxCosineScore = max(cosine)
			minCosineScore = min(cosine)
			maxPostLength = max(postLen)
			minPostLength = min(postLen)
			maxDate = max(epochTime)
			minDate = min(epochTime)
			pageScoreParam = 0.1
			cosineScoreParam = 0.7
			postScoreParam = 0.1
			epochScoreParam = 0.1	
			postLenParam = 0.0
		index = 0
		while index < len(cosine) :
			if (float(maxCosineScore) - float(minCosineScore)) > 0  :
				cosineNorm[index] = (float(cosine[index]) - float(minCosineScore))	/ (float(maxCosineScore) - float(minCosineScore))
			if (float(maxPageScore) - float(minPageScore)) > 0 :
				pageScoreNorm[index] = (float(pageScore[index]) - float(minPageScore)) / (float(maxPageScore) - float(minPageScore))
			if (float(maxPostScore) - float(minPostScore)) > 0 :
				postScoreNorm[index] = (float(postScore[index]) - float(minPostScore)) / (float(maxPostScore) - float(minPostScore))
			if (float(maxPostLength) - float(minPostLength)) > 0 :
				postLenNorm[index] = (float(postLen[index]) - float(minPostLength)) / (float(maxPostLength) - float(minPostLength))
			if (float(maxDate) - float(minDate) ) :
				epochTimeNorm[index] = (float(epochTime[index]) - float(minDate)) / (float(maxDate) - float(minDate))

		        val = cosineParam * (float(cosineNorm[index])) + pageScoreParam*(float(pageScoreNorm[index])) + postScoreParam*(float(postScoreNorm[index])) + 0*(float(postLenNorm[index])) + epochScoreParam *(float(epochTimeNorm[index]))
			ppIDScore.append([iden[index],copy(val),cosineNorm[index],pageScoreNorm[index],postScoreNorm[index],postLenNorm[index],epochTimeNorm[index],postList[index]])
			index = index + 1
                index = 0
		ppIDScore.sort(key=itemgetter(1),reverse=True)
		#while index < len(cosine) :
		#	print "ID = ",ppIDScore[index][0]," score = ",ppIDScore[index][1]
		#	index = index + 1
		createTestcase = False;

		if( createTestcase ) :
			fo = open("./testcase/"+query, "wb+")
			index = 0	
			while index < len(cosine) and index<32:
				fo.write(postList[index])
				fo.write("\n")
				fo.write("$$$$\nSTART|")
				fo.write(str(cosine[index])+"|"+str(pageScore[index])+"|"+str(postScore[index])+"|"+str(epochTime[index])+"|"+str(postLen[index])+"||" )
				fo.write("\n$$$$\n")
				index = index + 1
			fo.close()	
				
	return ppIDScore	
print "reached end"	
