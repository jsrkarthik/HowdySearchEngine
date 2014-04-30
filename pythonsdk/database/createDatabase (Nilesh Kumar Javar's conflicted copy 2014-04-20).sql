DROP DATABASE IF EXISTS `nkj255-db1`;
CREATE DATABASE `nkj255-db1`;
use nkj255-db1;

CREATE TABLE PageInfo( pageName VARCHAR(50), pageID INT, likes INT, PRIMARY KEY(pageID));

CREATE TABLE PostInfo( postID VARCHAR(50), pageID VARCHAR(50), likes INT, shares INT, author VARCHAR(50),date VARCHAR(15), objectID INT, post VARCHAR(1000) CHARACTER SET utf8 COLLATE utf8_unicode_ci, PRIMARY KEY(postID, pageID));

LOAD DATA LOCAL INFILE '/home/javar/Desktop/Dropbox/IRProject/pythonsdk/postTable.data' INTO TABLE PostInfo FIELDS TERMINATED BY ',,,' LINES TERMINATED BY 'SNL1990' STARTING BY 'SNL1990';
