#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/19

class A(object):
    """123"""
    queue = list()
    test = 0
    if len(queue):
        print('not empty')
    else:
        print('empty')


class B(A):
    def add(self):
        self.queue.append('yeah')

    def change(self):
        self.test = 1


if __name__ == '__main__':
    print('start main')
    a = B()
    print(A.queue)
    print(A.test)

    print(a.queue)
    print(a.test)
    print("change -------")
    a.add()
    a.change()
    print(A.queue)
    print(A.test)

    print(a.queue)
    print(a.test)
    b = B()
    print('---'*9)
    print(A.queue)
    print(A.test)

    print(a.queue)
    print(a.test)

    print(b.queue)
    print(b.test)