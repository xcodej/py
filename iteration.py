# dict
d = {'key1': 1, 'key2': 2, 'key3': '3'}
for key in d:
	print(key)
	print(d[key])

for value in d.values():
	print(value)

for key, value in d.items():
	print('key:', key, 'value:', value)

# String
for ch in 'String':
	print(ch)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
print(isinstance([1, 2, 3], Iterable))

# list
aList = ['one', 'two', 'three', 'four']
for index, value in enumerate(aList):
	print(index, value)

for one, two, three in [(11, 22, 33), (21, 22, 23)]:
	print(one, two, three)
