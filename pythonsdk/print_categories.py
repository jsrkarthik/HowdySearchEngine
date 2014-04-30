import simplejson as json
fo_filter = open("FilteredPageList.txt","wb+")
fo = open("completePageInfo.txt","r")
categorySet = set()
count = 0
pageList = []
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
	final = mission+" "+affiliation+" "+description+" "+about+" "
	if(city != "College Station") :
		continue
	if not ( name.find("Texas A&M") == -1) :
		pageList.append([name,page_id,likes])	
		json.dump(data,fo_filter)
		fo_filter.write("\n")
		continue
	elif not( website.find("tamu.edu") ==-1 ) :
		json.dump(data,fo_filter)
		fo_filter.write("\n")
		pageList.append([name,page_id,likes])
		continue
	elif not( final.find("Texas A&M")== -1) :
		json.dump(data,fo_filter)
		fo_filter.write("\n")
		pageList.append([name,page_id,likes])
print "length of pageList = ",len(pageList)
fo = open("pageTable.data","wb+")	
for page in pageList :
	print "Page = ", page
	if(page[2] > 500 ) :
		print "Writing page"
		print page[0],"  ",page[1],"  ",page[2]	
		fo.write("SNL1990%s,,,%s,,,%dSNL1990\n" %(page[0],page[1],int(page[2])))
fo.close()
