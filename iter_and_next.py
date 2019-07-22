#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class IterDemo(object):

  def __init__(self):
    self.count = 0

  def __iter__(self):
    print('__iter__ run ...')
    # 该函数会由iter函数调用 返回一个可以迭代的对象
    return self

  def __next__(self):
    # 该函数会由next内建函数调用
    print('__next__ run ...')
    if self.count < 10:
      self.count += 1
      return "__next__ : %s" % self.count
    else:
      raise StopIteration



if __name__ == "__main__":
    it = IterDemo()

    it1 = iter(it)

    a = next(it1)

    print(a)

    print('=======================')

    for i in IterDemo():
        print(i)
