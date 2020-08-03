import redis

r = redis.Redis(host='1.1.1.1',port=6379,db=0,password='PASSWORD')
r.set('key','value')
r.get('key')
