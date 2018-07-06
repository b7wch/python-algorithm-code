# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def __init__(self):
        self.result = collections.defaultdict(list)

    def do_travel(self, root, n=1):
        if not root:
            return
        self.result[n].append(root.val)
        self.do_travel(root.left, n + 1)
        self.do_travel(root.right, n + 1)

    def largestValues(self, root):
        self.do_travel(root)
        if not self.result.keys():
            return []
        result = list()
        for i in range(1, max(self.result.keys())+1):
            result.append(max(self.result[i]))
        return result