"""
Deque (double-ended queue) allows fast adding and removing at BOTH ends.
append, appendleft, pop and popleft all take the same short time however long
the deque is. (A list is fast at its right end only: removing its first item
makes every other item move.)

Common uses:
1. BFS in graphs and trees
2. Sliding window problems
3. Undo operations
4. Round-robin scheduling
"""

from collections import deque

# 1. CREATING A DEQUE
# _____________________
dq = deque()
assert len(dq) == 0

dq2 = deque([1, 2, 3, 4, 5])  # from a list
assert list(dq2) == [1, 2, 3, 4, 5]

# 2. ADDING AT BOTH ENDS
# _____________________
dq.append(1)  # Add to right end
dq.append(2)
dq.appendleft(0)  # Add to left end
assert dq == deque([0, 1, 2])

# 3. REMOVING FROM BOTH ENDS
# _____________________
right_element = dq.pop()  # Remove from right end
left_element = dq.popleft()  # Remove from left end
assert right_element == 2
assert left_element == 0
assert dq == deque([1])

# 4. ROTATING
# _____________________
dq2.rotate(2)  # Rotate right by 2 positions
assert dq2 == deque([4, 5, 1, 2, 3])

dq2.rotate(-3)  # Rotate left by 3 positions
assert dq2 == deque([2, 3, 4, 5, 1])

# 5. LIMITED SIZE (A CIRCULAR BUFFER)
# _____________________
# With maxlen, adding to a full deque drops an item from the other end
limited_dq = deque(maxlen=3)
for i in range(5):
    limited_dq.append(i)

assert list(limited_dq) == [2, 3, 4]  # 0 and 1 were pushed out

# 6. EXTENDING
# _____________________
dq3 = deque([1, 2])
dq3.extend([3, 4])  # Extend right
dq3.extendleft([0, -1])  # Extend left: adds 0, then -1, so the order comes out reversed
assert dq3 == deque([-1, 0, 1, 2, 3, 4])

print('All checks passed.')
