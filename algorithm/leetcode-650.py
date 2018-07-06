#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/19

def minSteps(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i] = dp[j] + i / j
                break
    return dp[n]


print(minSteps(88))
