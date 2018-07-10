# ####常用的数据库操作
# #增删改查CRUD
from pymongo import MongoClient

settings = {
    "uri":"mongodb://top-theme-mongo:L4SDrxH8M7jk9Z7iotMcx6FxOPLaF6CWkF2ZfUhQKiAK5zN3KqFkQFNVLCsyGNTGapk0RGLZD1YiIuVLQRoC5w==@top-theme-mongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb",   #ip
    "db_name" : "test",    #数据库名字，没有则自动创建
    "collection_name" : "test_set"   #集合名字，没有则自动创建
}

conn = MongoClient(settings["uri"])
db = conn[settings["db_name"]]
my_set = db[settings["collection_name"]]
#插入
def insert_dic(dic):
    my_set.insert(dic)
    print("插入成功")
#更新
def update(dic,newdic):
    my_set.update(dic,newdic)
    print("更新成功")
#删除
def delete(dic):
    my_set.remove(dic)
    print("删除成功")
#查找
def dbFind(dic):
    data = my_set.find(dic)
    for result in data:
        print(result)
    print("查找成功")
#查找全部
def findAll():
    # 查询全部
    for i in my_set.find():
        print(i)

if __name__ == "__main__":
    dic = {"name": "tom", "age": 18}


    insert_dic(dic)
    findAll()

    update({"name": "tom"}, {"$set": {"age": "25"}})
    dbFind({"name": "tom"})

    findAll()





