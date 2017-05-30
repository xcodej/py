from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)

from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
