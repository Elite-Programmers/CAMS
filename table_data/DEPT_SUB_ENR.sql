LOAD DATA INFILE 'DEPT_SUB_ENR.csv'
INTO TABLE DEPT_SUB_ENR
APPEND FIELDS TERMINATED BY ','
(SCODE,SNAME,BRANCH)