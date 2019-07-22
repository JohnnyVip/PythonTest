# !/usr/bin/env python3
# -*- coding:utf-8 -*-


l = [str(i)+":"+v for i,v in enumerate(['a','b','c'])]
print(l)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print(type(zip(questions, answers)))
print(enumerate(['a','b','c']))