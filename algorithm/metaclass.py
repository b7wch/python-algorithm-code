#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/1/19


class MetaType(type):
    def __new__(mcs, *args, **kwargs):
        print("metaclass new")
        return super().__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("meta class init")
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("metaclass call")
        return super().__call__(*args, **kwargs)


class MetaObject(metaclass=MetaType):
    def __new__(cls, *args, **kwargs):
        print("Test new")
        return super().__new__(cls)

    def __init__(self, a):
        self.a = a
        print("Test init")


class Met(metaclass=MetaType):
    pass


print("process run")
t = MetaObject(1)
print(t.a)
print("process end")
