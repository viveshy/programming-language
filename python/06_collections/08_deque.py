"""
A deque ("deck", short for double-ended queue) adds and removes items fast at
BOTH ends.

    ┌────────┬──────────────┬──────────────────┐
    │ Action │ Right end    │ Left end         │
    ├────────┼──────────────┼──────────────────┤
    │ add    │ dq.append(x) │ dq.appendleft(x) │
    │ remove │ dq.pop()     │ dq.popleft()     │
    └────────┴──────────────┴──────────────────┘

All four take O(1) time. A list is fast at its right end only.

Why it matters: BFS takes items from the front of a queue, and sliding windows
drop items from the front. Both need a fast popleft().

We will cover:
1. Creating a deque
2. Adding at both ends
3. Removing from both ends
4. A queue for BFS
5. Rotating
6. Limited size with maxlen
7. Extending
"""

from collections import deque  # deque lives in the collections module


# ┌────────────────────────────────────────────────────────────┐
# │ 1. CREATING A DEQUE                                        │
# └────────────────────────────────────────────────────────────┘
# deque() makes an empty one. deque(items) starts with the items of a list.

dq = deque()
assert len(dq) == 0

nums = deque([1, 2, 3, 4, 5])
assert list(nums) == [1, 2, 3, 4, 5]  # list() turns it back into a list


# ┌────────────────────────────────────────────────────────────┐
# │ 2. ADDING AT BOTH ENDS                                     │
# └────────────────────────────────────────────────────────────┘
# append(x) adds at the right end. appendleft(x) adds at the left end.

dq.append(1)
dq.append(2)
dq.appendleft(0)
assert dq == deque([0, 1, 2])


# ┌────────────────────────────────────────────────────────────┐
# │ 3. REMOVING FROM BOTH ENDS                                 │
# └────────────────────────────────────────────────────────────┘
# pop() removes the right item and gives it back. popleft() does the same at
# the left.

assert dq.pop() == 2
assert dq.popleft() == 0
assert dq == deque([1])

# dq[0] and dq[-1] read the two ends without removing anything.
# Reading the middle, dq[i], is slow on a long deque: O(n).

assert nums[0] == 1
assert nums[-1] == 5


# ┌────────────────────────────────────────────────────────────┐
# │ 4. A QUEUE FOR BFS                                         │
# └────────────────────────────────────────────────────────────┘
# A queue serves items in the order they came: first in, first out.
# With a deque: append() at the right, popleft() at the left.

queue = deque()
queue.append('ana')
queue.append('bo')
assert queue.popleft() == 'ana'  # the first to come is the first served

# A stack is the other way round: last in, first out. "Undo" works like this:
# the newest action is undone first. append() and pop() both work at the right
# end, so a plain list is enough for a stack.

stack = []
stack.append('ana')
stack.append('bo')
assert stack.pop() == 'bo'


# ┌────────────────────────────────────────────────────────────┐
# │ 5. ROTATING                                                │
# └────────────────────────────────────────────────────────────┘
# rotate(k) moves every item k places to the right. Items that fall off the
# right end come back in at the left. rotate(-k) moves them k places left.

circle = deque([1, 2, 3, 4, 5])
circle.rotate(2)
assert circle == deque([4, 5, 1, 2, 3])

circle.rotate(-3)
assert circle == deque([2, 3, 4, 5, 1])


# ┌────────────────────────────────────────────────────────────┐
# │ 6. LIMITED SIZE WITH MAXLEN                                │
# └────────────────────────────────────────────────────────────┘
# deque(maxlen=3) holds at most 3 items. Adding to a full deque drops an item
# from the other end.

last3 = deque(maxlen=3)
for i in range(5):
    last3.append(i)
assert list(last3) == [2, 3, 4]  # 0 and 1 were pushed out


# ┌────────────────────────────────────────────────────────────┐
# │ 7. EXTENDING                                               │
# └────────────────────────────────────────────────────────────┘
# extend(items) adds many items at the right, in order.

more = deque([1, 2])
more.extend([3, 4])
assert more == deque([1, 2, 3, 4])


print('All checks passed.')
