#!/usr/bin/python3.4

import redis
import pymysql
import config

r=redis.Redis(host=config.RHOST,port=config.RPORT,db=config.RDB,password=config.RPASSWORD)
KEY='key'
VAL='value'
r.setnx(KEY,VAL)
rval = r.get(KEY)
print("Redis Data {} => {} ".format(KEY,rval))

db=pymysql.connect(config.MHOST,config.MUSER,config.MPASSWORD,config.MDB)
cur=db.cursor()
cur.execute("select version()")
data = cur.fetchone()
print("Database version {}".format(data))
db.close()
