import MySQLdb as mdb
import querying as ql
from copy import copy
from operator import itemgetter
while(1) :
	query = raw_input("Enter Query")
	if(query == 'exit'):
        	break;
	cosineResults = ql.querying(query)
	con = mdb.connect('localhost', 'root', 'javar', 'nkj255-db1')
	if(len(cosineResults) == 1 and cosineResults[0]==-1) :
		break;
	print "Cosine Rsults  = ",cosineResults
        with con :
        	cur = con.cursor(mdb.cursors.DictCursor)
		cosine = []
		ppIDScore = []
		pageScore = []
		postScore = []
		postLen = []
        	for postPageId in cosineResults:
			postId = postPageId[0].split("_")[1]
			pageId = postPageId[0].split("_")[0]	
                  	cur.execute("SELECT * FROM PostInfo,PageInfo WHERE PageInfo.pageID = PostInfo.pageID  and PostInfo.postID=%s and PostInfo.pageID=%s ORDER BY date ASC",(postId,pageId))
                  	row = cur.fetchone()
			if not row :
				continue 
			print "row = ",row
		        cosine.append( float(postPageId[1]) )	
			likes = row["likes"]
			comments = row["comments"]
			shares = row["shares"]
			pageLikes = row["PageInfo.likes"]
			postScore.append( likes+shares+comments	)
			pageScore.append( pageLikes )
			postLen.append(len(row["post"]))
			print "postId = ",postId," pageId = ",pageId	
		maxPageScore = max(pageScore)
		minPageScore = min(pageScore)
		maxPostScore = max(postScore)
		minPostScore = min(postScore)
		maxCosineScore = float (max(cosine))
		minCosineScore = float (min(cosine))
		maxPostLength = max(postLen)
		minPostLength = min(postLen)
		index = 0
		while index < len(cosine) :
			if (float(maxCosineScore) - float(minCosineScore)) > 0  :
				cosine[index] = (float(cosine[index]) - float(minCosineScore))	/ (float(maxCosineScore) - float(minCosineScore))
			if (float(maxPageScore) - float(minPageScore)) > 0 :
				pageScore[index] = (float(pageScore[index]) - float(minPageScore)) / (float(maxPageScore) - float(minPageScore))
			if (float(maxPostScore) - float(minPostScore)) > 0 :`
				postScore[index] = (float(postScore[index]) - float(minPostScore)) / (float(maxPostScore) - float(minPostScore))
			if (float(maxPostLength) - float(minPostLength)) > 0 :`
				postLen[index] = (float(postLen[index]) - float(postLenScore)) / (float(postLenScore) - float(postLenScore))
		        val = 0.7* (float(cosine[index])) + 0.1*(float(pageScore[index])) + 0.1*(float(postScore[index])) + 0.1*(float(postLen[index]))
			ppIDScore.append([cosineResults[index][0],copy(val)])
			index = index + 1
		index = 0
		ppIDScore.sort(key=itemgetter(1),reverse=True)
		while index < len(cosine) :
			print "ID = ",ppIDScore[index][0]," score = ",ppIDScore[index][1]
			index = index + 1
		
