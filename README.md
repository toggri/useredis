# useredis
python에서 redis 사용하기 

```shell
$ pip3.4 install redis
```

```python
$ python3.4
>>> import redis
>>> r = redis.Redis(host='HOST', port=6379, db=0, password='PASSWORD')
>>> r.set('key','value')
True
>>> r.get('key')
b'value'
```

참고 : https://pypi.org/project/redis/
