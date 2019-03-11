import mongodb_module
import json
import common
def getEventCountByTimeInterval(UserActionTable,AIDs,data_time_begin,data_time_end) :
    #Test data:
    #Beijing time , 2019/2/13 00:00:00 --- 1549987200
    #Beijing time , 2019/2/14 00:00:00 --- 1550073600
    counts=[]
    for i in range(len(AIDs)):
        counts.append(0)

    dataset = mongodb_module.inspect_data_in_db(UserActionTable) #Search action records in required time
    for data in dataset:
        if data['ATime'] >= data_time_begin and data['ATime'] <= data_time_end:
            for i in range(len(AIDs)):
                if data['AID'] == AIDs[i]:
                    counts[i] += 1
    return counts


def getDetailedUserListByTimeInterval(UserActionTable,AID,data_time_begin,data_time_end):
    dataset = mongodb_module.inspect_data_in_db(UserActionTable)
    pending_UUIDs = []
    for data in dataset:#Get UUIDs
        if data['ATime'] >= data_time_begin and data['ATime'] <= data_time_end and data['AID'] == AID:
            pending_UUIDs.append(data['UUID'])
    dataset = mongodb_module.inspect_data_in_db('UserAttributes')
    result = dict()
    for data in dataset:
        if data['UUID'] in pending_UUIDs:
            result.update({data['UUID']:data['attributes']})
    return result

def getEventCountByAttribute(AID,PropertyName,time_begin,time_end): #Return a dict including properties and times they appear
    result = dict()
    uhash_list = common.getUhashByAIDAndTime(AID,time_begin,time_end)
    for uhash in uhash_list:
        dataset = mongodb_module.inspect_data_in_db('ActionProperties')
        for data in dataset:
            if data['uhash'] == uhash:
                actionproperties = json.loads(data['properties'])
                result.update({actionproperties[PropertyName]:result.get(actionproperties[PropertyName],0)+1})
    return result

def getDetailedUserListByAttribute(AID,PropertyName,PropertyValue,time_begin,time_end):
    result = dict()
    uhash_list = common.getUhashByAIDAndTime(AID,time_begin,time_end)
    target_uhash_list = []
    target_uuid_list = []
    for uhash in uhash_list:
        dataset = mongodb_module.inspect_data_in_db('ActionProperties')
        for data in dataset:
            if data['uhash'] == uhash:
                actionproperties = json.loads(data['properties'])
                if actionproperties[PropertyName] == PropertyValue:
                    target_uhash_list.append(uhash)
    for uhash in target_uhash_list:
        target_uuid_list.append(common.getUUIDByUhash(uhash))
    for uuid in target_uuid_list:
        result.update({uuid:common.getUserAttributesByUUID(uuid)})

    return result




if __name__ == '__main__':
    #getEventCountByTimeInterval('UserActions',['2','4'],1549987200,1550237885)
    # print(getDetailedUserListByTimeInterval('UserActions','4',1549987200,1550237885))
    #print(getEventCountByAttribute('4','Properties1',1549987200,1550237885))
    print(getDetailedUserListByAttribute('4','Properties1','1',1549987200,1550237885))