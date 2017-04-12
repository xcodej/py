def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

for x in _odd_iter():
	print(x)
	if x > 1000:
		break


def _not_divisible(n):
	return lambda x: x % n > 0
