#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/17
# 图的表示方法
a, b, c, d, e, f, g, h = range(1, 9)
# 邻接集
graph = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]

# 邻接集字典表示法
graph_ = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}
# 邻接列表

graph = [
    [b, c, d, e, f],
    [c, e],
    [d],
    [e],
    [f],
    [c, g, h],
    [f, h],
    [f, g]
]

# 加权邻接字典

N = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},
    {c: 4, e: 3},
    {d: 8},
    {e: 7},
    {f: 5},
    {c: 2, g: 2, h: 2},
    {f: 1, h: 6},
    {f: 9, g: 8}
]


def iter_dfs(G, s):
    S, Q = set(), list()
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u


result = list(iter_dfs(graph_, 'a'))
print("->".join(result))


def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)


import collections


def bfs(G, s):
    P, Q = {s: None}, collections.deque([s])
    yield s
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
            yield v
print([x for x in bfs(graph_, 'a')])
