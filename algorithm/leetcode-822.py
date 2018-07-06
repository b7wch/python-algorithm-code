#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/8



def flipgame(fronts, backs):
    rr = []
    b = []
    for x in range(len(fronts)):
        if backs[x] == fronts[x]:
            continue
        else:
            rr.append(fronts[x])
            b.append(x, backs[x])
    rr = set(rr)
    r = []
    for e in b:
        if e in rr:
            continue
        else:
            r.append(e)
    if not r:
        return 0
    else:
        sorted(r, cmp=lambda x,y: cmp(x[1], y[1], reverse=True))


print(flipgame([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]))
