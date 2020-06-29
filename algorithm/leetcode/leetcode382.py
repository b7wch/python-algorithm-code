#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/25
import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result = self.head.val
        next_node = self.head
        loop_index = 0
        while next_node:
            if random.randint(0, loop_index + 1) == loop_index:
                result = next_node.val
            next_node = next_node.next
            loop_index += 1
        return result


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

s = Solution(a)
print(s.getRandom())