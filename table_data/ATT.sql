LOAD DATA INFILE 'ATT.csv'
INTO TABLE ATT
APPEND FIELDS TERMINATED BY ','
(USN,YEAR,SLOT,SCODE,DAY)