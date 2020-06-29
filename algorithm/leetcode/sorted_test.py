#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/22

def merge(seq):
    mid = len(seq) // 2
    lef, rgt = seq[:mid], seq[mid:]
    if len(lef) > 1:
        lef = merge(lef)
    if len(rgt) > 1:
        rgt = merge(rgt)
    res = []
    while lef and rgt:
        if lef[-1] > rgt[-1]:
            res.append(lef.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lef or rgt) + res
