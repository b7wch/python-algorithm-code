#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/28


class Tlog(object):
    def info(self):
        print("test tlog")


tlog = Tlog()


def log(func):
    def wraper(*args, **kwargs):
        tlog.info()
        func(*args, **kwargs)

    return wraper


@log
def test():
    print("test")


test()
