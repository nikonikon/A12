from global_defination import *
from usergroup_class import *
# UGJson Structure : [[{},{},{}],[{},{},{}],[{},{},{}],[{},{},{}],[{},{},{}],[{},{},{}]]


"""
struct UGJson{
    int statement-id;
    String VarA;
    int if-statement;
    String VarB;
    int with_in_switch;
    int[2] time_interval;
    
}
"""



"""
TEST DATA : 
{'json0':{'statement-id':1,'VarA':'4','if-statement':0,'VarB':'2','with_in_switch'=0,'time_interval':[SYS_ANYTIME,SYS_ANYTIME]},'json1':{},'json2':{},'json3':{},'json4':{},'json5':{},
'json6':{},'json7':{},'json8':{},'json9':{},'json10':{},'json11':{},
'json12':{},'json13':{},'json14':{},'json15':{},'json16':{},'json17':{}}
"""
def createUserTable(UGName,UGJson):
    mongodb_module.create_UGGroup(UGName,UGJson)


def getUserTableByUGName(UGName):
    target = dict()
    dataset = mongodb_module.inspect_data_in_db('UserGroups')
    for data in dataset:
        if data['UGName'] == UGName:
            target = data
            break
    d_list = target['UGJson']

    UUID1 = set([])
    UUID2 = set([])
    for i in range(0, 6):
        for j in range(0, 3):
            number = j + i * 3
            one_of_json = d_list['json' + str(number)]
            if 'statement-id' not in one_of_json:
                continue
            if one_of_json['statement-id'] == 0:
                statement_id0 = statement_id_0(one_of_json['VarA'],one_of_json['if-statement'],one_of_json['VarB'],one_of_json['with_in_switch'],one_of_json['time_interval'])
                UUID = statement_id0.return_UUID()
            elif one_of_json['statement-id'] == 1:
                statement_id1 = statement_id_1(one_of_json['with_in_switch'],one_of_json['time_interval'])
                UUID = statement_id1.return_UUID()
            elif one_of_json['statement-id'] == 2:
                statement_id2 = statement_id_2(one_of_json['with_in_switch'],one_of_json['time_interval'])
                UUID = statement_id2.return_UUID()
            elif one_of_json['statement-id'] == 3:
                statement_id3 = statement_id_3(one_of_json['VarA'],one_of_json['if-statement'],one_of_json['VarB'])
                UUID = statement_id3.return_UUID()
            else:
                print("what f*** you choose! only [0,3] is allowed in statement-id")
                break
            UUID1 = UUID1 | UUID
        if i == 0:
            UUID2 = UUID1
        UUID2 = UUID2 & UUID1
    return list(UUID2)

if __name__ == '__main__':
    print(getUserTableByUGName('UserGroup4'))
    # print(createUserTable('UserGroup4',{'json0':{"statement-id" : 3,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "2",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json1':{},'json2':{"statement-id" : 3,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "2",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json3':{"statement-id" : 1,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "2",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json4':{"statement-id" : 1,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "1",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json5':{"statement-id" : 2,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 1,
    #         "VarB" : "2",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json6':{"statement-id" : 0,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 3,
    #         "VarB" : "1",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json7':{"statement-id" : 3,
    #         "VarA" : "Attribute3",
    #         "if-statement" : 4,
    #         "VarB" : "3",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json8':{"statement-id" : 0,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "1",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json9':{},'json10':{},'json11':{},'json12':{},'json13':{},'json14':{},'json15':{},'json16':{"statement-id" : 0,
    #         "VarA" : "Attribute2",
    #         "if-statement" : 0,
    #         "VarB" : "3",
    #         "with_in_switch" : 0,
    #         "time_interval" : [
    #             30,
    #             0
    #         ]},'json17':{}}))
    # getUserTableByUGName('UserGroup1')
    # dataset = mongodb_module.inspect_data_in_db('UserGroups')
    # for data in dataset:
    #     # c = json.dumps(data['UGJson'])
    #     print (data['UGJson'])
    #     # c = eval(c)
    #     # c = json.loads(data['UGJson'])
    #     # print(c)

