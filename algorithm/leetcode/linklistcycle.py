#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        S = set()
        while head:
            if id(head) not in S:
                S.add(id(head))
            else:
                return True
            head = head.next
        return False


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = "{0:032b}"