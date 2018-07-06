#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/23
import re


def check(filename):
    rule = re.compile(r"^[\w-]+(\.[\w-]+)*$")
    if rule.match(filename):
        return True
    else:
        return False


check_list = ['a', 'b', 'a.txt', 'a_b.txt', "data.NTI.API.V2.0.b-200m.20180517.0001.nti"]
for each in check_list:
    print(check(each))
error_check_list = ['..a', '/b', '\a.txt', 'a_b/.txt', "data.N\TI.API.V2.0.b-200m.20180517.0001.nti"]
print("==" * 20)
for each in error_check_list:
    print(check(each))
