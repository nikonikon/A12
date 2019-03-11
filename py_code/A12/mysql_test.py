"""
MySQL [A12]> desc AAMAP;
+-------+-----------+------+-----+---------+-------+
| Field | Type      | Null | Key | Default | Extra |
+-------+-----------+------+-----+---------+-------+
| AID   | char(50)  | NO   | PRI | NULL    |       |
| Aname | char(100) | YES  |     | NULL    |       |
+-------+-----------+------+-----+---------+-------+
2 rows in set (0.147 sec)

MySQL [A12]> desc UUMAP;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| UUID  | char(50) | NO   | PRI | NULL    |       |
| UID   | char(50) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
2 rows in set (0.149 sec)

"""
from sqlalchemy import create_engine,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
engine = create_engine("mysql+mysqldb://root:A12A12A12@ar8327k.top:3308/A12")

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class AAMAP(Base):
    __tablename__ = 'AAMAP'
    AID = Column(String(50),primary_key=True,unique=True,index=True,nullable=False)
    Aname = Column(String(100))

class UUMAP(Base):
    __tablename__ = 'UUMAP'
    UID = Column(String(50),primary_key=False,nullable=False)
    UUID = Column(String(50),primary_key=True,nullable=True,index=True,unique=True)

r = session.query(AAMAP).filter(AAMAP.AID==str(random.randint(0,9)))
print(list(session.execute(r)).pop(0)[0])
session.close()