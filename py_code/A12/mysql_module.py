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

engine = create_engine("mysql+mysqldb://root:A12A12A12@107.182.29.165:3308/A12")

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

class FFMAP(Base):
    __tablename__ = 'FFMAP'
    FID = Column(String(50),primary_key=True,nullable=False,index=True,unique=True)
    Fname = Column(String(50),nullable=False)

def sync_write_AAMAP(AID,Aname):
    session.add(AAMAP(AID=AID,Aname=Aname))
    session.commit()

def sync_write_UUMAP(UUID,UID):
    session.add(UUMAP(UUID=UUID,UID=UID))
    session.commit()

def sync_write_FFMAP(FID,Fname):
    session.add(FFMAP(FID=FID,Fname=Fname))
    session.commit()

def async_write_AAMAP(AID,Aname):
    session.add(AAMAP(AID=AID,Aname=Aname))

def async_write_UUMAP(UUID,UID):
    session.add(UUMAP(UUID=UUID,UID=UID))

def async_write_FFMAP(FID,Fname):
    session.add(FFMAP(FID=FID,Fname=Fname))

def query_FFMAP_Fname_matches(Fname):
    r = session.query(FFMAP).filter(FFMAP.Fname == Fname)
    return list(session.execute(r))

def sync():
    session.commit()

if __name__ == '__main__':
    print(query_FFMAP_Fname_matches('漏斗1'))