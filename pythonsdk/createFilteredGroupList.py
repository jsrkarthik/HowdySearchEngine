import simplejson as json
fo_filter = open("filteredGroupList.txt","wb+")
fo = open("completeGroupInfo.txt","r")
categorySet = set()
count = 0
pageList = []
pageIDSet = set()
likesThreshold = 0
for line in fo :
	count = count + 1
	data = json.loads(line)
	link = str("")
	description = str("")
	city = str("")
	country = str("")
	group_id = ""
	name = data["name"]
	print line
	if "id" in data :
		page_id = data["id"]
	if "description" in data :
		description = data["description"]
	if "venue" in data :
		if "city" in data["venue"] :
			city = data["venue"]["city"]
		if "country" in data["venue"] :
			country = data["venue"]["country"]
	if "link" in data :
		link = data["link"]
	final = description+" "+link+" "
	if((page_id not in pageIDSet) and (country == "United States" or country == "")) :
		pageIDSet.add(page_id)
		#if(city != "College Station") :
		#	continue
		if not ( name.find("Texas A&M") == -1) :
			pageList.append([name,page_id,link])	
			json.dump(data,fo_filter)
			fo_filter.write("\n")
			continue
		elif not( link.find("tamu.edu") ==-1 ) :
			json.dump(data,fo_filter)
			fo_filter.write("\n")
			pageList.append([name,page_id,link])
			continue
		elif not( final.find("Texas A&M") == -1 and final.find("tamu.edu")==-1) :
			json.dump(data,fo_filter)
			fo_filter.write("\n")
			pageList.append([name,page_id,link])
print "length of groupList = ",len(pageList)
#fo_filter.close()
fo = open("groupTable.data","wb+")	
for page in pageList :
		print "Writing page"
		print page[0],"  ",page[1]	
		fo.write("SNL1990%s,,,%s,,,%d,,,%s,,,%dSNL1990" %(page[0].encode('utf-8'),page[1].encode('utf-8'),int(25), page[2].encode('utf-8'), bool(0)))
print "length of groupList = ",len(pageList)
fo.close()
