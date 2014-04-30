#Script to get the access token
#Steps in case if token expires :
#	1. I have created an app in facebook developers website : developers.facebook.com under APPS tab.
#	App id :      1476062702607954
# 	App Secret :  dcaa2a6dd1a5c18e068d05341b572395		
# 	2. In the graph explorer tool under the tools tab in the same website
#	   select your application and hit getAccessToken
#	3. use the same access_token as assigned below. The token expires on May# 	21st 11:35am
#		
import sys
#import json
import simplejson as json
import facebook
import urllib2
from facepy import GraphAPI
from facepy import utils
import time
app_id = 1476062702607954 # must be integer

app_secret = "dcaa2a6dd1a5c18e068d05341b572395" 

ACCESS_TOKEN = "CAAUZBeKEOHlIBAD3BBzVODnZB1jkv2o8sHhZBHz5GNZC9ZCMujTr64NbZCn83uxmq3M3U5tyaxe3TUd4IQ20IGCKCMpcaf1HiZBLGHO6dcahUCZAtkK4yolCiJjRgXMywiiRZC9NI5aretMLhiY76IJL6HqgCMAAUkkDnK1AVXdB9L83ACnUPtxXn"

''' short lived access token generated from the facebook developers site
USER_ACCESS_TOKEN = 'CAAUZBeKEOHlIBABKJ3H6ZCduupTYWKf3EhCA1i9ORsQ4ldHNDBbq9njO6ZBQ9ykaV2jlGkD8ZBaz99GsvvrnZCfYuFAKu6g11n60tE00cP1aYKlytFzZA1GabU2lAa6u3sz8SZA3CPcvtSAQLgEAyy4xNKmzYqUGzB2Xo8yoZCB5ZCir5MYEMDZAFBVEHZBafOjZCzfXaeF8FGCFrAZDZD'
generating long lived access tokeb from the short lived access token 
long_lived_access_token, expires_at = utils.get_extended_access_token(USER_ACCESS_TOKEN, app_id, app_secret)
print "long_lived_ACCESS_TOKEN = ",  long_lived_access_token
print "expires at = ",expires_at'''


graph = GraphAPI(ACCESS_TOKEN);
queryList = ["*\"Texas AND A\&M\"*","TAMU","Aggie","aggie"]
fo = open("complete_search_page2.txt", "wb+")
fo.close()
fo = open("complete_search_page2.txt","a+")
categoryList = set()
pageList = []
fo1 = open("CompletePageList.txt","wb+")
fo_pageInfo = open("completePageInfo.txt","wb+")
for query in queryList :
	graphQueryStr = '/search?q=\"'+query+'\"&type=page'
	results = graph.get(graphQueryStr)
	while(len(results['data'])>0 ) :
		for result in results['data'] :
			temp = []
			temp.append(result['name'])
			temp.append(result['id'])
			page_result = graph.get(result['id'])
			print "pageResult = ",page_result
			json.dump(page_result,fo_pageInfo)
			fo_pageInfo.write("\n")
			pageList.append(temp)
			categoryList.add(result['category'])
			json.dump(result['name'],fo1)
			fo1.write(" ")
			json.dump(result['id'],fo1)
			fo1.write("\n")
			json.dump(result,fo)	
			fo.write("\n")
		next_page = results['paging']['next']
		split_next_page = next_page.split("com")
		results = graph.get(split_next_page[1])
		print "In Loop"        
fo1.close()
fo_pageInfo.close()
fieldList = set()
print "len of pageList = ",len(pageList)	
count = 0
for page in pageList :
	print "page = ",page[0].encode('utf-8'), " count = ", count
	if (count == 800) :
		time.sleep(5)
		count = 0
	count = count + 1
	page_result = graph.get(str(page[1]))
	for field in page_result :
		fieldList.add(field)
	#about, description, mission,
print "All field = "
for field in fieldList  :
	print field
print page_result
json.dump(results,fo)
fo.close()

