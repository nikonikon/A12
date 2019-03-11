import pymongo
import time
import hashlib

serverConnection = pymongo.MongoClient("mongodb://107.182.29.165:27019/")
database = serverConnection['A12']
crashDB = database['Crashes']
userActions = database['UserActions']
actionProperties = database['ActionProperties']
userAttributes = database['UserAttributes']
filiterTable = database['FiliterTable']
versionTable = database['VersionTable']
userGroups = database['UserGroups']

def create_filiter(AIDs):
    m2 = hashlib.md5()
    m2.update(AIDs.__str__().encode())
    aid_dict = dict()
    for i in range(len(AIDs)):
        aid_dict.update({'AID'+str(i):AIDs[i]})
    aid_dict.update({'FID':m2.hexdigest()})
    print(aid_dict)
    filiterTable.insert_one(aid_dict)
    return m2.hexdigest()

def sync_updateUserArritbutes(UUID,aJson):
    userAttributes.insert_one({"UUID":UUID,"attributes":aJson})

def sync_updateActionProperties(uhash,properties):
    actionProperties.insert_one({'uhash':uhash,'properties':properties})

def sync_updateCrashDB(CURL,UUID,STACK):
    crashDB.insert_one({'CTime':time.time(),'CURL':CURL,'UUID':UUID,'STACK':STACK})

def sync_updateUserAction(UUID,AID):
    m2 = hashlib.md5()
    tmpd = {'UUID':UUID,'ATime':time.time(),'AID':AID}
    m2.update(tmpd.__str__().encode())
    tmpd.update({'uhash': m2.hexdigest()})
    userActions.insert_one(tmpd)
    return m2.hexdigest()

def inspect_data_in_db(db_name):
    data = database[db_name]
    return data.find()

def inspect_data_in_db_2(db_name):
    return database[db_name]

def create_version(version_number,comment):
    versionTable.insert_one({'time':time.time(),'version':version_number,'UpdateContent':comment})

def create_UGGroup(UGName,UGJson):
    userGroups.insert_one({'UGName':UGName,'UGJson':UGJson})





if __name__ == '__main__':
    create_filiter(['5','1'])