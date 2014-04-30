from facepy import GraphAPI
from facepy import utils
import simplejson as json

app_id = 1476062702607954 # must be integer

app_secret = "dcaa2a6dd1a5c18e068d05341b572395" 

ACCESS_TOKEN = "CAAUZBeKEOHlIBAD3BBzVODnZB1jkv2o8sHhZBHz5GNZC9ZCMujTr64NbZCn83uxmq3M3U5tyaxe3TUd4IQ20IGCKCMpcaf1HiZBLGHO6dcahUCZAtkK4yolCiJjRgXMywiiRZC9NI5aretMLhiY76IJL6HqgCMAAUkkDnK1AVXdB9L83ACnUPtxXn"
#fo = open("filteredPageList.txt","r")
fo = open("filteredGroupList.txt","r")
pages = []
page = []
count = 0
for line in fo :
	#print "line =",line
	#if(count > 50) :
	#	break
	data = json.loads(line)
	pages.append([data["name"],data["id"]])
	count = count + 1
print pages	
graph = GraphAPI(ACCESS_TOKEN);
#results = graph.get("/155828851146262/posts?limit=200&until=2013-12-31")
#print "results = ", results
pageCount = 0;
for page in pages :
	print "total : ", len(pages)," count = ",pageCount," page = ",page 
	if(pageCount > -1 ) :
		pageID = page[1]
		pageName = page[0]
		fileName = "./groupPostDir/"+pageName+".txt"
		#results = graph.get("/"+str(pageID)+"/posts?limit=200&until=2014-04-05")
		results = graph.get("/"+str(pageID)+"/feed?limit=200&until=2013-12-31")
		fo_pageInfo = open(fileName,"wb+")
		fo_pageInfo.close()
		fo_pageInfo = open(fileName,"ab+")
		count = 0
		stopFlag = 0
		while(  len(results['data']) > 0 and stopFlag == 0) :
			count = 0
			for result in results['data'] :
				if "message" in result.keys() :
					if(count%25 == 0) :
						date = result['created_time']	
						date = date.split('-')
						#print "date = ",date[0],"-",date[1],"-",date[2]
						if(int(date[0]) <= 2009) :
							stopFlag = 1
							break
							count = 0	
					json.dump(result,fo_pageInfo)
					fo_pageInfo.write("\n")
					count = count + 1
			next_page = results['paging']['next']
			split_next_page = next_page.split("com")
			results = graph.get(split_next_page[1])
			count = count + 1
		fo_pageInfo.close()
	pageCount = pageCount + 1
