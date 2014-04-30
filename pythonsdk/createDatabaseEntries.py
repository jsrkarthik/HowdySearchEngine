import simplejson as json
import re
import os
from facepy import GraphAPI
from facepy import utils
import time
count = 0
path = "./pagePostDir"
count = 0
ACCESS_TOKEN_INDEX = 0
'''ACCESS_TOKEN = ["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"]

app_id = [1476062702607954,1423599847894702,429608827184078,274845076022600,616788648389516,637905736263864,228874263988094,266704943502322,1439939002913252,487631031365300] # must be integer

app_secret = ["dcaa2a6dd1a5c18e068d05341b572395", "9462507246f74057edae911b257f2688","33845e9c47d8686f2b69e125f98243a1","acfd0ed8aaa57cbc9f83a9331b6940f9", "6a66b1a04c12a1330531868e9f959dab","9a8996e83661c2f6396edb47c75371c0","4a70de2698eb320837ae4438066483e3","8aa4800630cf5094a3cd840317ca7027","e022ab250088ec8044cdae7fdaba31fa","92812f8a945ff3611a026756cc4c29ac"]
index = 0
while index < len(ACCESS_TOKEN) :
	#short lived access token generated from the facebook developers site
	USER_ACCESS_TOKEN = ACCESS_TOKEN[index]
	#generating long lived access tokeb from the short lived access token 
	try :
		ACCESS_TOKEN[index], expires_at = utils.get_extended_access_token(USER_ACCESS_TOKEN, app_id[index], app_secret[index])
	except Exception as error_message :
		print error_message
		if error_message[1:3] == "190" :
			print "Error code 190..continuing, index = ",index
		index = index + 1
		continue
	index = index+1
	print "long_lived_ACCESS_TOKEN = ",  ACCESS_TOKEN[index-1]
	print "expires at = ",expires_at

print ACCESS_TOKEN
sleep(1000)'''
fo = open("pagePostTable.data","ab+")
ACCESS_TOKEN = ['CAAUZBeKEOHlIBAH7b0hBAYHnuA6AjZA05qRFnWZBAzgSbxmMwXdjpzB62o6B5Ex8R1lBUNKGJUlUGlhA0FzhVguq8vJLZB7vVnzE8UzAFAkfkWcnyDD2H0yGHmzqO62m7UL8AWtsZCO9tA3JlauT4JmTScjunsOJ80g4N9AwpW4m5ppdbcq0GgQsu3CBXrzMZD', 'CAAUOwas8bq4BAIqn2DsczdWfPaad6UQR1QbKR93SuhkvIQCx76VLr267uARewqSE4EHSrjxKhZCvCv9YrZAyCOMZA0cJNdk8wLa152gVguUq704R3qMGdTRZAUs0rtesUC14iVzx4QI7B7dTLp2pi3RMM8SWZBa8LPT6YlnhFllwDCD8bAZAjQ', 'CAAGGuhmJY84BAAhBBHwk15C5yvlOxZAArT5Ml2dsTbcxVskZA1Hb3GOZBjs7ITCR8GZABCgDRHZA22Yed9GrOjIccW3GZBvSh2SWNFfhtcG4BdzdOkHc4dbFKrKZBbJiLyOOIQtYjhXRv8UUv3ZBE8t59YFPZB3sXk8m7QDEy6qUs3L0vkLgK4bj7', 'CAAD5ZBFsf5UgBAAfiiDFvkWEsZBZC1zkeeawaqZCVDbG221BJPxkoMV1xXAmbhteXE5ATH1Nd1ZCblyeOdehANxZA0wK9ZAQIaF8j3QSGG4UZCw0BpP0X2C5ZB9nlJG2L6LeqSDJezZBhHb06pSN8SaXXCDnrg2NXZC4JzdxYZARzFOHvRZCPZBVGXrMmFF0eZA8RZCM03kZD','CAAIw90xJ64wBAGHd9EF46uzrQZACrEqf7SuCsvvaJwlrwZBiTznIp3eofPrvdgIknVTyCpOhc3HYkLl6dZCAzOgRyIhJGU5mu227vu4ReZAZA7aCmRmkhmIkGJcVrqlfzJBX0F37bx4KZBRCEB6LGHtaVN7pfuJcD8aLeTA7MU9w5ZC5ZCgJqvRVb8MipZAWZAZCxsZD', 'CAAJELADPaLgBADltf6NAydZAcf2dV8KzCsJFxufWTB4Keoh7GtZBgCjJ0xFcfKbJkpY5VTf16wgabHGnxdIZC2ZB5Vemq7M6ThizHZA9sCiSWVSLuSwImAVZCZAk1MZAPuM8SCwR3KJZAd6YwibjxXO56SMtJAFxkOskvIgtgqEFZBrthM7VEhwLzzA0KEt1OfOaMZD','CAADQKPE0B34BAPGuZApLYuBMIt5RAGoZAZBl95CkcdZAR1ObHMu3hZCYLSFFquKL2sQMVbPDWCpsU2eGvvyMLB2j3zVEekkrbNpZC3Hro1uQZBLeBOTNJ6RqFRWfjzMffJ1YCDseWa5QcJXDQYy36YzouC7SRmna0PdWSQ5WZCJMX7nW6tIjbGjmH3qb4t5zwr0ZD', 'CAADykRVq0ZCIBAHKGnYEsRMLr0FbZB6chP6KOiPSaoygUgF4ITyHhup4cYGCDZBshf56wKTMnwkSuHdfHMfmofBexrDKk89oQOnmE25OjbNNrcaJgtSzjtL3SOpUZAHjpOZCPsDSbjKbMEePUaHZCa2C6rJKRVvZADP9WNjZBu0ZCU5ZAgbi436XYY', 'CAAUdnezEUeQBAIjEFAOFHpXcHZB0995PzDA24ZCGCKQM2gSZBmc5v4gTpmC0ingCXBjiQ1mstRSX7Mpr4tW9Ui27wIMzmO1SX8IqMxs2ph23ydoeaFZAMuBfCWMKEQH0V7P1BmUHgxJnYk6dHIhDF2ylihAQATOZBqn3lC1MDZBLvUYQ4VHpMr', 'CAAG7f3Jn7rQBAMEx2ANgoFkGvpZCa1aTMbjJg6JVW2j6ZAKi9VZCwTKFWjkDU8pNlaTgBFuo2y6TM2rRuzW1PqDCd9rhJ818pHdYyVA7TLLJsuQ3i8aXkJ4AZBQcUb9FhZCBhaZCcxO8azCN0lKnrpkScftdWpakDrVxr7Qd0P52x2ZA43m3oW5JtwKjsGuElkZD']
graph = GraphAPI(ACCESS_TOKEN[ACCESS_TOKEN_INDEX]);

#Creating PostTable Entries
startTime = time.time()
for root,dirs,files in os.walk(path):
	for page in files :
		print "page = ",page
		if page.endswith(".txt") :
			cFile = open(os.path.join(root,page),"r")
			for line in cFile :
				if(count > 30416) :
					pageID = str("0")
					postID = str("0")
					date =  str(" ")
					objectID = str(" ")
					data = json.loads(line)
					if not "message" in data.keys() :
						continue
					pageID = int(data["from"]["id"])
					print "postID full = ",data["id"],
					postID = int((data["id"].split('_'))[1])
					print "actual postID = ",postID
					likes = int(0)
					shares = int(0)
					comments = int(0)
					if(count !=0 and count%600 == 0) :
						endTime = time.time();
						print "count = ",count
						print "time elapsed =",endTime-startTime
						time.sleep(10)
						ACCESS_TOKEN_INDEX = ACCESS_TOKEN_INDEX + 1
						if(ACCESS_TOKEN_INDEX == 10 ) :
							ACCESS_TOKEN_INDEX = 0 
						isCheck = 1
						while(isCheck ) :
							isCheck = 0
							try:
        	   					        graph = GraphAPI(ACCESS_TOKEN[ACCESS_TOKEN_INDEX])
        						except Exception as error_message:
								print "error_message = ",error_message
								sleep_time = 10
        	    						if error_message[3:4] == "17" :
									sleep_time = 1900
								if error_message[1:3] == "613" :
									sleep_time = 600
	                					print "Sleeping for %d seconds." %(sleep_time)
	                					time.sleep(sleep_time) 
								isCheck = 1
					isCheck = 1
					while( isCheck ) :
						isCheck = 0
						try:
        	   			        	likeData = graph.get("/fql?q=SELECT%20like_info.like_count,%20comment_info.comment_count,%20share_count%20FROM%20stream%20WHERE%20post_id%20=%20%22"+data["id"]+"%22")
        					except Exception as error_message:
							print "error_message = ",error_message
							sleep_time = 10
        	    					if error_message[3:4] == "17" :
								sleep_time = 1800
							if error_message[1:3] == "613" :
								sleep_time = 600
	                				print "Sleeping for %d seconds." %(sleep_time)
	                				time.sleep(sleep_time) 
							isCheck = 1
					print "like Data = ",likeData, "count = ",count, "timeElapsed = ",time.time()-startTime
	                                commentData = []
					if(len(likeData["data"]) > 0) :
						likes = likeData["data"][0]["like_info"]["like_count"];
						comments = likeData["data"][0]["comment_info"]["comment_count"]
					print "likes = ",likes,"comments = ",comments
					if "shares" in data :
						shares = int(data["shares"]["count"])
					author = "NILESH"
					date = (data["created_time"].split('T'))[0]
					post = data["message"]
					objectID = 0
					if "object_id" in data :
						objectID = str(data["object_id"])
					fo.write("SNL1990%s,,,%s,,,%d,,,%d,,,%d,,,%s,,,%s,,,%s,,,%s,,,%dSNL1990" %(str(postID),str(pageID),likes,comments,shares,author,date,objectID,post.encode('utf-8'),bool(1)))
				count = count + 1
fo.close()
print "Count = ",count
#creating PageTable Entries

'''
path = "./groupPostDir"
groupCount = 0
fo = open("groupPostTable.data","ab+")
#Creating PostTable Entries
for root,dirs,files in os.walk(path):
	for page in files :
		print "page = ",page
		if page.endswith(".txt") :
			cFile = open(os.path.join(root,page),"r")
			for line in cFile :
				pageID = str("0")
				postID = str("0")
				date =  str(" ")
				objectID = str(" ")
				data = json.loads(line)
				if not "message" in data.keys() :
					continue
				pageID = int(data["from"]["id"])
				print "postID full = ",data["id"],
				postID = int((data["id"].split('_'))[1])
				print "actual postID = ",postID
				likes = int(0)
				shares = int(0)
				comments = int(0)
				if(count !=0 and count%600 == 0) :
					endTime = time.time();
					print "count = ",count
					print "time elapsed =",endTime-startTime
					time.sleep(10)
					ACCESS_TOKEN_INDEX = ACCESS_TOKEN_INDEX + 1
					if(ACCESS_TOKEN_INDEX == 10 ) :
						ACCESS_TOKEN_INDEX = 0
					try:
           				        graph = GraphAPI(ACCESS_TOKEN[ACCESS_TOKEN_INDEX])
        				except Exception as error_message:
						sleep_time = 10
            					if not (error_message.find("17") == -1) :
							sleep_time = 1800
						if error_message[1:3] == "613" :
							sleep_time = 600
                				print "Sleeping for %d seconds." %(sleep_time)
                				time.sleep(sleep_time) 
				likeData = graph.get("/fql?q=SELECT%20like_info.like_count,%20comment_info.comment_count,%20share_count%20FROM%20stream%20WHERE%20post_id%20=%20%22"+data["id"]+"%22")
				print "like Data = ",likeData, "count = ",count, "timeElapsed = ",time.time()-startTime 
				if(len(likeData["data"]) > 0 ):
					likes = likeData["data"][0]["like_info"]["like_count"];
					comments = likeData["data"][0]["comment_info"]["comment_count"]
				if "shares" in data :
					shares = int(data["shares"]["count"])
				author = "NILESH"
				date = (data["created_time"].split('T'))[0]
				post = data["message"]
				objectID = 0
				if "object_id" in data :
					objectID = str(data["object_id"])
				fo.write("SNL1990%s,,,%s,,,%d,,,%d,,,%d,,,%s,,,%s,,,%s,,,%s,,,%dSNL1990" %(str(postID),str(pageID),likes,comments,shares,author,date,objectID,post.encode('utf-8'),bool(0)))
				groupCount = groupCount + 1
				count = count + 1
fo.close()
print "Count = ",count	
print "groupCount = ", groupCount
#creating groupTable Entries'''

