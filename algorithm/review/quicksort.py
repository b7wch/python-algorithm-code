#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/27

def quick_sort(seq):
    if not seq:
        return []
    index, l, h = partition(seq)
    return quick_sort(l) + [index] + quick_sort(h)


def partition(seq):
    index = seq[0]
    l = [x for x in seq[1:] if x < index]
    h = [x for x in seq[1:] if x >= index]
    return index, l, h


import random

test = [random.randint(0, 10) for _ in range(10)]
print(quick_sort(test))
