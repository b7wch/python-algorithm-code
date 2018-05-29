#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/22

from collections import deque

class ActorScheduler:

    def __init__(self):
        self._acotrs = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._acotrs[name] = actor

    def send(self, name, msg):
        actor = self._acotrs.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass

if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print("Got:", msg)

    def counter(sched):
        while True:
            n = yield
            if n == 0:
                break
            sched.send("printer", n)
            sched.send("counter", n-1)
    sched = ActorScheduler()
    sched.new_actor("printer", printer())
    sched.new_actor("counter", counter(sched))
    sched.send("counter", 10000)
    sched.run()