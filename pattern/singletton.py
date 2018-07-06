#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/27


def singleton(func):
    cache = dict()

    def single_wrapper(*args, **kwargs):
        if not cache.get(func, None):
            cache[func] = func(*args, **kwargs)
        return cache[func]

    return single_wrapper


@singleton
class Cat(object):
    pass


class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class Bob(Singleton):
    pass


a = Bob()
b = Bob()

print(id(a), id(b), id(a) == id(b))
