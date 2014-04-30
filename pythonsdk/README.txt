facebook_getToken_final.py - This file has tokens and setup to get the list of pages from facebook and the list is stored in completePageInfo.txt. 

createFilteredPageList.py - This file contains code to generate the filtered pageList based on their relation to TAMU and the list of pages is dumped into file filteredPageList.txt

getPagePost.py - The file to retrieve the post of year 2012-2013 and creates a file by the name of the page in directory pagePostDir

createDatabaseEntries.py this file creates the posts in form of database entries. The file pageTable.data contains all the entries serialized from the all the pages

./database/createDatabase.sql This file contains the scripts to create and load the database once logged onto the server.

Command to log on to database : mysql -h localhost -u root -p --local-infile=1 


