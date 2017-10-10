from pymongo import *
import datetime
client = MongoClient('localhost',27017)
db =client.mdb
print('alldbname=',client.database_names())
print('table_allname=',db.collection_names())
print('db=',db)
collection = db.mdb
print('table=',collection)


#print(collection)

post ={"author":"Mike",
       "text":"My first blog post",
       "tags":["Mongodb","python","pymongo"],
       "date":datetime.datetime.utcnow()
       }
post2 ={"author":"Mike",
       "text":
           {"name1":"My first blog post 1",
            "name2":"My first blog post 2",
            "name3":"My first blog post 3",
            },
       "tags":["Mongodb2x","python","pymongo"],
       "date":datetime.datetime.utcnow(),
       "key":123456
       }
#posts = db.mdb.insert_one(post)
#posts = db.mdb.insert_many(post)
#print('刚插入的post的id为',posts.inserted_id)
for i in db.mdb.find({"author":"Mike","$or":[{'date': datetime.datetime(2017, 6, 4, 13, 55, 14, 461000)},{'date': datetime.datetime(2017, 6, 4, 13, 51, 29, 181000)}]}).sort([("date",ASCENDING),( '_id',DESCENDING)]):
    print ('i=',i)
    print ('i["tags"]=',i["tags"])
uresult = db.mdb.update_many({"author":"Mike"},{"$set":{"text":"My first blog post 2"},"$currentDate":{"date":True}})
uresult1 = db.mdb.update_one({"key":123},{"$set":{"by":{"name":"My first blog post 1","name2":"My first blog post 2"}}})
uresult2 = db.mdb.update_one({"key":123},{"$set":{"by.name":"My first blog post 2x"}})
dresult = db.mdb.delete_one({"author":"Mike"})
#post_id = ObjectId('59340dafc7d8ca11381ef7f6')
#postresult = db.mdb.find_one({"_id":post_id})
#dresult = db.mdb.delete_many({"author":"Mike"})
#db.mdb.drop()
rresult = db.mdb.replace_one({"author":"Mike"},post2)
gresult = db.mdb.aggregate([{"$match":{"author":"Mike"}},{"$group":{"_id":"$tags","count":{"$sum":1}}}])
indexresult = db.mdb.create_index([( 'key',DESCENDING),( 'author',ASCENDING)])
#
# for i in db.mdb.find({"author":"Mike"}).sort([("date",ASCENDING),( '_id',DESCENDING)]):
for i in db.mdb.find({"author":"Mike"}):
    print ('i3=',i)
    print ('i3["tags"]=',i["tags"])

print('匹配次数=',uresult.matched_count)
print('匹配次数2=',uresult1.matched_count)
print('更新次数=',uresult.modified_count)
print('更新次数2=',uresult1.modified_count)
print('删除次数=',dresult.deleted_count)
print('第一个i=',db.mdb.find_one()['_id'])
for i in db.mdb.find({"key":123}):
    print ('update_key=',i)
for i in db.mdb.find({"key":123456}):
    print ('replace_key=',i)
for i in gresult:
    print ('聚合结果=',i)


#post_id = posts.insert_one(post).insert_id
#pasts.insert_one(post).i
#posts.find_one()
