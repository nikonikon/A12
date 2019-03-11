import mongodb_module
import json
from global_defination import *


def distinctCount(attributeList):#return a set containing all attributes
    s = set()
    for attribute in attributeList:
        s.update({attribute})
    return s

def valueNotExist(value):
    if value == VALUE_NOT_EXIST:
        return True
    else:
        return False

def countInList(lst):
    counts = dict()
    for element in lst:
        counts.update({element:counts.get(element,0)+1})
    return counts

def getUhashByAID(AID):
    result = []
    dataset = mongodb_module.inspect_data_in_db('UserActions')
    for data in dataset:
        if data['AID'] == AID:
            result.append(data['uhash'])
    return result

def getUhashByAIDAndTime(AID,time_begin,time_end):
    result = []
    dataset = mongodb_module.inspect_data_in_db('UserActions')
    for data in dataset:
        if data['AID'] == AID and data['ATime'] >= time_begin and data['ATime'] <= time_end:
            result.append(data['uhash'])
    return result

def getUUIDByUhash(uhash):
    dataset = mongodb_module.inspect_data_in_db('UserActions')
    for data in dataset:
        if data['uhash'] == uhash:
            return data['UUID']

def getUserAttributesByUUID(UUID):
    dataset = mongodb_module.inspect_data_in_db('UserAttributes')
    for data in dataset:
        if data['UUID'] == UUID:
            return json.loads(data['attributes'])

def with_in_time(AID,time_begin,time_end):
    user_list = []
    dataset = mongodb_module.inspect_data_in_db('UserActions')
    for data in dataset:
        if data['ATime'] >= time_begin and data['ATime'] <= time_end and data['AID'] == AID:
            user_list.append(data['UUID'])
    user_list = list(distinctCount(user_list))
    return user_list

def done_this_multiple_time(AID,times,time_begin,time_end):
    user_list = list()
    count = dict()
    dataset = mongodb_module.inspect_data_in_db('UserActions')
    for data in dataset:
        if data['ATime'] >= time_begin and data['ATime'] <= time_end and data['AID'] == AID:
            count.update({data['UUID']:count.get(data['UUID'],0)+1})
    for k,v in count.items():
        if v >= times:
            user_list.append(k)
    return user_list


if __name__ == '__main__':
    # print(with_in_time('4',1549987200,1550237885))
    print(done_this_multiple_time('4',2,1549987200,1550237885))