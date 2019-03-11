from sqlalchemy import create_engine,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import pymongo
import time
import hashlib
import random
import mysql_module
import mongodb_module
import jsonGenerator

engine = create_engine("mysql+mysqldb://root:A12A12A12@ar8327k.top:3308/A12")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
m2 = hashlib.md5()

UUID_List = []
UID_List = []
Aname_List = []
AID_List = []

class AAMAP(Base):
    __tablename__ = 'AAMAP'
    AID = Column(String(50),primary_key=True,unique=True,index=True,nullable=False)
    Aname = Column(String(100))

class UUMAP(Base):
    __tablename__ = 'UUMAP'
    UID = Column(String(50),primary_key=False,nullable=False)
    UUID = Column(String(50),primary_key=True,nullable=True,index=True,unique=True)

#Fill UUID,UID,Aname lists. For no MySQL insert dry run.

for i in range(10):
    Aname_List.append('事件' + str(i))
    UID_List.append(str(i))
    UUID_List.append(m2.hexdigest())
    AID_List.append(i)
"""
#Generate AA TABLE
for i in range(10):
    session.add(AAMAP(AID=str(i),Aname=('事件'+str(i))))
    Aname_List.append('事件'+str(i))

#Generate UU TABLE
for i in range(10):
    m2.update(str(i).encode())
    session.add(UUMAP(UID=str(i),UUID=m2.hexdigest()))
    UUID_List.append(m2.hexdigest())
    UID_List.append(str(i))

session.commit()
"""
#Generate all mongo
for i in range(10):
    r = session.query(AAMAP).filter(AAMAP.AID == str(random.randint(0, 9))) #Pick random action
    random_UUID_index = random.randint(0,9)
    uhash = mongodb_module.sync_updateUserAction(UUID_List[random_UUID_index],list(session.execute(r))[0][0]) #Pick random user
    properties = {'Properties1':'1','Properties2':'2','Properties3':'3','Properties4':'4'}
    mongodb_module.sync_updateActionProperties(uhash,jsonGenerator.generateJson(properties)) #Write action properties

attributes = {'Attribute1':'1','Attribute2':'2','Attribute3':'3'}

for uuid in UUID_List:
    mongodb_module.sync_updateUserArritbutes(uuid,jsonGenerator.generateJson(attributes)) #Write user attributes

"""  AIDs = [3,2,5,1]
    creaate_filiter("漏斗1",AIDs)
    AIDs = [3,2,7]
    creaate_filiter("漏斗2",AIDs)
"""