"""
/onRegister
特殊-注册事件
1、UUID UUID
2、用户名 userName
3、用户信息（json） userAttributes

/onLogin
特殊-登录事件
1、UUID UUID
2、用户名 userName

/onUserAction
事件类：
1、当事件发生时：
1.1、事件ID（String) AID
1.2、事件属性（json） actionProperties
1.3、UUID UUID

/onCrash
崩溃事件：
1、UUID UUID
2、URL URL

"""
from flask import Flask
from flask import json
from flask import request
from flask import abort
import mysql_module
import mongodb_module

app = Flask(__name__)
@app.route('/',methods=['GET'])
def approot():    return 'INDEX'

@app.route('/statistics/onRegister',methods=['POST'])
def s_onRegister():
    if request.method == 'POST' :
        data = json.loads(request.data)
        user = data['userName']
        uuid = data['UUID']
        userAttributes = data['userAttributes']
        mysql_module.sync_write_UUMAP(uuid,user)
        mongodb_module.updateUserArritbutes_sync(uuid,userAttributes)
        return 'OK'
    abort(400)

@app.route('/statistics/onLogin', methods=['POST'])
def s_onLogin():
    if request.method == 'POST' :
        data = json.loads(request.data)
        user = data['userName']
        uuid = data['UUID']
        mysql_module.sync_write_UUMAP(uuid,user)
        return 'OK'
    abort(400)


@app.route('/statistics/onUserAction', methods=['POST'])
def s_onUserAction():
    if request.method == 'POST' :
        data = json.loads(request.data)
        AID = data['AID']
        Properties = data['actionProperties']
        UUID = data['UUID']
        uhash = mongodb_module.sync_updateUserAction(UUID,AID)
        mongodb_module.sync_updateActionProperties(uhash,Properties)
        return 'OK'
    abort(400)


@app.route('/statistics/onCrash', methods=['POST'])
def s_onCrash():
    if request.method == 'POST' :
        data = json.loads(request.data)
        URL = data['URL']
        UUID = data['UUID']
        STACK = data['STACK']
        mongodb_module.sync_updateCrashDB(URL,UUID,STACK)
        return 'OK'
    abort(400)



if __name__ == '__main__':
    app.run(debug=False)
