#!/usr/bin/python3.4
# -*- coding:utf-8 -*- 
import redis
import pymysql
import config

# connect redis
try:
   r=redis.Redis(host=config.RHOST,port=config.RPORT,db=config.RDB,password=config.RPASSWORD)
   print("Redis Connected {} ".format(r))
except e:
   print("Error redis {}".format(e))

# connect mysql
try:
   db=pymysql.connect(config.MHOST,config.MUSER,config.MPASSWORD,config.MDB)
   cur=db.cursor()
   print("Mysql Connected {} ".format(cur))
except e:
   print("Error mysql {}".format(e))


# select data
try:
   query=config.QUERY
   cur.execute(query)
   data = cur.fetchall()
   for d in data:
      print("{}".format(d[0]))
     # insert into redis db0 
      r.setex(d[0],86400,"")
except e:
   print("Error main process {}".format(e))
finally:
   db.close()

# end.
