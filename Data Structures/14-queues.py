# Fi Fo = First In - First Out

# its like queue in real world, queue of ppl first in restroom, the first person in the queue is the first person who will get it.
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.popleft()
print(queue)
if not queue:
    print("empty")
