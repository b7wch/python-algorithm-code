#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/13
from collections import defaultdict


# 归并排序 nlg(n)
def merge_sort(seq):
    mid = len(seq) // 2
    lef, rgt = seq[:mid], seq[mid:]
    if len(lef) > 1:
        lef = merge_sort(lef)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    while lef and rgt:
        if lef[-1] > rgt[-1]:
            res.append(lef.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lef or rgt) + res


# 递归版插入排序
def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1


# 递归选择排序
def sel_sort_rec(seq, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i - 1)


# 计数排序
def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C) + 1):
        B.extend(C[k])
    return B


# 快速排序: 也可以叫做一种折半排序
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quick_sort(lo) + [pi] + quick_sort(hi)


def bubble_sort(seq):
    length = len(seq)
    for i in range(length):
        for j in range(length - i):
            if j + 1 >= length:
                break
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


if __name__ == '__main__':
    t = [9 - x for x in range(9)]
    bubble_sort(t)
    print(t)
