#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/20


def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


print(maxProfit([1,2,3,4,5,6]))
