LOAD DATA INFILE 'STUDENT_SEM_ENR.csv'
INTO TABLE STUDENT_SEM_ENR
APPEND FIELDS TERMINATED BY ','
(USN,BRANCH,SEM,SECTION,YEAR,BATCH)