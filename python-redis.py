#!/usr/bin/env python
# -*- coding:utf-8 -*-

from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel([('172.31.0.2', 5001),
                     ('172.31.0.3', 5001),
                     ('172.31.0.4', 5001),
                     ('172.31.0.5', 5001)],
                    socket_timeout=10000)

# 获取主服务器地址
master = sentinel.discover_master('mymaster')
print(master)
# 输出：('172.31.0.2', 5001)


# 获取从服务器地址
slave = sentinel.discover_slaves('mymaster')
print(slave)
# 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]



# 获取主服务器进行写入
master = sentinel.master_for('mymaster', socket_timeout=0.5, password='redis_auth_pass', db=15)
w_ret = master.set('foo', 'bar')
# 输出：True


# # 获取从服务器进行读取（默认是round-roubin）
slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='redis_auth_pass', db=15)
r_ret = slave.get('foo')
print(r_ret)
# # 输出：bar