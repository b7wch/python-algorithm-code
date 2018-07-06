#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/26


class Solution(object):

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = list()
        temp = ''
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            temp = S[i].upper() + temp
            if len(temp) == K:
                result.append(temp)
                temp = ""
        if temp:
            result.append(temp)
        result.reverse()
        return "-".join(result)


print(Solution().licenseKeyFormatting("2-5g-3-J", 2))
