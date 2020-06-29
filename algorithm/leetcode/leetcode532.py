#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/25
import collections


class _Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = set()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if abs(nums[i] - nums[j]) == k:
                    if (nums[i], nums[j]) not in result and (nums[j], nums[i]) not in result:
                        result.add((nums[i], nums[j]))
        return len(result)


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = collections.Counter(nums)
        length = len(nums)
        if k == 0:
            result = 0
            for e in counter.keys():
                if counter[e] == 2:
                    result += 1
            return result
        result = set()
        for i in range(length):
            if (nums[i] + k) in counter.keys() and (nums[i] + k) not in result:
                result.add((nums[i], nums[i] + k))
            if (nums[i] - k) in counter.keys() and (nums[i] - k) not in result:
                result.add((nums[i], nums[i] - k))
        return len(result)


print(Solution().findPairs([1, 3, 1, 5, 4], 0))
