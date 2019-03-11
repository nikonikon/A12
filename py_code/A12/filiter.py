import mongodb_module
import mysql_module
import useractions
from global_defination import *

def create_filiter(Fname,AIDs):
    FID = mongodb_module.create_filiter(AIDs)
    mysql_module.sync_write_FFMAP(FID,Fname)

def getUserByAID(userTable,AID,time_begin,time_end):
    return useractions.getDetailedUserListByTimeInterval(userTable,AID,time_begin,time_end)

def countUserByUUID(userTable):
    return len(userTable)

def getUserByTableDiff(userTable1,userTable2):
    common = userTable1.keys() & userTable2.keys()
    l1 = userTable1.keys() - common
    l2 = userTable2.keys() - common
    l1.update(l2)
    print(len(l1))
    print(l1)

def getAIDsFromFID(FID): #Returns a list , contains a sequence of actions
    dataset = mongodb_module.inspect_data_in_db('FiliterTable')
    for x in dataset:
        if x['FID'] == FID:
            number_of_aid = len(x) - 2 #Number of AID
            result = list()
            for i in range(number_of_aid):
                result.append(str(x['AID'+str(i)]))
            return result

def getFIDByName(Fname):
    return mysql_module.query_FFMAP_Fname_matches(Fname)[0][0]

if __name__ == '__main__':
    #print(getAIDsFromFID('4e8cdfd66d8d6b68d0fb76a085fda7f3'))
    #print(getFIDByName('漏斗1'))
    #AIDs = getAIDsFromFID(getFIDByName('漏斗1'))
    #lst = list()
    #for AID in AIDs:
    #    x = getUserByAID('UserActions',AID,1549987200,1550237885)
    #    print(x)
    #    print(countUserByUUID(x))
    #    lst.append(x)
    #print(lst)
    dt1 = {'d41d8cd98f00b204e9800998ecf8427e': '{"Attribute1": "1", "Attribute2": "2", "Attribute3": "3"}'}
    dt2 = {'d41d8cd98f00b204e9800998ecf8427e': '{"Attribute1": "1", "Attribute2": "2", "Attribute3": "3"}',
           'AAA':'{AAF}'}

    getUserByTableDiff(dt1,dt2)