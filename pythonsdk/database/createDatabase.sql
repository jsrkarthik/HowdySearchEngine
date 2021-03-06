

DROP DATABASE IF EXISTS `nkj255-db1`;
CREATE DATABASE `nkj255-db1`;
use nkj255-db1;

CREATE TABLE PageInfo( pageName VARCHAR(50), pageID VARCHAR(50), likes INT, pageLink VARCHAR(1000), isPage bool DEFAULT 1, PRIMARY KEY(pageID));

CREATE TABLE PostInfo( postID VARCHAR(50), pageID VARCHAR(50), likes INT, comments INT, shares INT, author VARCHAR(50),date VARCHAR(15), objectID VARCHAR(50), post VARCHAR(10000) CHARACTER SET utf8 COLLATE utf8_unicode_ci, isPage bool DEFAULT 1, PRIMARY KEY (postID, pageID));

LOAD DATA LOCAL INFILE '/home/javar/Desktop/Dropbox/IRProject/pythonsdk/pageTable.data' INTO TABLE PageInfo FIELDS TERMINATED BY ',,,' LINES TERMINATED BY 'SNL1990' STARTING BY 'SNL1990';

LOAD DATA LOCAL INFILE '/home/javar/Desktop/Dropbox/IRProject/pythonsdk/groupTable.data' INTO TABLE PageInfo FIELDS TERMINATED BY ',,,' LINES TERMINATED BY 'SNL1990' STARTING BY 'SNL1990';

LOAD DATA LOCAL INFILE '/home/javar/Desktop/Dropbox/IRProject/pythonsdk/pagePostTable.data' INTO TABLE PostInfo FIELDS TERMINATED BY ',,,' LINES TERMINATED BY 'SNL1990' STARTING BY 'SNL1990';

LOAD DATA LOCAL INFILE '/home/javar/Desktop/Dropbox/IRProject/pythonsdk/groupPostTable.data' INTO TABLE PostInfo FIELDS TERMINATED BY ',,,' LINES TERMINATED BY 'SNL1990' STARTING BY 'SNL1990';
