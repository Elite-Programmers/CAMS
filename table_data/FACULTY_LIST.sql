LOAD DATA INFILE 'FACULTY_LIST.csv'
INTO TABLE FACULTY_LIST
APPEND FIELDS TERMINATED BY ','
(FID,NAME,DESIGNATION,BRANCH)