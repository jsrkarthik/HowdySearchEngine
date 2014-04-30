import simplejson as json
#fo_filter = open("filteredPageList.txt","wb+")
fo = open("completePageInfo.txt","r")
categorySet = set()
count = 0
pageList = []
pageIDSet = set()
likesThreshold = 0
for line in fo :
	count = count + 1
	data = json.loads(line)
	webiste = str("")
	mission = str("")
	affiliation = str("")
	likes = ("0")
	description = str("")
	about = str("")
	city = str("")
	page_id = ""
	link = ""
	name = data["name"]
	if "id" in data :
		page_id = data["id"]
	if "website" in data :
		website = data["website"]
	if "mission" in data :
		mission = data["mission"]
	if "affiliation" in data :
		affiliation = data["affiliation"]
	if "likes" in data :
		likes = data["likes"]
	if "description" in data :
		description = data["description"]
	if "about" in data:
		about = data["about"]
	if "location" in data :
		if "city" in data["location"] :
			city = data["location"]["city"]
	if "link" in data :
		link = data["link"]
	final = mission+" "+affiliation+" "+description+" "+about+" "
	if((page_id not in pageIDSet) and (int(likes) > likesThreshold )) :
		pageIDSet.add(page_id)
		if(city != "College Station") :
			continue
		if not ( name.find("Texas A&M") == -1) :
			pageList.append([name,page_id,likes,link])	
			#json.dump(data,fo_filter)
			#fo_filter.write("\n")
			continue
		elif not( website.find("tamu.edu") ==-1 ) :
			#json.dump(data,fo_filter)
			#fo_filter.write("\n")
			pageList.append([name,page_id,likes,link])
			continue
		elif not( final.find("Texas A&M")== -1) :
			#json.dump(data,fo_filter)
			#fo_filter.write("\n")
			pageList.append([name,page_id,likes,link])
print "length of pageList = ",len(pageList)
#fo_filter.close()
fo = open("pageTable.data","wb+")	
for page in pageList :
	print "Page = ", page
	if(page[2] > likesThreshold ) :
		print "Writing page"
		print page[0],"  ",page[1],"  ",page[2]," ",page[3]	
		fo.write("SNL1990%s,,,%s,,,%d,,,%s,,,%dSNL1990" %(page[0],page[1],int(page[2]),page[3],bool(1)))
print "length of pageList = ",len(pageList)
fo.close()
