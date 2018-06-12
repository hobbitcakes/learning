#!/usr/bin/env python3

import threading

def worker():
    """Thread Worker functuion"""
    print('Worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
