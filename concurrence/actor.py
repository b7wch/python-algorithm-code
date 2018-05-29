#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/11
from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Get: ", msg)


p = PrintActor()
p.start()
p.send("123")
p.send(123)
p.close()
p.join()


def print_actor():
    while True:
        try:
            msg = yield
            print("Got: ", msg)
        except GeneratorExit:
            print("Actor terminating")


p = print_actor()
next(p)
p.send("hello world")
p.send("world")
try:
    p.close()
except Exception:
    pass


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, "do_" + tag)(*payload)

    def do_A(self, x):
        print("Running A: ", x)

    def do_B(self, y, x):
        print("Runing B: ", y, x)


a = TaggedActor()
a.start()
a.send(("A", 1))
a.send(("B", 2, 1))
a.close()
a.join()


class Result(object):
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())
