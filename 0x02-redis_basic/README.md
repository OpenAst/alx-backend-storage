# Redis basic


This project contains  tasks for learning to use the Redis NoSQL data storage application through Python3.

---

## Resources
- [Redis commands](https://intranet.alxswe.com/rltoken/lQ8ANhVfxDTxDr2UDSyQRA)
- [Redis python client](https://intranet.alxswe.com/rltoken/imfgFhAZPlg7YMZ_tHvFZw)
- [How to Use Redis With Python](https://intranet.alxswe.com/rltoken/7SluvFvgckwVgsvrfOf1CQ)

## Install Redis on Ubuntu 18.04
`$ sudo apt-get -y install redis-server`
`$ pip3 install redis`
`$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf`

# Tasks
0. Writing strings to Redis
exercise.py contains a Python script that meets the following requirements:
- Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

- Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.
- Type-annotate store correctly. Remember that data can be a str, bytes, int or float

