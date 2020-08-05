#!/usr/bin/python3.4
# -*- coding:utf-8 -*- 
import redis
import pymysql
import config

TW_PKEY="TW" # twitter
IT_PKEY="IT" # insta

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
      # d[] : ai_userid, sns_type
      if d[1] == '3':
         # twitter
         aid="{}_{}".format(TW_PKEY,d[0].strip())
      else:
         # instagram
         aid="{}_{}".format(IT_PKEY,d[0].strip())

      print("{}".format(aid))

      #insert into redis db0 
      r.setex(aid,86400,"")
except e:
   print("Error main process {}".format(e))
finally:
   db.close()

# end.
