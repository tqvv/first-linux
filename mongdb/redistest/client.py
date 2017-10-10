import redis
r = redis.Redis()
#r.set('tang','qian')
print('tang=',r.get('tang'))
print('tang=',r.get('tang'))
print('strkey=',str(r.get('strkey')))
#r.set("visit:mypage:total",100)
i = 0
for i in range(1,10):
    r.incr("visit:mypage:total")
r.incr("visit:mypage:total")
print("visit:mypage:total=" ,r.get('visit:mypage:total'))
print("dbsize=",r.dbsize())
#redis中使用的命令在pytho中基本都可以用 r.命令名()实现
print("dbsize=",r.info())
r.rpush
r.save()
print(redis.__file__)