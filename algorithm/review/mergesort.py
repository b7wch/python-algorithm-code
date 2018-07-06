#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/27


def merge_sort(seq):
    middle = len(seq) // 2
    left, right = seq[:middle], seq[middle:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    res = []
    while left and right:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res


def insert_srot(seq, i):
    if i == 0:
        return
    insert_srot(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1


def select_sort(seq, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    select_sort(seq, i - 1)


import collections


def counting_sort(seq):
    base = collections.defaultdict(list)
    for each in seq:
        base[each].append(each)
    result = []
    for i in range(min(base.keys()), max(base.keys()) + 1):
        result.extend(base[i])
    return result


import random

test = [random.randint(0, 10) for _ in range(10)]
# select_sort(test, len(test) - 1)
print(counting_sort(test))
