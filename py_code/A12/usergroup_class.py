
import time
import mongodb_module
import json

one_hour = 60 * 60
one_day = 24 * one_hour
now_unix_time = time.time()


class statement_id_0:
    def __init__(self, VarA, if_statement, VarB, with_in_switch, time_interval):
        # UUID做过VarA 条件 VarB(次数) 在 判断 time_interval
        # with_in_time (VarA,time_begin,time_end)
        # 1.将所有AID = VarA 且符合时间的 detail 从 useraction 表中筛选 为list(UUID)
        # 2.time_begin
        self.VarA = VarA
        self.VarB = VarB
        self.if_statement = if_statement
        self.with_in_switch = with_in_switch
        self.time_interval = time_interval




    def __get_time_begin(self):
        if self.with_in_switch == 0:  # 任意时间
            time_begin = 0
            return time_begin

        elif self.with_in_switch == 1:  # 新增后
            pass
            # 获得用户注册时间

        elif self.with_in_switch == 2:  # 最近
            time_begin = now_unix_time - self.time_interval[0] * one_day
            return time_begin

        elif self.with_in_switch == 3:  # 固定时间
            time_begin = self.time_interval[0]
            return time_begin




    def __get_time_end(self):
        if self.with_in_switch == 0:  # 任意时间
            time_end = 2147483646
            return time_end

        elif self.with_in_switch == 1:  # 新增后
            pass
            # 获得用户注册时间

        elif self.with_in_switch == 2:  # 最近
            time_end = now_unix_time
            return time_end

        elif self.with_in_switch == 3:  # 固定时间
            time_end = self.time_interval[1]
            return time_end




    def __with_in_time(self,AID, time_begin, time_end):
        user_list = []
        dataset = mongodb_module.inspect_data_in_db('UserActions')
        for data in dataset:
            if data['ATime'] >= time_begin and data['ATime'] <= time_end and data['AID'] == AID:
                user_list.append(data['UUID'])
        return user_list




    def __retrun_register_time(self,UUID):
        register_time = 0
        dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
        for dataUser in dataUserAttributes:  # 找到register_time
            if UUID == dataUser['UUID']:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if 'register_time' not in attributes:
                    print("you f*** dont write register_time in %s" % (UUID))
                    break
                else:
                    register_time = attributes['register_time']  ######################
                    break
        return register_time




    def __dont_care_me(self):
        # 未固定次数
        if self.with_in_switch != 1:
            UUID = self.__with_in_time(self.VarA, self.__get_time_begin(), self.__get_time_end())
            return UUID

        elif self.with_in_switch == 1:
            user_list = []
            dataset = mongodb_module.inspect_data_in_db('UserActions')
            for data in dataset:
                if data['AID'] == self.VarA:
                    register_time = self.__retrun_register_time(data['UUID'])
                    if data['ATime'] >= register_time and data['ATime'] <= register_time + one_day * self.time_interval[1]:
                        user_list.append(data['UUID'])
            return user_list




    def return_UUID(self):
        user_list = []
        UUID = self.__dont_care_me()
        set_UUID = set(UUID)

        if self.if_statement == 0:  # >
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) > int(self.VarB):
                    user_list.append(single_UUID)

        elif self.if_statement == 1:  # =
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) == int(self.VarB):
                    user_list.append(single_UUID)

        elif self.if_statement == 2:  # <
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) < int(self.VarB):
                    user_list.append(single_UUID)

        elif self.if_statement == 3:  # >=
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) >= int(self.VarB):
                    user_list.append(single_UUID)

        elif self.if_statement == 4:  # <=
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) <= int(self.VarB):
                    user_list.append(single_UUID)

        elif self.if_statement == 5:  # !=
            for single_UUID in set_UUID:
                if UUID.count(single_UUID) != int(self.VarB):
                    user_list.append(single_UUID)

        return set(user_list)
        # 最终实现目标



class statement_id_1:
    def __init__(self, with_in_switch, time_interval):
        # 新增于 with_in_switch(最近/固定时间)
        self.with_in_switch = with_in_switch
        self.time_interval = time_interval




    def __get_time_begin(self):
        if self.with_in_switch == 0:  # 最近
            time_begin = now_unix_time - self.time_interval[0] * one_day
            return time_begin

        elif self.with_in_switch == 1:  # 固定时间
            return self.time_interval[0]
            # 获得用户注册时间




    def __get_time_end(self):
        if self.with_in_switch == 0:  # 最近
            time_end = now_unix_time
            return time_end

        elif self.with_in_switch == 1:  # 固定时间
            return self.time_interval[1]
            # 获得用户注册时间




    def __retrun_register_time(self,UUID):
        register_time = 0
        dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
        for dataUser in dataUserAttributes:  # 找到register_time
            if UUID == dataUser['UUID']:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if 'register_time' not in attributes:
                    print("you f*** dont write register_time in %s" % (UUID))
                    break
                else:
                    register_time = attributes['register_time']  ######################
                    break
        return register_time





    def return_UUID(self):
        user_list = []
        dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
        for dataUser in dataUserAttributes:
            single_UUID = dataUser['UUID']
            register_time = self.__retrun_register_time(single_UUID)
            if register_time <= self.__get_time_end() and register_time >= self.__get_time_begin():
                user_list.append(single_UUID)
        return set(user_list)




class statement_id_2:
    def __init__(self, with_in_switch, time_interval):
        # 活跃于 with_in_switch(最近/固定时间)
        self.with_in_switch = with_in_switch
        self.time_interval = time_interval




    def __get_time_begin(self):
        if self.with_in_switch == 0:  # 最近
            time_begin = now_unix_time - self.time_interval[0] * one_day
            return time_begin

        elif self.with_in_switch == 1:  # 固定时间
            return self.time_interval[0]
            # 获得用户活跃时间




    def __get_time_end(self):
        if self.with_in_switch == 0:  # 最近
            time_end = now_unix_time
            return time_end

        elif self.with_in_switch == 1:  # 固定时间
            return self.time_interval[1]
            # 获得用户活跃时间




    def return_UUID(self):
        user_list = []
        dataset = mongodb_module.inspect_data_in_db('UserActions')
        for data in dataset:
            if data['ATime']  <= self.__get_time_end() and data['ATime'] >= self.__get_time_begin():
                user_list.append(data['UUID'])
        return set(user_list)


class statement_id_3:
    def __init__(self, VarA, if_statement, VarB):
        # UUID 的 属性VarA 判断if_statement 属性值VarB
        self.VarA = VarA
        self.VarB = VarB
        self.if_statement = if_statement

    def __int_or_str(self):
        flag = 0
        dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
        for dataUser in dataUserAttributes:
            attributes = dataUser['attributes']
            attributes = json.loads(attributes)
            if self.VarA in attributes:
                if type(attributes[self.VarA]) == str:
                    flag = 1
                    return flag
                elif type(attributes[self.VarA]) == int:
                    flag = 2
                    return flag
                else:
                    print("what f*** you give me! its neither str nor int")
                    return flag
                break
            else:
                continue
        if flag == 0:
            print("what f*** attribute you choose! no one in databases! f***")
            return flag

    def __if_int(self):
        user_list = []
        if self.if_statement == 0:  # >
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] > int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 1:  # =
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] == int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 2:  # <
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] < int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 3:  # >=
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] >= int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 4:  # <=
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] <= int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 5:  # !=
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] != int(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        else:
            print("what f*** you choose only [0,5] is allowed in int")

        return user_list

    def __if_str(self):
        user_list = []
        if self.if_statement == 0:  # 是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] == str(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 1:  # 包含
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if str(self.VarB) in attributes[self.VarA]:
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 2:  # 不是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] != str(self.VarB):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 3:  # 不包含
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if str(self.VarB) not in attributes[self.VarA]:
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 4:  # 开头是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA].startswith(str(self.VarB)):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 5:  # 结尾是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA].endswith(str(self.VarB)):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 6:  # 开头不是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if not attributes[self.VarA].startswith(str(self.VarB)):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 7:  # 结尾不是
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if not attributes[self.VarA].endswith(str(self.VarB)):
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 8:  # 是空值
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] == 'null':
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        elif self.if_statement == 9:  # 不空值
            dataUserAttributes = mongodb_module.inspect_data_in_db('UserAttributes')
            for dataUser in dataUserAttributes:
                attributes = dataUser['attributes']
                attributes = json.loads(attributes)
                if self.VarA in attributes:
                    if attributes[self.VarA] != 'null':
                        user_list.append(dataUser['UUID'])
                else:
                    continue
        else:
            print("what f*** you choose only [0,9] is allowed in str")

        return user_list

    def return_UUID(self):
        if self.__int_or_str() == 1:
            return set(self.__if_str())
        elif self.__int_or_str() == 2:
            return set(self.__if_int())

