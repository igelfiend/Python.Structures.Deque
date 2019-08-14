#!/usr/bin/env python
# coding=utf8

from copy import deepcopy


class Deque:
    def __init__(self):
        self.data = []

    def addFront(self, item):
        self.data.insert(0, item)

    def addTail(self, item):
        self.data.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        else:
            value = deepcopy(self.data[0])
            del self.data[0]
            return value

    def removeTail(self):
        if self.size() == 0:
            return None
        else:
            value = deepcopy(self.data[-1])
            del self.data[-1]
            return value

    def size(self):
        return len(self.data)
