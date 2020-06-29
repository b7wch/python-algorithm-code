#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/25
import collections


class Solution(object):
    def isIsomorphic(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp = dict()
        lenght = len(S)
        SS = [i for i in range(lenght)]
        TT = [i for i in range(lenght)]
        for i, j in enumerate(S):
            if temp.get(j) is None:
                temp[j] = SS[i]
            SS[i] = temp.get(j)
        temp.clear()
        for i, j in enumerate(T):
            if temp.get(j) is None:
                temp[j] = TT[i]
            TT[i] = temp.get(j)
        if SS == TT:
            return True
        else:
            return False


print(Solution().isIsomorphic('ab', 'aa'))
