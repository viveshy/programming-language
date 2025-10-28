from collections import deque

# Deque (Double-ended queue) - allows efficient insertion and deletion from both ends
# Time complexity: O(1) for append, appendleft, pop, popleft

# Creating a deque
dq = deque()
print(f"Empty deque: {dq}")
# Expected Output: Empty deque: deque([])

# Adding elements
dq.append(1)        # Add to right end
dq.append(2)
dq.appendleft(0)    # Add to left end
print(f"After adding elements: {dq}")
# Expected Output: After adding elements: deque([0, 1, 2])

# Removing elements
right_element = dq.pop()        # Remove from right end
left_element = dq.popleft()     # Remove from left end
print(f"Removed from right: {right_element}, from left: {left_element}")
# Expected Output: Removed from right: 2, from left: 0
print(f"After removal: {dq}")
# Expected Output: After removal: deque([1])

# Creating deque from iterable
dq2 = deque([1, 2, 3, 4, 5])
print(f"Deque from list: {dq2}")
# Expected Output: Deque from list: deque([1, 2, 3, 4, 5])

# Rotating elements
dq2.rotate(2)       # Rotate right by 2 positions
print(f"After rotating right by 2: {dq2}")
# Expected Output: After rotating right by 2: deque([4, 5, 1, 2, 3])

dq2.rotate(-3)      # Rotate left by 3 positions
print(f"After rotating left by 3: {dq2}")
# Expected Output: After rotating left by 3: deque([2, 3, 4, 5, 1])

# Limited size deque (circular buffer)
limited_dq = deque(maxlen=3)
for i in range(5):
    limited_dq.append(i)
    print(f"Adding {i}: {limited_dq}")

# Extending deque
dq3 = deque([1, 2])
dq3.extend([3, 4])           # Extend right
dq3.extendleft([0, -1])      # Extend left (note: order is reversed)
print(f"Extended deque: {dq3}")

# Common use cases:
# 1. BFS in graphs/trees
# 2. Sliding window problems
# 3. Undo operations
# 4. Round-robin scheduling