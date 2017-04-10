def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))


def str(x):
	return '%s' % x

strings = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(strings)
print(list(strings))
