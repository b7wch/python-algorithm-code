#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/19

def jump_ways(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


def jump_ways_2(n):
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    return jump_ways(n - 1) + jump_ways(n - 2) + jump_ways(n - 3)


print(jump_ways(15))

print(jump_ways_2(15))
