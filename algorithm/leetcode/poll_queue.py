#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/1/18
import queue
import socket
import os
import select
import threading


class PollableQueue(queue.Queue):
    def _init(self, maxsize):
        super()._init(maxsize=maxsize)
        if os.name == "posix":
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 0))
            server.listen(1)
            print("server fileno:", server.fileno())
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("_putsocket fileno:", self._putsocket.fileno())
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            print("_getsocket fileno:", self._getsocket.fileno())
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self, block=True, timeout=None):
        self._getsocket.recv(1)
        return super().get()


def consumer(queues):
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print("Got:", item)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()

t = threading.Thread(target=consumer, args=([q1, q2, q3], ))
t.daemon = True
print("start consumer thread")
t.start()

print("start put")
q1.put(1)
q2.put(10)
q3.put("hello world")
q2.put('213')
t.join()