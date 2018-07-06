#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/19


def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n-1, 1, -1):
        for x in range(i):
            if (prices[i] - prices[x]) > max_profit:
                max_profit = prices[i] - prices[x]
    return max_profit

def maxprofit2(prices):
    minprice = float('inf')
    maxprofit = 0
    for i in range(len(prices)):
        if minprice > prices[i]:
            minprice = prices[i]
        elif prices[i]-minprice > maxprofit:
            maxprofit = prices[i] - minprice
    return maxprofit
print(maxprofit2([7, 1, 5, 3, 6, 4]))
