-- ------------------------------------------------------
--  File created - Friday-September-06-2019   
-- ------------------------------------------------------
-- ------------------------------------------------------
--  DDL for Table BICYCLE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`BICYCLE` 
   (	`SERIALNUMBER` DECIMAL(38,0), 
	`CUSTOMERID` DECIMAL(38,0) DEFAULT 0, 
	`MODELTYPE` VARCHAR(50), 
	`PAINTID` DECIMAL(38,0) DEFAULT 0, 
	`FRAMESIZE` DOUBLE DEFAULT 0, 
	`ORDERDATE` DATETIME, 
	`STARTDATE` DATETIME, 
	`SHIPDATE` DATETIME, 
	`SHIPEMPLOYEE` DECIMAL(38,0) DEFAULT 0, 
	`FRAMEASSEMBLER` DECIMAL(38,0) DEFAULT 0, 
	`PAINTER` DECIMAL(38,0) DEFAULT 0, 
	`CONSTRUCTION` VARCHAR(50) DEFAULT 'Bonded', 
	`WATERBOTTLEBRAZEONS` DECIMAL(38,0) DEFAULT 4, 
	`CUSTOMNAME` VARCHAR(50), 
	`LETTERSTYLEID` VARCHAR(50), 
	`STOREID` DECIMAL(38,0) DEFAULT 0, 
	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0, 
	`TOPTUBE` DOUBLE DEFAULT 0, 
	`CHAINSTAY` DOUBLE DEFAULT 0, 
	`HEADTUBEANGLE` DOUBLE DEFAULT 0, 
	`SEATTUBEANGLE` DOUBLE DEFAULT 0, 
	`LISTPRICE` DECIMAL(38,4) DEFAULT 0, 
	`SALEPRICE` DECIMAL(38,4) DEFAULT 0, 
	`SALESTAX` DECIMAL(38,4) DEFAULT 0, 
	`SALESTATE` VARCHAR(50), 
	`SHIPPRICE` DECIMAL(38,4) DEFAULT 0, 
	`FRAMEPRICE` DECIMAL(38,4) DEFAULT 0, 
	`COMPONENTLIST` DECIMAL(38,4) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table BICYCLETUBEUSAGE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`BICYCLETUBEUSAGE` 
   (	`SERIALNUMBER` DECIMAL(38,0) DEFAULT 0, 
	`TUBEID` DECIMAL(38,0) DEFAULT 0, 
	`QUANTITY` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table BIKEPARTS
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`BIKEPARTS` 
   (	`SERIALNUMBER` DECIMAL(38,0) DEFAULT 0, 
	`COMPONENTID` DECIMAL(38,0) DEFAULT 0, 
	`SUBSTITUTEID` DECIMAL(38,0) DEFAULT 0, 
	`LOCATION` VARCHAR(50), 
	`QUANTITY` DECIMAL(38,0) DEFAULT 0, 
	`DATEINSTALLED` DATETIME, 
	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table BIKETUBES
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`BIKETUBES` 
   (	`SERIALNUMBER` DECIMAL(38,0) DEFAULT 0, 
	`TUBENAME` VARCHAR(50), 
	`TUBEID` DECIMAL(38,0) DEFAULT 0, 
	`LENGTH` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table CITY
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`CITY` 
   (	`CITYID` DECIMAL(38,0), 
	`ZIPCODE` VARCHAR(50), 
	`CITY` VARCHAR(50), 
	`STATE` VARCHAR(50), 
	`AREACODE` VARCHAR(50), 
	`POPULATION1990` DECIMAL(38,0) DEFAULT 0, 
	`POPULATION1980` DECIMAL(38,0) DEFAULT 0, 
	`COUNTRY` VARCHAR(50), 
	`LATITUDE` DOUBLE DEFAULT 0, 
	`LONGITUDE` DOUBLE DEFAULT 0, 
	`POPULATIONCDF` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table COMMONSIZES
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`COMMONSIZES` 
   (	`MODELTYPE` VARCHAR(50), 
	`FRAMESIZE` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table COMPONENT
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`COMPONENT` 
   (	`COMPONENTID` DECIMAL(38,0) DEFAULT 0, 
	`MANUFACTURERID` DECIMAL(38,0) DEFAULT 0, 
	`PRODUCTNUMBER` VARCHAR(50), 
	`ROAD` VARCHAR(50), 
	`CATEGORY` VARCHAR(50), 
	`LENGTH` DOUBLE DEFAULT 0, 
	`HEIGHT` DOUBLE DEFAULT 0, 
	`WIDTH` DOUBLE DEFAULT 0, 
	`WEIGHT` DOUBLE DEFAULT 0, 
	`YEAR` DECIMAL(38,0), 
	`ENDYEAR` DECIMAL(38,0), 
	`DESCRIPTION` VARCHAR(100), 
	`LISTPRICE` DECIMAL(38,4) DEFAULT 0, 
	`ESTIMATEDCOST` DECIMAL(38,4) DEFAULT 0, 
	`QUANTITYONHAND` DOUBLE DEFAULT 10
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table COMPONENTNAME
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`COMPONENTNAME` 
   (	`COMPONENTNAME` VARCHAR(50), 
	`ASSEMBLYORDER` DECIMAL(38,0) DEFAULT 0, 
	`DESCRIPTION` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table CUSTOMER
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`CUSTOMER` 
   (	`CUSTOMERID` DECIMAL(38,0), 
	`PHONE` VARCHAR(50), 
	`FIRSTNAME` VARCHAR(50), 
	`LASTNAME` VARCHAR(50), 
	`ADDRESS` VARCHAR(50), 
	`ZIPCODE` VARCHAR(50), 
	`CITYID` DECIMAL(38,0) DEFAULT 0, 
	`BALANCEDUE` DECIMAL(38,4) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table CUSTOMERTRANSACTION
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`CUSTOMERTRANSACTION` 
   (	`CUSTOMERID` DECIMAL(38,0) DEFAULT 0, 
	`TRANSACTIONDATE` DATETIME, 
	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0, 
	`AMOUNT` DECIMAL(38,4) DEFAULT 0, 
	`DESCRIPTION` VARCHAR(250), 
	`REFERENCE` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table EMPLOYEE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`EMPLOYEE` 
   (	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0, 
	`TAXPAYERID` VARCHAR(50), 
	`LASTNAME` VARCHAR(50), 
	`FIRSTNAME` VARCHAR(50), 
	`HOMEPHONE` VARCHAR(50), 
	`ADDRESS` VARCHAR(50), 
	`ZIPCODE` VARCHAR(50), 
	`CITYID` DECIMAL(38,0) DEFAULT 0, 
	`DATEHIRED` DATETIME, 
	`DATERELEASED` DATETIME, 
	`CURRENTMANAGER` DECIMAL(38,0) DEFAULT 0, 
	`SALARYGRADE` DECIMAL(38,0) DEFAULT 0, 
	`SALARY` DECIMAL(38,4) DEFAULT 0, 
	`TITLE` VARCHAR(100), 
	`WORKAREA` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table GROUPCOMPONENTS
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`GROUPCOMPONENTS` 
   (	`GROUPID` DECIMAL(38,0) DEFAULT 0, 
	`COMPONENTID` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table GROUPO
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`GROUPO` 
   (	`COMPONENTGROUPID` DECIMAL(38,0), 
	`GROUPNAME` VARCHAR(50), 
	`BIKETYPE` VARCHAR(50), 
	`YEAR` DECIMAL(38,0), 
	`ENDYEAR` DECIMAL(38,0), 
	`WEIGHT` DECIMAL(15,4)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table LETTERSTYLE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`LETTERSTYLE` 
   (	`LETTERSTYLE` VARCHAR(50), 
	`DESCRIPTION` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table MANUFACTURER
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`MANUFACTURER` 
   (	`MANUFACTURERID` DECIMAL(38,0), 
	`MANUFACTURERNAME` VARCHAR(50), 
	`CONTACTNAME` VARCHAR(50), 
	`PHONE` VARCHAR(50), 
	`ADDRESS` VARCHAR(50), 
	`ZIPCODE` VARCHAR(50), 
	`CITYID` DECIMAL(38,0) DEFAULT 0, 
	`BALANCEDUE` DECIMAL(38,4) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table MANUFACTURERTRANSACTION
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`MANUFACTURERTRANSACTION` 
   (	`MANUFACTURERID` DECIMAL(38,0) DEFAULT 0, 
	`TRANSACTIONDATE` DATETIME, 
	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0, 
	`AMOUNT` DECIMAL(38,4) DEFAULT 0, 
	`DESCRIPTION` VARCHAR(250), 
	`REFERENCE` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table MODELSIZE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`MODELSIZE` 
   (	`MODELTYPE` VARCHAR(50), 
	`MSIZE` DOUBLE DEFAULT 0, 
	`TOPTUBE` DOUBLE DEFAULT 0, 
	`CHAINSTAY` DOUBLE DEFAULT 0, 
	`TOTALLENGTH` DOUBLE DEFAULT 0, 
	`GROUNDCLEARANCE` DOUBLE DEFAULT 0, 
	`HEADTUBEANGLE` DOUBLE DEFAULT 0, 
	`SEATTUBEANGLE` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table MODELTYPE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`MODELTYPE` 
   (	`MODELTYPE` VARCHAR(50), 
	`DESCRIPTION` VARCHAR(50), 
	`COMPONENTID` DECIMAL(38,0)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table PAINT
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`PAINT` 
   (	`PAINTID` DECIMAL(38,0), 
	`COLORNAME` VARCHAR(50), 
	`COLORSTYLE` VARCHAR(50) DEFAULT 'Solid', 
	`COLORLIST` VARCHAR(50), 
	`DATEINTRODUCED` DATETIME, 
	`DATEDISCONTINUED` DATETIME
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table PREFERENCE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`PREFERENCE` 
   (	`ITEMNAME` VARCHAR(50), 
	`VALUE` DOUBLE DEFAULT 0, 
	`DESCRIPTION` VARCHAR(250), 
	`DATECHANGED` DATETIME
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table PURCHASEITEM
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`PURCHASEITEM` 
   (	`PURCHASEID` DECIMAL(38,0) DEFAULT 0, 
	`COMPONENTID` DECIMAL(38,0) DEFAULT 0, 
	`PRICEPAID` DECIMAL(38,4) DEFAULT 0, 
	`QUANTITY` DECIMAL(38,0) DEFAULT 0, 
	`QUANTITYRECEIVED` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table PURCHASEORDER
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`PURCHASEORDER` 
   (	`PURCHASEID` DECIMAL(38,0), 
	`EMPLOYEEID` DECIMAL(38,0) DEFAULT 0, 
	`MANUFACTURERID` DECIMAL(38,0) DEFAULT 0, 
	`TOTALLIST` DECIMAL(38,4) DEFAULT 0, 
	`SHIPPINGCOST` DECIMAL(38,4) DEFAULT 0, 
	`DISCOUNT` DECIMAL(38,4) DEFAULT 0, 
	`ORDERDATE` DATETIME, 
	`RECEIVEDATE` DATETIME, 
	`AMOUNTDUE` DECIMAL(38,4) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table RETAILSTORE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`RETAILSTORE` 
   (	`STOREID` DECIMAL(38,0), 
	`STORENAME` VARCHAR(50), 
	`PHONE` VARCHAR(50), 
	`CONTACTFIRSTNAME` VARCHAR(50), 
	`CONTACTLASTNAME` VARCHAR(50), 
	`ADDRESS` VARCHAR(50), 
	`ZIPCODE` VARCHAR(50), 
	`CITYID` DECIMAL(38,0) DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table REVISIONHISTORY
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`REVISIONHISTORY` 
   (	`ID` DECIMAL(38,0), 
	`VERSION` VARCHAR(50), 
	`CHANGEDATE` DATETIME, 
	`NAME` VARCHAR(50), 
	`REVISIONCOMMENTS` VARCHAR(250)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table SAMPLENAME
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`SAMPLENAME` 
   (	`ID` DECIMAL(38,0), 
	`LASTNAME` VARCHAR(50), 
	`FIRSTNAME` VARCHAR(50), 
	`GENDER` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table SAMPLESTREET
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`SAMPLESTREET` 
   (	`ID` DECIMAL(38,0), 
	`BASEADDRESS` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table STATETAXRATE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`STATETAXRATE` 
   (	`STATE` VARCHAR(50), 
	`TAXRATE` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table TEMPDATEMADE
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`TEMPDATEMADE` 
   (	`DATEVALUE` DATETIME, 
	`MADECOUNT` DOUBLE DEFAULT 0
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table TUBEMATERIAL
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`TUBEMATERIAL` 
   (	`TUBEID` DECIMAL(38,0) DEFAULT 0, 
	`MATERIAL` VARCHAR(50), 
	`DESCRIPTION` VARCHAR(100), 
	`DIAMETER` DOUBLE DEFAULT 0, 
	`THICKNESS` DOUBLE DEFAULT 0, 
	`ROUNDNESS` VARCHAR(50), 
	`WEIGHT` DOUBLE DEFAULT 0, 
	`STIFFNESS` DOUBLE DEFAULT 0, 
	`LISTPRICE` DECIMAL(38,4) DEFAULT 1, 
	`CONSTRUCTION` VARCHAR(50) DEFAULT 'Bonded'
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Table WORKAREA
-- ------------------------------------------------------

  CREATE TABLE `BIKE_SHOP`.`WORKAREA` 
   (	`WORKAREA` VARCHAR(50), 
	`DESCRIPTION` VARCHAR(50)
   ) 
    NO INMEMORY ;
-- ------------------------------------------------------
--  DDL for Index PK_BICYCLE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_BICYCLE` ON `BIKE_SHOP`.`BICYCLE` (`SERIALNUMBER`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_BICYCLETUBEUSAGE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_BICYCLETUBEUSAGE` ON `BIKE_SHOP`.`BICYCLETUBEUSAGE` (`SERIALNUMBER`, `TUBEID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_BIKEPARTS
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_BIKEPARTS` ON `BIKE_SHOP`.`BIKEPARTS` (`SERIALNUMBER`, `COMPONENTID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_BIKETUBES
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_BIKETUBES` ON `BIKE_SHOP`.`BIKETUBES` (`SERIALNUMBER`, `TUBENAME`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_CITY
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_CITY` ON `BIKE_SHOP`.`CITY` (`CITYID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_COMMONSIZES
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_COMMONSIZES` ON `BIKE_SHOP`.`COMMONSIZES` (`MODELTYPE`, `FRAMESIZE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_COMPONENT
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_COMPONENT` ON `BIKE_SHOP`.`COMPONENT` (`COMPONENTID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_COMPONENTNAME
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_COMPONENTNAME` ON `BIKE_SHOP`.`COMPONENTNAME` (`COMPONENTNAME`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_CUSTOMER
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_CUSTOMER` ON `BIKE_SHOP`.`CUSTOMER` (`CUSTOMERID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_CUSTOMERTRANSACTION
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_CUSTOMERTRANSACTION` ON `BIKE_SHOP`.`CUSTOMERTRANSACTION` (`CUSTOMERID`, `TRANSACTIONDATE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_EMPLOYEE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_EMPLOYEE` ON `BIKE_SHOP`.`EMPLOYEE` (`EMPLOYEEID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_GROUPCOMPONENTS
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_GROUPCOMPONENTS` ON `BIKE_SHOP`.`GROUPCOMPONENTS` (`GROUPID`, `COMPONENTID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_GROUPO
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_GROUPO` ON `BIKE_SHOP`.`GROUPO` (`COMPONENTGROUPID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_LETTERSTYLE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_LETTERSTYLE` ON `BIKE_SHOP`.`LETTERSTYLE` (`LETTERSTYLE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_MANUFACTURER
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_MANUFACTURER` ON `BIKE_SHOP`.`MANUFACTURER` (`MANUFACTURERID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_MANUFTRANSACTION
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_MANUFTRANSACTION` ON `BIKE_SHOP`.`MANUFACTURERTRANSACTION` (`MANUFACTURERID`, `TRANSACTIONDATE`, `REFERENCE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_MODELSIZE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_MODELSIZE` ON `BIKE_SHOP`.`MODELSIZE` (`MODELTYPE`, `MSIZE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_MODELTYPE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_MODELTYPE` ON `BIKE_SHOP`.`MODELTYPE` (`MODELTYPE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_PAINT
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_PAINT` ON `BIKE_SHOP`.`PAINT` (`PAINTID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_PREFERENCE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_PREFERENCE` ON `BIKE_SHOP`.`PREFERENCE` (`ITEMNAME`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_PURCHASEITEM
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_PURCHASEITEM` ON `BIKE_SHOP`.`PURCHASEITEM` (`PURCHASEID`, `COMPONENTID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_PURCHASEORDER
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_PURCHASEORDER` ON `BIKE_SHOP`.`PURCHASEORDER` (`PURCHASEID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_RETAILSTORE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_RETAILSTORE` ON `BIKE_SHOP`.`RETAILSTORE` (`STOREID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_REVISIONHISTORY
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_REVISIONHISTORY` ON `BIKE_SHOP`.`REVISIONHISTORY` (`ID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_SAMPLENAME
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_SAMPLENAME` ON `BIKE_SHOP`.`SAMPLENAME` (`ID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_SAMPLESTREET
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_SAMPLESTREET` ON `BIKE_SHOP`.`SAMPLESTREET` (`ID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_STATETAXRATE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_STATETAXRATE` ON `BIKE_SHOP`.`STATETAXRATE` (`STATE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_TEMPDATEMADE
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_TEMPDATEMADE` ON `BIKE_SHOP`.`TEMPDATEMADE` (`DATEVALUE`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_TUBEMATERIAL
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_TUBEMATERIAL` ON `BIKE_SHOP`.`TUBEMATERIAL` (`TUBEID`) 
  ;
-- ------------------------------------------------------
--  DDL for Index PK_WORKAREA
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `BIKE_SHOP`.`PK_WORKAREA` ON `BIKE_SHOP`.`WORKAREA` (`WORKAREA`) 
  ;
-- ------------------------------------------------------
--  Constraints for Table BICYCLE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `PK_BICYCLE` PRIMARY KEY (`SERIALNUMBER`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table BICYCLETUBEUSAGE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BICYCLETUBEUSAGE` ADD CONSTRAINT `PK_BICYCLETUBEUSAGE` PRIMARY KEY (`SERIALNUMBER`, `TUBEID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table BIKEPARTS
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BIKEPARTS` ADD CONSTRAINT `PK_BIKEPARTS` PRIMARY KEY (`SERIALNUMBER`, `COMPONENTID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table BIKETUBES
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BIKETUBES` ADD CHECK (TubeName IN ('Top', 'Seat', 'Rear', 'Chain', 'Down', 'Front'));
  ALTER TABLE `BIKE_SHOP`.`BIKETUBES` ADD CONSTRAINT `PK_BIKETUBES` PRIMARY KEY (`SERIALNUMBER`, `TUBENAME`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table CITY
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`CITY` ADD CONSTRAINT `PK_CITY` PRIMARY KEY (`CITYID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table COMMONSIZES
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`COMMONSIZES` ADD CONSTRAINT `PK_COMMONSIZES` PRIMARY KEY (`MODELTYPE`, `FRAMESIZE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table COMPONENT
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`COMPONENT` ADD CONSTRAINT `PK_COMPONENT` PRIMARY KEY (`COMPONENTID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table COMPONENTNAME
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`COMPONENTNAME` ADD CONSTRAINT `PK_COMPONENTNAME` PRIMARY KEY (`COMPONENTNAME`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table CUSTOMER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`CUSTOMER` ADD CONSTRAINT `PK_CUSTOMER` PRIMARY KEY (`CUSTOMERID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table CUSTOMERTRANSACTION
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`CUSTOMERTRANSACTION` ADD CONSTRAINT `PK_CUSTOMERTRANSACTION` PRIMARY KEY (`CUSTOMERID`, `TRANSACTIONDATE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table EMPLOYEE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`EMPLOYEE` ADD CONSTRAINT `PK_EMPLOYEE` PRIMARY KEY (`EMPLOYEEID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table GROUPCOMPONENTS
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`GROUPCOMPONENTS` ADD CONSTRAINT `PK_GROUPCOMPONENTS` PRIMARY KEY (`GROUPID`, `COMPONENTID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table GROUPO
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`GROUPO` ADD CONSTRAINT `PK_GROUPO` PRIMARY KEY (`COMPONENTGROUPID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table LETTERSTYLE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`LETTERSTYLE` ADD CONSTRAINT `PK_LETTERSTYLE` PRIMARY KEY (`LETTERSTYLE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table MANUFACTURER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MANUFACTURER` ADD CONSTRAINT `PK_MANUFACTURER` PRIMARY KEY (`MANUFACTURERID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table MANUFACTURERTRANSACTION
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MANUFACTURERTRANSACTION` ADD CONSTRAINT `PK_MANUFTRANSACTION` PRIMARY KEY (`MANUFACTURERID`, `TRANSACTIONDATE`, `REFERENCE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table MODELSIZE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MODELSIZE` ADD CONSTRAINT `PK_MODELSIZE` PRIMARY KEY (`MODELTYPE`, `MSIZE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table MODELTYPE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MODELTYPE` ADD CONSTRAINT `PK_MODELTYPE` PRIMARY KEY (`MODELTYPE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table PAINT
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PAINT` ADD CHECK (ColorStyle IN ('Solid', 'Two Color', 'Three Color', 'Special'));
  ALTER TABLE `BIKE_SHOP`.`PAINT` ADD CONSTRAINT `PK_PAINT` PRIMARY KEY (`PAINTID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table PREFERENCE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PREFERENCE` ADD CONSTRAINT `PK_PREFERENCE` PRIMARY KEY (`ITEMNAME`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table PURCHASEITEM
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PURCHASEITEM` ADD CONSTRAINT `PK_PURCHASEITEM` PRIMARY KEY (`PURCHASEID`, `COMPONENTID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table PURCHASEORDER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PURCHASEORDER` ADD CONSTRAINT `PK_PURCHASEORDER` PRIMARY KEY (`PURCHASEID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table RETAILSTORE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`RETAILSTORE` ADD CONSTRAINT `PK_RETAILSTORE` PRIMARY KEY (`STOREID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table REVISIONHISTORY
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`REVISIONHISTORY` ADD CONSTRAINT `PK_REVISIONHISTORY` PRIMARY KEY (`ID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table SAMPLENAME
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`SAMPLENAME` ADD CHECK (Gender IN ('M', 'F'));
  ALTER TABLE `BIKE_SHOP`.`SAMPLENAME` ADD CONSTRAINT `PK_SAMPLENAME` PRIMARY KEY (`ID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table SAMPLESTREET
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`SAMPLESTREET` ADD CONSTRAINT `PK_SAMPLESTREET` PRIMARY KEY (`ID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table STATETAXRATE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`STATETAXRATE` ADD CONSTRAINT `PK_STATETAXRATE` PRIMARY KEY (`STATE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table TEMPDATEMADE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`TEMPDATEMADE` ADD CONSTRAINT `PK_TEMPDATEMADE` PRIMARY KEY (`DATEVALUE`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table TUBEMATERIAL
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`TUBEMATERIAL` ADD CONSTRAINT `PK_TUBEMATERIAL` PRIMARY KEY (`TUBEID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Constraints for Table WORKAREA
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`WORKAREA` ADD CONSTRAINT `PK_WORKAREA` PRIMARY KEY (`WORKAREA`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS NOLOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `STUDENTS`  ENABLE;
-- ------------------------------------------------------
--  Ref Constraints for Table BICYCLE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKEMODELTYPE` FOREIGN KEY (`MODELTYPE`)
	  REFERENCES `BIKE_SHOP`.`MODELTYPE` (`MODELTYPE`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKEEMPLOYEE` FOREIGN KEY (`EMPLOYEEID`)
	  REFERENCES `BIKE_SHOP`.`EMPLOYEE` (`EMPLOYEEID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKERETAIL` FOREIGN KEY (`STOREID`)
	  REFERENCES `BIKE_SHOP`.`RETAILSTORE` (`STOREID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKECUSTOMER` FOREIGN KEY (`CUSTOMERID`)
	  REFERENCES `BIKE_SHOP`.`CUSTOMER` (`CUSTOMERID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKELETTER` FOREIGN KEY (`LETTERSTYLEID`)
	  REFERENCES `BIKE_SHOP`.`LETTERSTYLE` (`LETTERSTYLE`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLE` ADD CONSTRAINT `FK_BIKEPAINT` FOREIGN KEY (`PAINTID`)
	  REFERENCES `BIKE_SHOP`.`PAINT` (`PAINTID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table BICYCLETUBEUSAGE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BICYCLETUBEUSAGE` ADD CONSTRAINT `FK_REFERENCE26` FOREIGN KEY (`SERIALNUMBER`)
	  REFERENCES `BIKE_SHOP`.`BICYCLE` (`SERIALNUMBER`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BICYCLETUBEUSAGE` ADD CONSTRAINT `FK_REFERENCE27` FOREIGN KEY (`TUBEID`)
	  REFERENCES `BIKE_SHOP`.`TUBEMATERIAL` (`TUBEID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table BIKEPARTS
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BIKEPARTS` ADD CONSTRAINT `FK_REFERENCE24` FOREIGN KEY (`SERIALNUMBER`)
	  REFERENCES `BIKE_SHOP`.`BICYCLE` (`SERIALNUMBER`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BIKEPARTS` ADD CONSTRAINT `FK_REFERENCE4` FOREIGN KEY (`EMPLOYEEID`)
	  REFERENCES `BIKE_SHOP`.`EMPLOYEE` (`EMPLOYEEID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BIKEPARTS` ADD CONSTRAINT `FK_REFERENCE5` FOREIGN KEY (`COMPONENTID`)
	  REFERENCES `BIKE_SHOP`.`COMPONENT` (`COMPONENTID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table BIKETUBES
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`BIKETUBES` ADD CONSTRAINT `FK_REFERENCE6` FOREIGN KEY (`SERIALNUMBER`)
	  REFERENCES `BIKE_SHOP`.`BICYCLE` (`SERIALNUMBER`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`BIKETUBES` ADD CONSTRAINT `FK_TUBEMATERIALBIKETUBES` FOREIGN KEY (`TUBEID`)
	  REFERENCES `BIKE_SHOP`.`TUBEMATERIAL` (`TUBEID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table COMPONENT
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`COMPONENT` ADD CONSTRAINT `FK_REFERENCE` FOREIGN KEY (`CATEGORY`)
	  REFERENCES `BIKE_SHOP`.`COMPONENTNAME` (`COMPONENTNAME`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`COMPONENT` ADD CONSTRAINT `FK_REFERENCE16` FOREIGN KEY (`MANUFACTURERID`)
	  REFERENCES `BIKE_SHOP`.`MANUFACTURER` (`MANUFACTURERID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table CUSTOMER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`CUSTOMER` ADD CONSTRAINT `FK_CITYCUSTOMER` FOREIGN KEY (`CITYID`)
	  REFERENCES `BIKE_SHOP`.`CITY` (`CITYID`);
-- ------------------------------------------------------
--  Ref Constraints for Table CUSTOMERTRANSACTION
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`CUSTOMERTRANSACTION` ADD CONSTRAINT `FK_REFERENCE18` FOREIGN KEY (`CUSTOMERID`)
	  REFERENCES `BIKE_SHOP`.`CUSTOMER` (`CUSTOMERID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table EMPLOYEE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`EMPLOYEE` ADD CONSTRAINT `FK_CITYEMPLOYEE` FOREIGN KEY (`CITYID`)
	  REFERENCES `BIKE_SHOP`.`CITY` (`CITYID`);
-- ------------------------------------------------------
--  Ref Constraints for Table GROUPCOMPONENTS
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`GROUPCOMPONENTS` ADD CONSTRAINT `FK_REFERENCE14` FOREIGN KEY (`COMPONENTID`)
	  REFERENCES `BIKE_SHOP`.`COMPONENT` (`COMPONENTID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`GROUPCOMPONENTS` ADD CONSTRAINT `FK_REFERENCE15` FOREIGN KEY (`GROUPID`)
	  REFERENCES `BIKE_SHOP`.`GROUPO` (`COMPONENTGROUPID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table MANUFACTURER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MANUFACTURER` ADD CONSTRAINT `FK_CITYMANUFACTURER` FOREIGN KEY (`CITYID`)
	  REFERENCES `BIKE_SHOP`.`CITY` (`CITYID`);
-- ------------------------------------------------------
--  Ref Constraints for Table MANUFACTURERTRANSACTION
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MANUFACTURERTRANSACTION` ADD CONSTRAINT `FK_MANUFTRANS` FOREIGN KEY (`MANUFACTURERID`)
	  REFERENCES `BIKE_SHOP`.`MANUFACTURER` (`MANUFACTURERID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table MODELSIZE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`MODELSIZE` ADD CONSTRAINT `FK_MODELTYPE` FOREIGN KEY (`MODELTYPE`)
	  REFERENCES `BIKE_SHOP`.`MODELTYPE` (`MODELTYPE`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table PURCHASEITEM
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PURCHASEITEM` ADD CONSTRAINT `FK_REFERENCE20` FOREIGN KEY (`PURCHASEID`)
	  REFERENCES `BIKE_SHOP`.`PURCHASEORDER` (`PURCHASEID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`PURCHASEITEM` ADD CONSTRAINT `FK_REFERENCE21` FOREIGN KEY (`COMPONENTID`)
	  REFERENCES `BIKE_SHOP`.`COMPONENT` (`COMPONENTID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table PURCHASEORDER
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`PURCHASEORDER` ADD CONSTRAINT `FK_REFERENCE22` FOREIGN KEY (`MANUFACTURERID`)
	  REFERENCES `BIKE_SHOP`.`MANUFACTURER` (`MANUFACTURERID`) ON DELETE CASCADE;
  ALTER TABLE `BIKE_SHOP`.`PURCHASEORDER` ADD CONSTRAINT `FK_REFERENCE23` FOREIGN KEY (`EMPLOYEEID`)
	  REFERENCES `BIKE_SHOP`.`EMPLOYEE` (`EMPLOYEEID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table RETAILSTORE
-- ------------------------------------------------------

  ALTER TABLE `BIKE_SHOP`.`RETAILSTORE` ADD CONSTRAINT `FK_CITYRETAILSTORE` FOREIGN KEY (`CITYID`)
	  REFERENCES `BIKE_SHOP`.`CITY` (`CITYID`);
