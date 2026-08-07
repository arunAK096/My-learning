from multiprocessing import Queue

customqueue = Queue(maxsize=3)
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.full())
print(customqueue.qsize())
print(customqueue.get())
print(customqueue.qsize())
print(customqueue.empty())
print(customqueue.full())