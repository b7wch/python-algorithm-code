#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/29

class Node:
    lft = None
    rgt = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif node.key > key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    return node


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    if node.key > key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)


class Tree:
    root = None

    def __setitem__(self, key, value):
        self.root = insert(self.root, key, value)

    def __getitem__(self, item):
        return search(self.root, item)

    def __contains__(self, item):
        try:
            search(self.root, item)
        except KeyError:
            return False
        return True

tree = Tree()
tree[5] = 'a'
tree[3] = 'b'
tree[6] = 'c'
print(3 in tree)
