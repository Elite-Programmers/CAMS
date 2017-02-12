spool table.txt;

DROP TABLE ATT CASCADE CONSTRAINT;
DROP TABLE FAC_ENR CASCADE CONSTRAINT;
DROP TABLE WRITE_TEST CASCADE CONSTRAINT;
DROP TABLE TEST_SUB CASCADE CONSTRAINT;
DROP TABLE TEST_TME CASCADE CONSTRAINT;
DROP TABLE DEPT_SUB_ENR CASCADE CONSTRAINT;
DROP TABLE STUDENT_SEM_ENR CASCADE CONSTRAINT;
DROP TABLE STUDENT_LIST CASCADE CONSTRAINT;
DROP TABLE CLASS_TCHR CASCADE CONSTRAINT;
DROP TABLE FACULTY_LIST CASCADE CONSTRAINT;
DROP TABLE CAMS_LOGIN CASCADE CONSTRAINT;

DROP SEQUENCE QSATT;
DROP SEQUENCE QSFID;
DROP SEQUENCE QSWT;
DROP SEQUENCE QSTS;
DROP SEQUENCE QSTNO;
DROP SEQUENCE QSSNOR;
DROP SEQUENCE QSENR;
DROP SEQUENCE QSCFID;

CREATE SEQUENCE QSCFID;
CREATE SEQUENCE QSENR;
CREATE SEQUENCE QSSNOR;
CREATE SEQUENCE QSTNO;
CREATE SEQUENCE QSTS;
CREATE SEQUENCE QSWT;
CREATE SEQUENCE QSFID;
CREATE SEQUENCE QSATT;

CREATE TABLE CAMS_LOGIN(
  USERID VARCHAR2(10),
  PASSWORD VARCHAR2(10),
  CONSTRAINT CAMS_LOGIN_PRIME PRIMARY KEY (USERID) ENABLE
);

CREATE TABLE FACULTY_LIST(
  FID VARCHAR2(7),
  NAME VARCHAR2(30) NOT NULL,
  DESIGNATION VARCHAR2(30) NOT NULL,
  BRANCH VARCHAR2(2),
  CONSTRAINT FACULTY_LIST_PRIME PRIMARY KEY (FID),
  CONSTRAINT FACULTY_LIST_FOREIGN FOREIGN KEY (FID) REFERENCES CAMS_LOGIN (USERID) ENABLE
);

CREATE TABLE CLASS_TCHR(
  SCFID NUMBER,
  FID VARCHAR2(7),
  SECTION VARCHAR2(1) NOT NULL,
  SEM NUMBER,
  YEAR NUMBER,
  CONSTRAINT CLASS_TCHR_PRIME PRIMARY KEY (SCFID) ENABLE,
  CONSTRAINT CLASS_TCHR_CHECK_SEM CHECK (SEM BETWEEN 1 AND 8) ENABLE,
  CONSTRAINT CLASS_TCHR_FOREIGN_FID FOREIGN KEY (FID) REFERENCES FACULTY_LIST (FID) ENABLE
);

CREATE UNIQUE INDEX CLASS_TCHR_UNIQUE ON CLASS_TCHR (FID,SEM,YEAR);

CREATE TABLE STUDENT_LIST(
  USN VARCHAR2(10),
  SNAME VARCHAR2(30),
  YEAR_OF_JOINING VARCHAR2(4),
  ADDRESS VARCHAR2(300),
  PARENT_PHNO NUMBER,
  PHNO NUMBER,
  CONSTRAINT STUDENT_LIST_PRIME PRIMARY KEY (USN) ENABLE,
  CONSTRAINT STUDENT_LIST_FOREIGN FOREIGN KEY (USN) REFERENCES CAMS_LOGIN (USERID) ENABLE
);

CREATE TABLE STUDENT_SEM_ENR(
  SENR NUMBER,
  USN VARCHAR2(10),
  BRANCH VARCHAR2(2),
  SEM NUMBER CONSTRAINT STUDENT_SEM_ENR_CHK CHECK(SEM BETWEEN 1 AND 8) ENABLE,
  BATCH NUMBER,
  SECTION VARCHAR2(1),
  YEAR NUMBER,
  CONSTRAINT STUDENT_SEM_ENR_PRIME PRIMARY KEY(SENR) ENABLE,
  CONSTRAINT STUDENT_SEM_ENR_FOREIGN_USN FOREIGN KEY (USN) REFERENCES STUDENT_LIST(USN) ENABLE
);

CREATE UNIQUE INDEX STUDENT_SEM_ENR_UNIQUE ON STUDENT_SEM_ENR (USN,SEM,SECTION,YEAR);


CREATE TABLE DEPT_SUB_ENR(
  SSNOR NUMBER,
  SCODE VARCHAR2(8),
  SNAME VARCHAR2(80),
  BRANCH VARCHAR2(2),
  CONSTRAINT DEPT_SUB_ENR_PRIME PRIMARY KEY(SSNOR) ENABLE
  );

CREATE UNIQUE INDEX DEPT_SUB_ENR_UNIQUE ON DEPT_SUB_ENR (SCODE,BRANCH);


CREATE TABLE TEST_TME(
  STNO NUMBER,
  TNO NUMBER CONSTRAINT TEST_TME_CHK_TNO CHECK (TNO BETWEEN 1 AND 3) ENABLE,
  DTE DATE,
  SLOT VARCHAR2(1) CONSTRAINT TEST_TME_CHK_SLOT CHECK (SLOT='A' OR SLOT='M') ENABLE,
  CONSTRAINT TEST_TME_PRIME PRIMARY KEY (STNO) ENABLE
 );

CREATE UNIQUE INDEX TEST_TME_UNIQUE ON TEST_TME (TNO,DTE,SLOT);


CREATE TABLE TEST_SUB(
  STS NUMBER,
  TTNO NUMBER,
  SCODE VARCHAR2(8),
  CONSTRAINT TEST_SUB_FOREIGN FOREIGN KEY (TTNO) REFERENCES TEST_TME (STNO) ENABLE,
  CONSTRAINT TEST_SUB_PRIME PRIMARY KEY(STS) ENABLE
);

CREATE UNIQUE INDEX TEST_SUB_UNIQUE ON TEST_SUB (TTNO,SCODE);


CREATE TABLE WRITE_TEST(
  SWT NUMBER,
  USN VARCHAR(10),
  SURT NUMBER,
  SCORE NUMBER,
  CONSTRAINT WRITE_TEST_PRIME PRIMARY KEY(SWT) ENABLE,
  CONSTRAINT WRITE_TEST_FOREIGN_SURT FOREIGN KEY(SURT) REFERENCES TEST_SUB(STS) ENABLE,
  CONSTRAINT WRITE_TEST_FOREIGN_USN FOREIGN KEY(USN) REFERENCES STUDENT_LIST(USN) ENABLE
);

CREATE UNIQUE INDEX WRITE_TEST_UNIQUE ON WRITE_TEST (USN,SCORE);
CREATE UNIQUE INDEX WRITE_TEST_FOREIGN ON WRITE_TEST (SURT,USN);



CREATE TABLE FAC_ENR(
  SFID NUMBER,
  FID VARCHAR2(7),
  SLOT NUMBER CONSTRAINT FAC_ENR_CHK_SLOT CHECK (SLOT BETWEEN 1 AND 7) ENABLE,
  DAY VARCHAR2(3),
  SECTION VARCHAR2(1) NOT NULL,
  BRANCH VARCHAR2(2),
  YEAR NUMBER,
  SCODE VARCHAR2(8),
  CONSTRAINT FAC_ENR_PRIME PRIMARY KEY (SFID) ENABLE,
  CONSTRAINT FAC_ENR_FOREIGN FOREIGN KEY (FID) REFERENCES FACULTY_LIST (FID) ENABLE
);

CREATE UNIQUE INDEX FAC_ENR_UNIQUE ON FAC_ENR (FID,SLOT,DAY,YEAR);


CREATE TABLE ATT(
  SATT NUMBER,
  USN VARCHAR2(10),
  YEAR DATE,
  SLOT NUMBER CONSTRAINT ATT_CHK_SLOT CHECK (SLOT BETWEEN 1 AND 7) ENABLE,
  SCODE VARCHAR2(8),
  POA VARCHAR2(1),
  CONSTRAINT ATT_PRIME PRIMARY KEY (SATT) ENABLE,
  CONSTRAINT ATT_FOREIGN_USN FOREIGN KEY(USN) REFERENCES STUDENT_LIST(USN) ENABLE
);

CREATE UNIQUE INDEX ATT_UNIQUE ON ATT (USN,YEAR,SLOT);

CREATE TRIGGER TRG_CLASS_TCHR
  BEFORE INSERT ON CLASS_TCHR
    FOR EACH ROW
      BEGIN
        SELECT QSCFID.NEXTVAL INTO :NEW.SCFID FROM DUAL;
      END;
    /

CREATE TRIGGER TRG_STUDENT_SEM_ENR
  BEFORE INSERT ON STUDENT_SEM_ENR
    FOR EACH ROW
      BEGIN
        SELECT QSENR.NEXTVAL INTO :NEW.SENR FROM DUAL;
      END;
    /

CREATE TRIGGER TRG_DEPT_SUB_ENR
  BEFORE INSERT ON DEPT_SUB_ENR
    FOR EACH ROW
      BEGIN
        SELECT QSSNOR.NEXTVAL INTO :NEW.SSNOR FROM DUAL;
      END;
    /

CREATE TRIGGER TRG_TEST_TME
  BEFORE INSERT ON TEST_TME
    FOR EACH ROW
      BEGIN
        SELECT QSTNO.NEXTVAL INTO :NEW.STNO FROM DUAL;
      END;
    /

CREATE TRIGGER TRG_TEST_SUB
  BEFORE INSERT ON TEST_SUB
    FOR EACH ROW
      BEGIN
        SELECT QSTS.NEXTVAL INTO :NEW.STS FROM DUAL;
      END;
    /

CREATE TRIGGER TRG_WRITE_TEST
    BEFORE INSERT ON WRITE_TEST
      FOR EACH ROW
        BEGIN
          SELECT QSWT.NEXTVAL INTO :NEW.SWT FROM DUAL;
        END;
      /

CREATE TRIGGER TRG_FAC_ENR
      BEFORE INSERT ON FAC_ENR
        FOR EACH ROW
          BEGIN
            SELECT QSFID.NEXTVAL INTO :NEW.SFID FROM DUAL;
          END;
        /

CREATE TRIGGER TRG_ATT
  BEFORE INSERT ON ATT
    FOR EACH ROW
      BEGIN
        SELECT QSATT.NEXTVAL INTO :NEW.SATT FROM DUAL;
      END;
    /

spool off;
