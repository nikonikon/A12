import pymongo
import time
myclient = pymongo.MongoClient("mongodb://107.182.29.165:27019/")
mydb = myclient['A12']
mycol = mydb["UserGroups"]
for x in mycol.find():
    print(x)
