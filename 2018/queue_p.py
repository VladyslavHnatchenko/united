from multiprocessing import Queue

q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

print(q)

print(q.get())
print(q.get())
print(q.get())

q.get()
# from queue import Queue
#
# q = Queue()
#
# q.put('eat')
# q.put('sleep')
# q.put('code')
#
# print(q)
#
# print(q.get())
# print(q.get())
# print(q.get())
#
# print(q.get_nowait())
#
# q.get()

# from collections import deque
#
# q = deque()
#
# q.append('eat')
# q.append('sleep')
# q.append('code')
# print(q)
#
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# # FIFO
# q = []
#
# q.append('aet')
# q.append('sleep')
# q.append('code')
#
# print(q)
# print(q.pop(0))
