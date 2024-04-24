import collections

# Counter: A subclass of dictionary for counting hashable objects
data = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 3, 2, 1]
counter = collections.Counter(data)
print("Counter:", counter)

# defaultdict: A dictionary subclass that provides a default value for missing keys
default_dict = collections.defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print("Default dictionary:", default_dict)
print("Value of 'c' in default dictionary (default value):", default_dict['c'])

# namedtuple: A factory function for creating tuple subclasses with named fields
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Named tuple:", p)
print("Accessing named tuple fields - x:", p.x, ", y:", p.y)

# deque: A list-like container with fast appends and pops on both ends
deque = collections.deque([1, 2, 3])
print("Deque:", deque)
deque.append(4)
print("Deque after appending 4:", deque)
deque.appendleft(0)
print("Deque after appending 0 to the left:", deque)
deque.pop()
print("Deque after popping from the right:", deque)
deque.popleft()
print("Deque after popping from the left:", deque)
